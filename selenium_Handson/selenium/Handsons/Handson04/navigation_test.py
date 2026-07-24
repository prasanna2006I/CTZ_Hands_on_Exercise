"""
navigation_test.py
Hands-On 4 - Task 2: WebDriver Navigation and Window Commands

Demonstrates:
  - navigating between pages and asserting the URL
  - going back in browser history
  - opening a new tab and switching between window handles
  - taking a screenshot
  - reading/setting the browser window size
"""

import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"
SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


def build_driver(headless: bool = True):
    """Create a configured Chrome WebDriver instance."""
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def run_navigation_demo():
    driver = build_driver(headless=True)

    try:
        # Step 28: open playground, click into Simple Form Demo, assert URL,
        # then navigate back.
        driver.get(PLAYGROUND_URL)
        simple_form_link = driver.find_element(By.LINK_TEXT, "Simple Form Demo")
        simple_form_link.click()

        assert "simple-form-demo" in driver.current_url, (
            "Expected 'simple-form-demo' in the URL after clicking the link"
        )
        print("Navigated to: " + driver.current_url)

        driver.back()
        print("Navigated back to: " + driver.current_url)

        # Step 29: open a second tab via JS, list window handles, switch to it.
        driver.execute_script('window.open("https://www.google.com");')
        all_tabs = driver.window_handles
        print("Open tabs: " + str(len(all_tabs)))

        driver.switch_to.window(all_tabs[1])
        print("Second tab title: " + driver.title)

        # Step 30: switch back to the original tab and take a screenshot.
        driver.switch_to.window(all_tabs[0])
        os.makedirs(SCREENSHOT_DIR, exist_ok=True)
        screenshot_path = os.path.join(SCREENSHOT_DIR, "playground_screenshot.png")
        driver.save_screenshot(screenshot_path)
        print("Screenshot saved at: " + screenshot_path)
        assert os.path.exists(screenshot_path), "Screenshot file was not created"

        # Step 31: window size handling.
        # Consistent window size matters because many pages use responsive
        # CSS breakpoints - the same page can show a completely different
        # layout (e.g. a hamburger menu instead of a full nav bar) at a
        # smaller width. If tests run with an inconsistent/random window
        # size, elements we expect to find (or expect to be clickable)
        # might not exist in that layout, causing flaky failures that have
        # nothing to do with an actual bug.
        current_size = driver.get_window_size()
        print("Current window size: " + str(current_size))

        driver.set_window_size(1280, 800)
        new_size = driver.get_window_size()
        print("Window resized to: " + str(new_size))

    finally:
        driver.quit()


if __name__ == "__main__":
    run_navigation_demo()
