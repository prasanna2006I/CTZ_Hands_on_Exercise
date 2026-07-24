"""
conftest.py
Hands-On 6 - shared pytest fixtures for the playground test suite.

Provides:
  - `driver` fixture (function scope): a fresh Chrome WebDriver per test,
    torn down automatically after each test.
  - `base_url` fixture (session scope): the playground base URL, shared
    read-only across the whole test session.
  - a pytest_runtest_makereport hook that captures a screenshot whenever
    a test using the `driver` fixture fails.
"""

import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the LambdaTest Selenium Playground, shared by all tests."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver():
    """
    Function-scoped driver fixture: a brand new Chrome instance is created
    for every single test function, and quit right after it finishes.

    scope='function' means each test gets full isolation (no leftover
    cookies/state from a previous test) at the cost of a slightly slower
    suite, since Chrome starts fresh each time. scope='session' would
    reuse one browser for the whole run - faster, but tests could then
    leak state into each other.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)

    yield chrome_driver  # --- setup is everything above this line ---

    chrome_driver.quit()  # --- teardown: runs after the test completes ---


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Screenshot-on-failure hook.

    pytest calls this hook after every phase of a test (setup, call,
    teardown). We only care about the "call" phase (the actual test body)
    failing. When it does, and the test used the `driver` fixture, we
    grab a screenshot so the failure is easier to diagnose later without
    needing to reproduce it manually.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture is not None:
            os.makedirs(SCREENSHOT_DIR, exist_ok=True)
            safe_name = item.name.replace("[", "_").replace("]", "_")
            screenshot_path = os.path.join(
                SCREENSHOT_DIR, "{}_failure.png".format(safe_name)
            )
            driver_fixture.save_screenshot(screenshot_path)
            print("\nFailure screenshot saved to: " + screenshot_path)
