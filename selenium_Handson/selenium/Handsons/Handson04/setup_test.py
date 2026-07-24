"""
setup_test.py
Hands-On 4 - Task 1: Selenium Architecture and Environment Setup

Selenium Architecture (three main components):

1. WebDriver
   WebDriver is the core API that talks directly to the browser through
   its native automation interface (e.g. Chrome talks via the DevTools
   Protocol / W3C WebDriver protocol). When we call driver.get(url) or
   element.click(), WebDriver sends a request to a small program called
   the "browser driver" (ChromeDriver for Chrome), which translates that
   request into real browser actions. This is why we need a matching
   ChromeDriver binary for the Chrome version installed on the machine.

2. Selenium Grid
   Selenium Grid solves the problem of running tests in parallel across
   multiple machines and/or multiple browsers at the same time. Instead
   of running 100 tests one after another on a single Chrome instance
   (slow), Grid lets us distribute those tests across many "nodes" -
   different machines, different browsers, different OS versions - all
   running at once, which massively cuts down total execution time for
   large test suites.

3. Selenium IDE
   Selenium IDE is a browser extension that lets you record your clicks
   and typing on a web page and automatically turns them into a
   reusable script (record-and-playback). It also supports exporting
   the recorded actions into real code (e.g. Python + Selenium
   WebDriver format), which is a fast way to bootstrap a first draft of
   a script before cleaning it up by hand.

This script:
  - imports Chrome WebDriver using webdriver-manager
  - opens Chrome
  - navigates to the LambdaTest Selenium Playground
  - prints the page title
  - closes the browser
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def run_basic_setup(headless: bool = False):
    """Open the playground, print its title, then close the browser."""
    options = Options()

    if headless:
        # --headless=new runs Chrome without a visible window, while
        # still behaving like a real browser for JS-heavy pages.
        options.add_argument("--headless=new")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # webdriver-manager downloads/updates the correct chromedriver
    # binary automatically, matching the locally installed Chrome
    # version, so we never have to manage driver binaries by hand.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Step 26: implicit wait tells the driver to poll the DOM for
        # up to 10 seconds whenever an element is not immediately
        # found, for EVERY find_element call for the lifetime of the
        # driver.
        driver.implicitly_wait(10)

        # WHY IMPLICIT WAIT IS CONSIDERED BAD PRACTICE vs EXPLICIT WAIT:
        # An implicit wait applies globally and blindly to every single
        # locator call, even when we actually want to assert that an
        # element is ABSENT (in which case we're stuck waiting the full
        # timeout unnecessarily). It also cannot express conditions
        # like "wait until clickable" or "wait until text changes" -
        # it only waits for presence in the DOM. Mixing implicit and
        # explicit waits in the same test can also cause unpredictable
        # total wait times. Explicit waits (WebDriverWait +
        # ExpectedConditions), covered in Hands-On 5, let us wait for
        # the *exact* condition each step actually needs, per element,
        # which is far more precise and reliable.

        driver.get(PLAYGROUND_URL)
        print("Page title: " + driver.title)
        return driver.title
    finally:
        driver.quit()


if __name__ == "__main__":
    # Step 27: running in headless mode - the title should still print
    # correctly even with no visible browser window.
    run_basic_setup(headless=True)
