# Hands-On 2: SDLC vs TDLC — V-Model & Agile QA Integration

## Task 1: V-Model Mapping

### 9. V-Model Diagram (ASCII)

```
Requirements  ------------------------------->  Acceptance Testing
     \                                                  /
      \                                                /
   System Design  ------------------------->  System Testing
        \                                            /
         \                                          /
    Architecture Design  ---------------->  Integration Testing
           \                                      /
            \                                    /
        Module Design  ----------------->  Unit Testing
              \                                /
               \                              /
                \____________________________/
                          Coding
                    (bottom vertex)
```

The left side is the **development branch** (going down, getting more detailed). The right side is the **testing branch** (going up, getting broader again). Every development phase has a matching testing phase drawn opposite it, joined at the "Coding" vertex at the bottom.

### 10. SDLC phase → TDLC phase → test artifact produced

| SDLC Phase | Matching TDLC Phase | Test Artifact Produced During Dev Phase |
|---|---|---|
| Requirements | Acceptance Testing | Acceptance Test Plan / User Acceptance criteria are drafted while requirements are being written |
| System Design | System Testing | System Test Plan, covering end-to-end scenarios based on the overall system design |
| Architecture Design | Integration Testing | Integration Test Plan, identifying which modules/components need to be tested together |
| Module Design | Unit Testing | Unit Test Plan / test case list, based on the detailed design of each individual module |
| Coding | — | The code itself, plus developer unit tests written alongside it |

### 11. Entry and Exit Criteria per TDLC phase

**Unit Testing**
- Entry Criteria: Module code is complete and compiles/runs; unit test cases are written and reviewed.
- Exit Criteria: All planned unit tests executed; code coverage meets the agreed threshold (e.g. 80%); no open critical defects in the unit.

**Integration Testing**
- Entry Criteria: Unit testing is complete for all modules being integrated; integration test environment is ready; stub/mock services are available where needed.
- Exit Criteria: All integration test cases executed; interfaces between modules verified as working; no open critical/high defects on module interactions.

**System Testing**
- Entry Criteria: All modules are integrated and integration testing is complete; system test environment mirrors production closely; test data is prepared.
- Exit Criteria: All system test cases executed; end-to-end flows pass; defect count is below the agreed threshold; no open critical/high defects.

**Acceptance Testing**
- Entry Criteria: System testing is complete and signed off; UAT environment is ready; business/end users are available.
- Exit Criteria: All acceptance criteria from the requirements are verified by actual business stakeholders; sign-off is obtained from the product owner/client.

### 12. Two early QA engagement points in the Course Management API project

1. **During the Requirements phase**: QA reviews the requirements document for the Course Management API (e.g. "a course code must be unique") and asks clarifying questions before any code is written — for example, "what should happen if two admins submit the same course code at the same second?" Catching this ambiguity here is far cheaper than finding it as a bug during system testing.
2. **During Architecture/Module Design**: QA reviews the proposed API contract (endpoint names, request/response schemas) before implementation starts, checking that the design is actually testable — for example, confirming that error responses will include a machine-readable error code, not just a free-text message, so automated tests can assert on it reliably.

---

## Task 2: Agile QA and Shift-Left Testing

### 13. Three problems with testing only after development is complete (Waterfall)

1. **Defects are found late and are expensive to fix.** If a requirements misunderstanding for the Course Management API (e.g. course codes should be case-insensitive) is only discovered during system testing, the fix may ripple through the database schema, the API layer, and the frontend — far more costly than catching it during design.
2. **Testing gets compressed under schedule pressure.** If development runs late, the testing phase is usually the one that gets squeezed, since the release date rarely moves. This leads to rushed, incomplete testing right before release — the riskiest possible time to cut corners.
3. **No early feedback loop for the developers.** Developers write the entire Course Management API before getting any test feedback, so bad design decisions (e.g. tight coupling between the course and enrollment modules) only surface once it's expensive to change them.

### 14. QA's role in each Agile ceremony

- **Sprint Planning**: QA works with the team to define clear, testable Acceptance Criteria for each user story (e.g. "Add Course" story) before it's committed to the sprint, so everyone agrees up front on what "done" means.
- **Daily Standup**: QA reports any blocking issues — for example, a test environment that's down, or a defect that's blocking further testing of a story — so the team can react quickly.
- **Sprint Review**: QA supports the demo by making sure the features shown actually satisfy the acceptance criteria, and may help demonstrate test coverage or known issues to stakeholders.
- **Retrospective**: QA raises process improvements — for example, "we found too many defects in the last sprint related to missing input validation; let's add a validation checklist to our Definition of Ready."

### 15. Four Shift-Left practices applied to the Course Management API

(a) **Reviewing requirements for testability** — Before development starts, QA checks that a requirement like "course fees must be calculated correctly" is rewritten with specific, testable numbers and rules (e.g. exact discount tiers), rather than left vague.

(b) **Writing test cases before code (TDD/BDD)** — For the `POST /api/courses/` endpoint, the team writes the Given-When-Then acceptance scenarios (see Task 2, Step 16 below) before a single line of the endpoint is implemented, so the implementation is built to satisfy already-agreed test scenarios.

(c) **Static code analysis** — Tools like `flake8`, `pylint`, or `bandit` run automatically on every pull request for the Course Management API codebase, catching style issues, unused variables, and basic security problems before a human reviewer even looks at the code.

(d) **API contract testing before integration** — Before the frontend team starts building the "Add Course" form, they agree on the exact request/response schema for `POST /api/courses/` (using something like an OpenAPI spec), and both sides write contract tests against that schema, catching mismatches before the two systems are ever integrated.

### 16. Acceptance Criteria in Given-When-Then format

**User Story:** As a college admin, I want to create a new course, so that students can enroll in it.

```gherkin
Scenario: Successfully create a new course (happy path)
  Given I am logged in as a college admin
  And no course with the code "CS101" exists
  When I submit a new course with code "CS101", name "Intro to CS", and 3 credits
  Then the course should be created successfully
  And I should see "CS101" in the course listing

Scenario: Attempt to create a course with a duplicate course code
  Given I am logged in as a college admin
  And a course with the code "CS101" already exists
  When I submit a new course with code "CS101"
  Then the system should reject the request
  And I should see an error message stating the course code already exists

Scenario: Attempt to create a course with missing required fields
  Given I am logged in as a college admin
  When I submit a new course without providing a course name
  Then the system should reject the request
  And I should see an error message indicating that the course name is required
```
