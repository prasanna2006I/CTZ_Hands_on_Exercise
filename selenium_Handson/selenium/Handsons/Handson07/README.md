# Hands-On 7 — Page Object Model (POM)

**Level:** Advanced
**Type:** Coding exercise

## What's in this folder

```
Handson07/
├── conftest.py                 # driver & base_url fixtures, failure screenshot hook
├── pages/
│   ├── base_page.py            # BasePage: navigate_to, get_title, wait_for_element
│   ├── simple_form_page.py     # SimpleFormPage
│   ├── checkbox_page.py        # CheckboxPage
│   ├── dropdown_page.py        # DropdownPage
│   └── input_form_page.py      # InputFormPage
├── tests/
│   ├── test_simple_form.py
│   ├── test_checkbox.py
│   ├── test_dropdown.py
│   └── test_input_form.py
└── screenshots/                # created automatically on test failure
```

Every locator lives as a class-level tuple inside its page class. Page
methods only perform actions and return values — they never contain
`assert` statements. Test files only call page methods and make
assertions — **zero `driver.find_element` calls appear in any test
file** (verified with `grep -r "find_element" tests/`, which returns
nothing).

## How to run

```bash
cd Handsons/Handson07
pytest tests/ -v --html=../../reports/report.html --self-contained-html
```

## Step 59 — Why POM matters: the Submit button ID example

Imagine the Submit button's `id` changes from `submit` to `btn-submit`
on the real site.

**In a flat (non-POM) script:** the locator `By.ID, "submit"` would be
typed directly inside every test function that clicks Submit. If 10
different test files each click Submit, you would have to find and fix
that locator in 10 separate places. Miss even one, and that test starts
failing for a reason that has nothing to do with an actual application
bug — just a stale locator.

**With POM:** the locator lives in exactly one place —
`SimpleFormPage.SUBMIT_BUTTON` (or `InputFormPage.SUBMIT_BUTTON`). When
the ID changes, you update that single class-level tuple once, and
every test that calls `page.click_submit()` or `page.submit_form()`
automatically picks up the fix — no test file needs to change at all.
This is exactly why locators as class-level constants are the core
benefit of the Page Object Model: one change in one file, instead of
hunting through the whole suite.
