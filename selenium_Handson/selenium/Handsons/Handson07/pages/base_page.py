"""
base_page.py
Hands-On 7 - Task 1, Step 50: BasePage - shared behaviour for every page object.

Every page-specific class (SimpleFormPage, CheckboxPage, DropdownPage,
InputFormPage) inherits from this class so navigation and waiting logic
is written once, not repeated in every page object.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Common functionality shared by all page objects."""

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        """Load the given URL in the browser."""
        self.driver.get(url)

    def get_title(self):
        """Return the current page's title."""
        return self.driver.title

    def wait_for_element(self, locator, timeout=10):
        """
        Wait until the element identified by `locator` (a (By, value) tuple)
        is visible, then return it. Centralising this here means every page
        object waits for elements the same, consistent way.
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        """Wait until the element identified by `locator` is clickable."""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
