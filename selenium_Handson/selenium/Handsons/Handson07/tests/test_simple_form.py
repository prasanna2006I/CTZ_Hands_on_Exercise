"""
test_simple_form.py
Hands-On 7 - Task 2, Step 55: refactored to use SimpleFormPage.

Notice this file contains ZERO driver.find_element calls and ZERO
locators - it only calls Page Object methods and makes assertions.
That is the golden rule of POM: test files decide WHAT should happen,
page files decide HOW to make it happen.
"""

from pages.simple_form_page import SimpleFormPage


def test_simple_form_submission(driver, base_url):
    page = SimpleFormPage(driver)
    page.navigate_to(base_url)
    page.open_from_home()

    page.enter_message("Hello Selenium")
    page.click_submit()

    assert page.get_displayed_message() == "Hello Selenium"
