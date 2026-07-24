"""
waits_demo.py
Hands-On 5 - Task 2: WebDriverWait and Expected Conditions

Demonstrates replacing time.sleep() with explicit waits, waiting for
clickability, and using a FluentWait-style poll for a dynamically
loaded element.
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def build_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def demo_explicit_wait_on_alert():
    """
    Step 36: click the 'Success Message' button on the Bootstrap Alerts
    demo, wait for the success alert to become visible, and assert its
    text contains 'successfully'.
    """
    driver = build_driver()
    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

        success_button = driver.find_element(By.ID, "successAlertButton")
        success_button.click()

        # Explicit wait: poll until the success alert div is visible,
        # rather than guessing a fixed sleep duration.
        alert = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        assert "successfully" in alert.text.lower(), (
            "Expected the alert text to mention 'successfully'"
        )
        print("Alert text:", alert.text)
    finally:
        driver.quit()


def demo_sleep_vs_explicit_wait():
    """
    Step 37: compare a hard-coded sleep against an explicit wait for the
    same action, and time both approaches.

    Why time.sleep(3) is bad:
      - It ALWAYS waits the full 3 seconds, even if the element was ready
        in 200ms - wasting time across hundreds of test runs.
      - If the machine or network is slower than usual, 3 seconds might
        not be enough, and the test fails anyway - it does not adapt.
      - An explicit wait polls repeatedly and returns the instant the
        condition is met, so it is BOTH faster on fast machines AND more
        reliable on slow ones, unlike a fixed sleep which is neither.
    """
    driver = build_driver()
    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

        # --- Version A: hard-coded sleep (bad practice) ---
        start = time.time()
        driver.find_element(By.ID, "successAlertButton").click()
        time.sleep(3)  # blindly waits 3 full seconds regardless of reality
        driver.find_element(By.CSS_SELECTOR, ".alert-success")
        sleep_duration = time.time() - start
        print("Duration using time.sleep(3): {:.2f}s".format(sleep_duration))

        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

        # --- Version B: explicit wait (good practice) ---
        start = time.time()
        driver.find_element(By.ID, "successAlertButton").click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        )
        wait_duration = time.time() - start
        print("Duration using explicit wait: {:.2f}s".format(wait_duration))

        print(
            "Explicit wait finished as soon as the element appeared, "
            "instead of always burning the full fixed delay."
        )
    finally:
        driver.quit()


def demo_element_to_be_clickable():
    """
    Step 38: wait for an element to be clickable before clicking it.

    Difference between the two Expected Conditions:
      - visibility_of_element_located: the element exists in the DOM AND
        has a height/width greater than 0 (i.e. you could see it), but
        says nothing about whether it can currently be interacted with.
      - element_to_be_clickable: everything visibility_of_element_located
        checks, PLUS the element is enabled (not disabled) AND is not
        currently obscured by another element on top of it (e.g. a
        loading spinner or modal overlay). This is the safer condition
        to wait for immediately before performing a .click().
    """
    driver = build_driver()
    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Bootstrap Alerts").click()

        success_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "successAlertButton"))
        )
        success_button.click()
        print("Clicked the success button only after it was confirmed clickable.")
    finally:
        driver.quit()


def demo_fluent_wait():
    """
    Step 39: FluentWait-style polling - poll every 500ms for up to 10
    seconds, ignoring NoSuchElementException while polling, applied to a
    dynamically-loaded table row on the Table Sort demo page.
    """
    driver = build_driver()
    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Table Sort").click()

        fluent_wait = WebDriverWait(
            driver,
            timeout=10,
            poll_frequency=0.5,
            ignored_exceptions=(NoSuchElementException,),
        )

        first_row = fluent_wait.until(
            lambda d: d.find_element(By.CSS_SELECTOR, "table tbody tr")
        )
        print("First table row loaded:", first_row.text)
    finally:
        driver.quit()


if __name__ == "__main__":
    demo_explicit_wait_on_alert()
    demo_sleep_vs_explicit_wait()
    demo_element_to_be_clickable()
    demo_fluent_wait()
