"""
simple_form_page.py
Hands-On 7 - Task 1, Steps 51-52: SimpleFormPage.

Encapsulates every locator and interaction for the Simple Form Demo page.
Page methods only perform actions and return values - they never contain
assert statements. Assertions belong in the test files.
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SimpleFormPage(BasePage):
    """Page Object for the Simple Form Demo page."""

    # Locators are defined once as class-level tuples. If the site's HTML
    # ever changes, only these lines need to be updated - not every test
    # that uses this page.
    MESSAGE_INPUT = (By.ID, "user-message")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#single-input button")
    DISPLAYED_MESSAGE = (By.ID, "message")
    SIMPLE_FORM_LINK = (By.LINK_TEXT, "Simple Form Demo")

    def open_from_home(self):
        """Click the 'Simple Form Demo' link from the playground home page."""
        self.wait_for_clickable(self.SIMPLE_FORM_LINK).click()

    def enter_message(self, text):
        """Type `text` into the message input field."""
        message_box = self.wait_for_element(self.MESSAGE_INPUT)
        message_box.clear()
        message_box.send_keys(text)

    def click_submit(self):
        """Click the Submit button."""
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_displayed_message(self):
        """Return the text of the message echoed back after submission."""
        return self.wait_for_element(self.DISPLAYED_MESSAGE).text
