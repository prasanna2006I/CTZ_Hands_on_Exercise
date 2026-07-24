"""
conftest.py
Hands-On 7 - shared pytest fixtures for the POM-based test suite.

Same driver/base_url/failure-screenshot setup as Hands-On 6, provided
again here so this folder's test suite (pytest tests/ -v) is fully
self-contained and runnable on its own.
"""

import os
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Allow "from pages.xxx import YYY" imports from the tests/ subfolder.
sys.path.insert(0, os.path.dirname(__file__))

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the LambdaTest Selenium Playground, shared by all tests."""
    return "https://www.lambdatest.com/selenium-playground/"


@pytest.fixture(scope="function")
def driver():
    """Function-scoped driver fixture - a fresh Chrome instance per test."""
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")

    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=options)

    yield chrome_driver

    chrome_driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Save a screenshot automatically whenever a test using `driver` fails."""
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
