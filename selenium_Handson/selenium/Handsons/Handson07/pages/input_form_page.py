"""
input_form_page.py
Hands-On 7 - Task 2, Step 57: InputFormPage.

Encapsulates all locators and interactions for the Input Form Submit
demo page, which has multiple fields (name, email, phone, address).
"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InputFormPage(BasePage):
    """Page Object for the Input Form Submit demo page."""

    INPUT_FORM_LINK = (By.LINK_TEXT, "Input Form Submit")

    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "inputEmail4")
    PHONE_FIELD = (By.NAME, "phone")
    ADDRESS_FIELD = (By.NAME, "address")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

    def open_from_home(self):
        """Click the 'Input Form Submit' link from the playground home page."""
        self.wait_for_clickable(self.INPUT_FORM_LINK).click()

    def fill_form(self, name, email, phone, address):
        """Fill in every field of the input form with the given values."""
        self.wait_for_element(self.NAME_FIELD).send_keys(name)
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def submit_form(self):
        """Click the form's Submit button."""
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        """Return the success message text shown after a valid submission."""
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
