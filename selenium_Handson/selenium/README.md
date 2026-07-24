# Selenium Basics — QA Concepts & Test Automation

**Digital Nurture 5.0 — Python Full Stack Engineer Track**

A complete solution set for the 7-part "QA Concepts & Selenium Basics"
hands-on exercise book: three written QA-theory exercises followed by
four coding exercises that build up a real Selenium + pytest + Page
Object Model test suite against the [LambdaTest Selenium
Playground](https://www.lambdatest.com/selenium-playground/).

## Project Overview

| Hands-On | Topic | Level | Type |
|---|---|---|---|
| 1 | QA Concepts, Functional Testing & Defect Lifecycle | Beginner | Written |
| 2 | SDLC vs TDLC — V-Model & Agile QA Integration | Beginner | Written |
| 3 | Test Automation Process, Lifecycle & Framework Types | Intermediate | Written |
| 4 | Selenium WebDriver Setup, Browser Drivers & Basic Commands | Intermediate | Code |
| 5 | Locators & Explicit/Fluent Waits | Intermediate | Code |
| 6 | Running Selenium Tests with pytest (fixtures, parametrize, HTML reports) | Advanced | Code |
| 7 | Page Object Model (POM) | Advanced | Code |

The four coding hands-ons build progressively: Hands-On 4 writes plain
WebDriver scripts, Hands-On 5 adds robust locators and explicit waits,
Hands-On 6 wraps everything in a pytest suite with fixtures and
reporting, and Hands-On 7 refactors the whole suite into a clean Page
Object Model with zero `driver.find_element` calls left in any test
file.

## Folder Structure

```
selenium_Handson/
│
├── README.md
├── requirements.txt
├── .gitignore
│
└── Handsons/
    │
    ├── Handson01/
    │   ├── qa_concepts.md
    │   └── README.md
    │
    ├── Handson02/
    │   ├── v_model_analysis.md
    │   └── README.md
    │
    ├── Handson03/
    │   ├── automation_strategy.md
    │   └── README.md
    │
    ├── Handson04/
    │   ├── setup_test.py
    │   ├── navigation_test.py
    │   └── README.md
    │
    ├── Handson05/
    │   ├── locator_demo.py
    │   ├── waits_demo.py
    │   └── README.md
    │
    ├── Handson06/
    │   ├── conftest.py
    │   ├── test_playground.py
    │   └── README.md
    │
    └── Handson07/
        ├── conftest.py
        ├── pages/
        │   ├── base_page.py
        │   ├── simple_form_page.py
        │   ├── checkbox_page.py
        │   ├── dropdown_page.py
        │   └── input_form_page.py
        ├── tests/
        │   ├── test_simple_form.py
        │   ├── test_checkbox.py
        │   ├── test_dropdown.py
        │   └── test_input_form.py
        └── README.md
```

Each `Handson0N/` folder is self-contained with its own `README.md`
explaining what's inside and how to run it.

## Technologies Used

- **Python 3.10+**
- **Selenium WebDriver 4.x** — browser automation
- **pytest** — test runner, fixtures, parameterisation
- **pytest-html** — self-contained HTML test reports
- **webdriver-manager** — automatic ChromeDriver version management
- **Google Chrome** (headless by default in every script/test)

## Installation

1. Install Python 3.10 or newer.
2. Clone this repository and move into it:
   ```bash
   git clone <your-repo-url>
   cd selenium_Handson
   ```
3. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate      # on Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Google Chrome must be installed on the machine; `webdriver-manager`
takes care of downloading a matching ChromeDriver binary automatically
the first time a script or test runs.

## Requirements

See `requirements.txt`:

```
selenium
pytest
pytest-html
webdriver-manager
```

## Running the Hands-Ons

**Hands-On 1–3** are written exercises — just open the `.md` files in
each folder.

**Hands-On 4–5** are standalone scripts:

```bash
python Handsons/Handson04/setup_test.py
python Handsons/Handson04/navigation_test.py
python Handsons/Handson05/locator_demo.py
python Handsons/Handson05/waits_demo.py
```

**Hands-On 6** is a pytest suite:

```bash
cd Handsons/Handson06
pytest test_playground.py -v
```

**Hands-On 7** is the full POM-based pytest suite:

```bash
cd Handsons/Handson07
pytest tests/ -v
```

## Generating an HTML Report

Run either pytest suite with the `--html` flag from inside its own
folder:

```bash
pytest test_playground.py -v --html=../../reports/report.html --self-contained-html
```

or, from Hands-On 7:

```bash
pytest tests/ -v --html=../../reports/report.html --self-contained-html
```

Open the generated `reports/report.html` in any browser to see test
names, pass/fail status, and duration for every test.

## Screenshots

- `Handsons/Handson04/screenshots/` — saved by `navigation_test.py`.
- `Handsons/Handson06/screenshots/` and `Handsons/Handson07/screenshots/`
  — saved automatically only when a test fails, via a
  `pytest_runtest_makereport` hook in each folder's `conftest.py`.

## Future Enhancements

- Add Selenium Grid configuration for cross-browser, parallel execution.
- Add a GitHub Actions workflow to run the full suite headlessly on
  every push.
- Extend the Data-Driven approach from Hands-On 3's strategy doc into
  Hands-On 6/7 by reading form input values from an external CSV file.
- Add the Bootstrap Alerts and Table Sort scenarios as further POM
  page objects and tests.

## Author

Digital Nurture 5.0 — Python Full Stack Engineer Track participant.

---

This project is GitHub-ready: compress this folder (or push it
directly) to share with your POC as required by the submission
guidelines.
