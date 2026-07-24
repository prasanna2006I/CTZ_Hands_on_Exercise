"""
test_checkbox.py
Hands-On 7 - Task 2, Step 56: refactored to use CheckboxPage.
"""

from pages.checkbox_page import CheckboxPage


def test_checkbox_demo(driver, base_url):
    page = CheckboxPage(driver)
    page.navigate_to(base_url)
    page.open_from_home()

    page.check_option(1)
    assert page.is_option_checked(1) is True

    page.uncheck_option(1)
    assert page.is_option_checked(1) is False
