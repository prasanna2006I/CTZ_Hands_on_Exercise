"""
checkbox_page.py
Hands-On 7 - Task 1, Step 53: CheckboxPage.

Encapsulates all locators and interactions for the Checkbox Demo page.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxPage(BasePage):
    """Page Object for the Checkbox Demo page."""

    CHECKBOX_DEMO_LINK = (By.LINK_TEXT, "Checkbox Demo")
    # Checkbox options are numbered list items inside #colorbox; index is
    # 1-based to match how a human would refer to "the first option".
    OPTION_TEMPLATE = "#colorbox li:nth-child({}) input"

    def open_from_home(self):
        """Click the 'Checkbox Demo' link from the playground home page."""
        self.wait_for_clickable(self.CHECKBOX_DEMO_LINK).click()

    def _option_locator(self, index):
        return (By.CSS_SELECTOR, self.OPTION_TEMPLATE.format(index))

    def check_option(self, index):
        """Click the checkbox at 1-based position `index` to select it."""
        checkbox = self.wait_for_element(self._option_locator(index))
        if not checkbox.is_selected():
            checkbox.click()

    def uncheck_option(self, index):
        """Click the checkbox at 1-based position `index` to deselect it."""
        checkbox = self.wait_for_element(self._option_locator(index))
        if checkbox.is_selected():
            checkbox.click()

    def is_option_checked(self, index):
        """Return True if the checkbox at 1-based position `index` is selected."""
        checkbox = self.wait_for_element(self._option_locator(index))
        return checkbox.is_selected()
