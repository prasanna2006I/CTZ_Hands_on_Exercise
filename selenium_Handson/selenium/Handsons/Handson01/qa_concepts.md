# Hands-On 1: QA Concepts, Functional Testing & Defect Lifecycle

## Task 1: Map Testing Types to a Real System

Target system: **Course Management API**

### 1. One test case per test level

**Unit Testing** — test a single function in isolation
- Function: `calculate_course_fee(base_fee, discount_percent)`
- Test: Call the function directly with `base_fee=1000`, `discount_percent=10` and check it returns `900`. No database, no HTTP call, no other module is involved — just this one function.

**Integration Testing** — two components working together
- Components: the `POST /api/courses/` endpoint + the database layer.
- Test: Call the endpoint with a valid course payload and then query the database directly to confirm a matching row was actually inserted with the correct values. This checks that the API layer and the persistence layer are talking to each other correctly.

**System Testing** — full end-to-end flow
- Test: Starting from an empty test database, send a `POST /api/courses/` request, then send a `GET /api/courses/{id}` request for the same course, and finally send a `DELETE /api/courses/{id}` request, verifying the correct response and state at every step. This exercises the whole system as a black box, exactly as a real client would use it.

**User Acceptance Testing (UAT)** — from the perspective of an actual college admin
- Test: A college admin logs into the admin portal, fills in the "Add New Course" form with real course details (name, code, credits, instructor), clicks Save, and confirms the course now shows up in the course listing page the way they expect it to. The admin is not thinking about endpoints or JSON — only about "does the system do what I need it to do".

### 2. Functional vs Non-Functional classification

| Test Case | Classification |
|---|---|
| Unit test on `calculate_course_fee` | Functional |
| Integration test on POST + DB | Functional |
| System end-to-end CRUD flow | Functional |
| UAT — admin adds a course | Functional |

**Non-Functional example:** Load the `POST /api/courses/` endpoint with 200 concurrent requests and confirm the 95th percentile response time stays under 500ms and the server does not return any 5xx errors. This is a **performance** test — it does not check *what* the API does, it checks *how well* it does it under load.

### 3. Black-Box vs White-Box Testing

- **Black-Box Testing**: The tester has no knowledge of the internal code, only the inputs and expected outputs. For example, sending a course name that is 200 characters long to `POST /api/courses/` and checking the response, without ever looking at the validation code that handles it.
- **White-Box Testing**: The tester (or developer) looks at the actual source code — branches, conditions, loops — and designs tests to exercise every code path. For example, looking at the validation function and writing a specific test for the `if len(name) > 150:` branch because that line exists in the code.

A **QA tester** typically performs black-box testing, since their job is to validate behaviour from the user's point of view without depending on implementation details. A **developer** typically performs white-box testing, since they already have full visibility into the code they just wrote and can target specific logic branches.

### 4. Formal test cases for POST /api/courses/

| Test Case ID | Description | Preconditions | Test Steps | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|---|
| TC_COURSE_001 | Create a course with valid data | API is running, DB is reachable, no course with the same code exists | 1. Send POST /api/courses/ with valid JSON body (name, code, credits, instructor) 2. Capture response | Response status is 201 Created; response body contains the new course with a generated ID | | |
| TC_COURSE_002 | Reject a course with a duplicate course code | A course with code "CS101" already exists in the DB | 1. Send POST /api/courses/ with code "CS101" again 2. Capture response | Response status is 409 Conflict (or 400); error message indicates the course code already exists | | |
| TC_COURSE_003 | Reject a course with missing required field | API is running | 1. Send POST /api/courses/ with the "name" field omitted 2. Capture response | Response status is 422 Unprocessable Entity (or 400); error message identifies "name" as required | | |

---

## Task 2: Defect Lifecycle & Severity Classification

### 5. Defect Lifecycle

```
   New
    |
    v
 Assigned  -----------------> Rejected
    |                              ^
    v                              |
   Open   ------------------------>|
    |                              |
    v                              |
  Fixed   -----------------> Deferred
    |
    v
 Retest
    |
    v
 Verified
    |
    v
  Closed
```

- **New**: The defect has just been logged by QA and has not been looked at yet.
- **Assigned**: A lead or manager has reviewed it and assigned it to a specific developer.
- **Open**: The developer has accepted the defect and is actively working on a fix.
- **Fixed**: The developer has completed the fix and checked in the code.
- **Retest**: QA picks up the fixed build and re-runs the original failing steps.
- **Verified**: QA confirms the fix works and no longer reproduces the defect.
- **Closed**: The defect is formally closed, usually after verification, and tracked as resolved.

**Rejected path**: At the "Assigned" or "Open" stage, a developer may determine the reported behaviour is not actually a defect (e.g. it is working as designed, or it is a duplicate). The defect is moved to **Rejected** with a comment explaining why, and it goes back to QA to either accept the rejection or dispute it.

**Deferred path**: After a defect is confirmed as valid but the team decides it is low impact and not worth fixing in the current release (e.g. due to time or budget constraints), it is moved to **Deferred** and revisited in a future release.

### 6. Severity and Priority classification

| Bug | Severity | Priority | Justification |
|---|---|---|---|
| a) POST /api/courses/ returns 500 for all requests | Critical | P1 | Core functionality is completely broken for every user — nobody can create a course at all. This blocks the main feature of the system, so it must be fixed immediately. |
| b) Course names > 150 chars are silently truncated, no error | Medium | P3 | The system does not crash and the feature technically still works, but data is being silently altered without informing the user, which is a real data-integrity concern — just not urgent enough to stop other work. |
| c) Typo in the /docs Swagger description | Low | P4 | Purely cosmetic, has zero impact on functionality. Can be fixed whenever convenient, even in a later release. |
| d) Login with correct credentials occasionally returns 401 (intermittent) | High | P1 | Even though it does not fail every time, it directly blocks users from accessing the system when it does occur, and intermittent bugs are a sign of deeper instability (e.g. a race condition) that needs urgent investigation before it gets worse. |

### 7. Defect Report — Bug (a)

| Field | Value |
|---|---|
| Defect ID | DEF-2026-0142 |
| Title | POST /api/courses/ returns 500 Internal Server Error for all requests |
| Environment | Staging, Ubuntu 22.04, Python 3.11, Chrome N/A (backend API) |
| Build Version | v1.4.2-staging |
| Severity | Critical |
| Priority | P1 |
| Steps to Reproduce | 1. Authenticate as an admin user and obtain a valid token. 2. Send a POST request to /api/courses/ with a fully valid JSON payload (name, code, credits, instructor). 3. Observe the response. |
| Expected Result | Server responds with 201 Created and the newly created course object in the response body. |
| Actual Result | Server responds with 500 Internal Server Error and no course is created in the database. |
| Attachments | screenshot of 500 error |

### 8. Severity vs Priority

**Severity** measures how badly the defect affects the system's functionality — the technical impact. **Priority** measures how urgently the business wants it fixed, regardless of technical impact.

**Example where High Severity does not mean High Priority**: Imagine a rarely-used "Export course list to legacy XML format" feature crashes the whole export module whenever it's used (High Severity — it completely breaks that feature). But almost no one uses this legacy export anymore, because the system moved to a newer export format months ago. The business may decide this is **Low Priority**, because fixing it isn't urgent even though the technical severity is high — there are more valuable things to work on first.
