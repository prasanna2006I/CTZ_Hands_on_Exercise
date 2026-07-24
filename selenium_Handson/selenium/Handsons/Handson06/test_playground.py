"""
test_playground.py
Hands-On 6 - pytest test suite for the LambdaTest Selenium Playground.

Covers:
  - parameterised Simple Form Demo submissions (Step 40, 42, 45)
  - Checkbox Demo select/deselect (Step 43)
  - Select Dropdown List selection (Step 49)

All tests receive the `driver` and `base_url` fixtures from conftest.py
via dependency injection - no test creates its own driver instance.

Run with:  pytest test_playground.py -v --html=../../reports/report.html --self-contained-html
"""

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


# Step 45: parameterise the form submission test with 3 different values.
@pytest.mark.parametrize("message", ["Hello", "Selenium Automation", "12345"])
def test_simple_form_submission(driver, base_url, message):
    """Enter a message, submit the form, and assert it is echoed back."""
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

    message_input = driver.find_element(By.ID, "user-message")
    message_input.send_keys(message)
    driver.find_element(By.CSS_SELECTOR, "#single-input button").click()

    displayed_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "message"))
    )

    assert displayed_message.text == message, (
        "Expected displayed message to equal '{}', got '{}'".format(
            message, displayed_message.text
        )
    )


def test_checkbox_demo(driver, base_url):
    """Check the first checkbox, verify it's selected, uncheck, verify deselected."""
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

    first_checkbox = driver.find_element(By.CSS_SELECTOR, "#colorbox li:nth-child(1) input")

    first_checkbox.click()
    assert first_checkbox.is_selected(), "Checkbox should be selected after first click"

    first_checkbox.click()
    assert not first_checkbox.is_selected(), "Checkbox should be deselected after second click"


def test_dropdown_selection(driver, base_url):
    """Select 'Wednesday' from the Select Dropdown List demo and verify it."""
    driver.get(base_url)
    driver.find_element(By.LINK_TEXT, "Select Dropdown List").click()

    dropdown_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "select-demo"))
    )
    select = Select(dropdown_element)
    select.select_by_visible_text("Wednesday")

    selected_option = select.first_selected_option
    assert selected_option.text == "Wednesday", (
        "Expected 'Wednesday' to be selected, got '{}'".format(selected_option.text)
    )
