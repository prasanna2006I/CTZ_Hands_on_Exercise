"""
test_dropdown.py
Hands-On 7 - Task 2, Step 56: refactored to use DropdownPage.
"""

from pages.dropdown_page import DropdownPage


def test_dropdown_selection(driver, base_url):
    page = DropdownPage(driver)
    page.navigate_to(base_url)
    page.open_from_home()

    page.select_day("Wednesday")

    assert page.get_selected_day() == "Wednesday"
