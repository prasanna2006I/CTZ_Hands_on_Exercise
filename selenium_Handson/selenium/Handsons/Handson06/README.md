# Hands-On 6 — Running Selenium Tests with pytest

**Level:** Advanced
**Type:** Coding exercise

## What's in this folder

- `conftest.py` — the `driver` fixture (function-scoped, yields a fresh Chrome instance per test and quits it afterwards), the `base_url` fixture (session-scoped), and a `pytest_runtest_makereport` hook that saves a screenshot automatically whenever a test fails.
- `test_playground.py` — `test_simple_form_submission` (parameterised with 3 messages via `@pytest.mark.parametrize`), `test_checkbox_demo`, and `test_dropdown_selection`.
- `screenshots/` — created automatically on the first test failure.

## How to run

```bash
cd Handsons/Handson06
pytest test_playground.py -v
```

To generate an HTML report:

```bash
pytest test_playground.py -v --html=../../reports/report.html --self-contained-html
```

This produces 5 test runs in total (3 parameterised form-submission tests + checkbox + dropdown), each shown individually in the report with pass/fail status and duration.
