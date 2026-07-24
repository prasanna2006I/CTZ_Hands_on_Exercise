"""
dropdown_page.py
Hands-On 7 - Task 1, Step 54: DropdownPage.

Encapsulates all locators and interactions for the Select Dropdown List
demo page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    """Page Object for the Select Dropdown List demo page."""

    DROPDOWN_DEMO_LINK = (By.LINK_TEXT, "Select Dropdown List")
    DAY_DROPDOWN = (By.ID, "select-demo")

    def open_from_home(self):
        """Click the 'Select Dropdown List' link from the playground home page."""
        self.wait_for_clickable(self.DROPDOWN_DEMO_LINK).click()

    def select_day(self, day_name):
        """Select a day of the week from the dropdown using its visible text."""
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        Select(dropdown_element).select_by_visible_text(day_name)

    def get_selected_day(self):
        """Return the currently selected option's visible text."""
        dropdown_element = self.wait_for_element(self.DAY_DROPDOWN)
        return Select(dropdown_element).first_selected_option.text
