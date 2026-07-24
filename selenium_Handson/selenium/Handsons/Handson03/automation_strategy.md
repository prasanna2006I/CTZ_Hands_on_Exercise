# Hands-On 3: Test Automation Process, Lifecycle & Framework Types

## Task 1: Automation Decision and Test Case Selection

### 17. Five criteria for deciding whether to automate a test case

1. **Repeatability** — will this test be run many times (e.g. every build, every regression cycle)? Applied to our scenario: the "POST /api/courses/ returns 201 with correct data" test will run on every single deployment as part of regression, so it's an excellent automation candidate.
2. **Stability of the feature** — is the feature's behaviour and UI/API contract unlikely to change frequently? Applied to our scenario: course creation is a core, stable feature of the system, not something being redesigned every sprint, so automating it won't mean constant rework.
3. **High business risk if broken** — would a failure here cause serious damage (data loss, revenue loss, compliance issue)? Applied to our scenario: if course creation silently breaks, no new courses can be added — a high-risk failure, which justifies the investment in automation.
4. **Objective, verifiable outcome** — can the pass/fail result be checked programmatically without human judgment? Applied to our scenario: checking the response status is 201 and the returned JSON matches the input is a purely objective, machine-checkable outcome.
5. **Time savings over manual execution** — will automating save more time across its lifetime than it costs to build and maintain? Applied to our scenario: manually testing this via Postman takes about 2 minutes each time; across hundreds of future regression runs, automating it clearly pays off.

### 18. Automate or Manual — with justification

| # | Test Case | Decision | Justification |
|---|---|---|---|
| a | Regression test for all CRUD endpoints after every code change | Automate | Runs repeatedly on every change, has objective pass/fail criteria — a textbook automation candidate. |
| b | Exploratory testing of a new search feature | Manual | Exploratory testing relies on human intuition and creativity to find unexpected issues; it has no fixed script to automate. |
| c | Performance test: 100 concurrent users on GET /api/courses/ | Automate | Requires precise, repeatable load generation and timing measurement that a human cannot do manually — needs a tool like Locust or JMeter. |
| d | UI test for the login form | Automate | Login is executed constantly across every other automated UI test as a prerequisite, so it's worth automating once and reusing everywhere. |
| e | Verify the API documentation (Swagger) is accurate | Manual | This requires human judgment to compare written descriptions against actual behaviour and readability — not easily reduced to a pass/fail script. |
| f | Smoke test: verify the API is reachable after deployment | Automate | Simple, repeatable, needs to run automatically right after every deployment, and is fast to write and maintain. |

### 19. Automation ROI calculation

- Manual execution time: 30 minutes per run
- Automation build time: 4 hours = 240 minutes (one-time cost)
- Maintenance overhead: 20% extra time added to each run *after* the 10th run

**Runs 1–10** (no maintenance overhead yet): each automated run "costs" effectively 0 extra minutes to execute (assume near-instant compared to manual), so the time saved per run vs manual is roughly 30 minutes.

Time saved after 10 runs = 10 × 30 minutes = 300 minutes, which already exceeds the 240-minute build cost. So the automation **pays for itself within the first 8 runs**, calculated as:

240 minutes (build cost) ÷ 30 minutes saved per run ≈ **8 runs**

After the 10th run, a 20% maintenance overhead applies to each run, meaning each subsequent automated run effectively "costs" a small amount of maintenance time, but since that overhead (a few minutes) is still far less than the 30 minutes a manual run would take, the automation continues to save time on every run after that — it simply pays for itself slightly slower than the initial estimate once maintenance is accounted for, but the breakeven point remains at roughly **8 runs**, well before maintenance overhead even kicks in at run 10.

### 20. Flaky Tests

**Definition:** A flaky test is a test that sometimes passes and sometimes fails *without any change to the code being tested* — the failure is caused by the test itself (timing, environment, or test design issues), not by a real defect.

**Example:** A Selenium test clicks a "Submit" button immediately after the page loads, but the button is rendered by JavaScript slightly after the initial page load. On a fast machine/network the click works; on a slower run, the element isn't ready yet and the test fails with a "no such element" or "element not clickable" error — even though the application itself works fine.

**Three strategies to prevent or fix flaky tests:**
1. Replace fixed `time.sleep()` calls with **explicit waits** (`WebDriverWait` + `ExpectedConditions`) so the test waits exactly as long as needed, no more, no less.
2. **Isolate test data** — use unique, per-test data (e.g. a randomly generated course code) rather than shared/static test data that could be mutated by other tests running in parallel.
3. **Retry with root-cause investigation** — a very limited automatic retry (e.g. once) can absorb rare environment blips, but the real flaky cause should always be investigated and fixed rather than relying on retries as a permanent solution, since masking flakiness erodes trust in the whole suite.

---

## Task 2: Compare Automation Framework Types

### 21. Comparison of the 5 framework types

**Linear (Record & Playback)**
- Description: Each test is a standalone script that records a straight-line sequence of steps against the application, with no reusable functions or structure.
- Advantage: Very fast to create — good for quick, one-off checks.
- Disadvantage: Massive duplication; if a locator changes, every script that uses it must be updated individually.
- Example use: A one-time smoke check that the Course Management admin login page loads, done once and discarded.

**Modular**
- Description: Breaks the application into logical modules (e.g. login, course creation, enrollment), with reusable functions for each module that tests can call.
- Advantage: Reduces duplication — common actions like "login" are written once and reused everywhere.
- Disadvantage: Still requires programming knowledge to write and modify test scripts; test data is often still hardcoded inside the scripts.
- Example use: A `login()` function used by every test in the Course Management suite that requires an authenticated admin.

**Data-Driven**
- Description: Separates test data from test logic — the same test script runs multiple times with different sets of input data pulled from an external source (CSV, JSON, Excel).
- Advantage: Easily test many input combinations (e.g. 50 different course names) without writing 50 separate scripts.
- Disadvantage: Requires extra setup to manage and maintain external data files, and the test logic itself can become harder to follow when heavily parameterised.
- Example use: Testing course creation with 20 different combinations of valid/invalid course codes and credit values pulled from a CSV file.

**Keyword-Driven**
- Description: Test steps are represented as keywords (e.g. "ClickButton", "EnterText") in a table (often a spreadsheet), interpreted by a driver engine — designed so non-programmers can write tests.
- Advantage: Non-technical team members (e.g. manual testers, business analysts) can create and modify tests without writing code.
- Disadvantage: Significant upfront investment to build the keyword engine/framework itself, and debugging failures can be harder since the keyword layer hides the underlying code.
- Example use: A business analyst defines a new test for the "Enroll Student" flow purely using keywords in a spreadsheet, without touching Python code.

**Hybrid**
- Description: Combines Modular, Data-Driven, and often Keyword-Driven elements into one framework — reusable functions, external test data, and sometimes a keyword layer, all together.
- Advantage: Gets the best of all worlds — reusability, data separation, and (optionally) accessibility for non-programmers.
- Disadvantage: More complex to design and set up initially; requires more upfront framework architecture decisions.
- Example use: The full Course Management Selenium suite — reusable Page Object methods (Modular) + CSV-driven test data for course creation (Data-Driven) all wired together.

### 22. Recommended framework for the given scenario

**Scenario:** Test login with 50 different user/password combinations, reuse login steps across 20 test cases, and support both technical and non-technical team members writing tests.

**Recommendation: Hybrid framework** (Modular + Data-Driven, with an optional lightweight Keyword layer).

Justification: The requirement to reuse login steps across 20 test cases points directly at the **Modular** approach (a single reusable `login()` method). The requirement to test 50 different credential combinations points directly at **Data-Driven** testing (parameterised tests reading from an external data source). The requirement for non-technical team members to also write tests suggests adding a thin **Keyword-Driven** layer on top so that testers who don't code can still define new login scenarios. Combining all three into a Hybrid framework satisfies every requirement in the scenario at once, rather than forcing a compromise with a single framework type.

### 23. Hybrid folder structure for the Course Management frontend tests

```
CourseManagementTests/
│
├── config/
│   └── config.yaml              # base URL, browser choice, timeouts
│
├── test_data/
│   ├── login_credentials.csv    # 50 username/password combinations
│   └── course_data.json         # sample course payloads for data-driven tests
│
├── pages/
│   ├── login_page.py            # Page Object for the login screen
│   ├── course_page.py           # Page Object for course creation
│   └── base_page.py             # shared Page Object methods
│
├── utils/
│   ├── data_reader.py           # loads CSV/JSON test data
│   └── driver_factory.py        # creates and configures the WebDriver
│
├── tests/
│   ├── test_login.py            # data-driven login tests, reusing login_page
│   └── test_course_creation.py  # course creation tests
│
├── keywords/                    # optional keyword layer for non-technical testers
│   └── keyword_engine.py
│
├── reports/
│   └── report.html
│
└── conftest.py                  # shared pytest fixtures (driver setup/teardown)
```
