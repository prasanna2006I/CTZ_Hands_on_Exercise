"""
locator_demo.py
Hands-On 5 - Task 1: Locator Strategies - From Simple to Robust

Target page: Simple Form Demo on the LambdaTest Selenium Playground.
The page has a text input where the user types a message, and after
clicking Submit, the message is echoed back on the page. The input
field itself has id="user-message" and name="message" in the site's
HTML, which is what the locators below target.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

PLAYGROUND_URL = "https://www.lambdatest.com/selenium-playground/"


def build_driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def demonstrate_locators():
    driver = build_driver()

    try:
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Simple Form Demo").click()

        # Step 32: locate the message input field using every basic strategy.

        # By ID - the most preferred strategy: fast, unique, and readable.
        by_id = driver.find_element(By.ID, "user-message")

        # By NAME - also reliable when the "name" attribute is unique on
        # the page, common for form fields.
        by_name = driver.find_element(By.NAME, "message")

        # By CLASS_NAME - works only if the class value is a single,
        # sufficiently unique class on the page (Selenium rejects
        # multi-class strings passed here).
        by_class = driver.find_element(By.CLASS_NAME, "form-control")

        # By TAG_NAME - finds the first <input> tag; too broad to be
        # reliable on its own for a page with multiple inputs, shown
        # here mainly for completeness.
        by_tag = driver.find_element(By.TAG_NAME, "input")

        # By XPATH (absolute path) - brittle: breaks the moment the page
        # structure changes even slightly. Shown here only to
        # demonstrate why it should be avoided.
        by_xpath_absolute = driver.find_element(
            By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]/form/div/input"
        )

        # By XPATH (relative, attribute-based) - far more robust than an
        # absolute path because it targets the element by its own
        # attribute, wherever it lives in the DOM tree.
        by_xpath_relative = driver.find_element(
            By.XPATH, "//input[@id='user-message']"
        )

        print("Located by ID:", by_id.get_attribute("id"))
        print("Located by NAME:", by_name.get_attribute("name"))
        print("Located by CLASS_NAME:", by_class.get_attribute("class"))
        print("Located by TAG_NAME:", by_tag.tag_name)
        print("Located by absolute XPATH:", by_xpath_absolute.get_attribute("id"))
        print("Located by relative XPATH:", by_xpath_relative.get_attribute("id"))

        # Step 33: three different CSS selectors for the same element.
        css_by_id = driver.find_element(By.CSS_SELECTOR, "#user-message")
        css_by_attribute = driver.find_element(
            By.CSS_SELECTOR, "[name='message']"
        )
        css_by_parent_child = driver.find_element(
            By.CSS_SELECTOR, "div.form-group > input#user-message"
        )

        print("CSS by ID:", css_by_id.get_attribute("id"))
        print("CSS by attribute:", css_by_attribute.get_attribute("id"))
        print("CSS by parent > child:", css_by_parent_child.get_attribute("id"))

        # Step 34: Checkbox Demo - XPath with text() and contains().
        driver.get(PLAYGROUND_URL)
        driver.find_element(By.LINK_TEXT, "Checkbox Demo").click()

        first_option_label = driver.find_element(
            By.XPATH, "//label[text()='Option 1']"
        )
        print("First checkbox label (exact text):", first_option_label.text)

        all_option_labels = driver.find_elements(
            By.XPATH, "//label[contains(text(),'Option')]"
        )
        print("All checkbox option labels found:", len(all_option_labels))
        for label in all_option_labels:
            print(" -", label.text)

    finally:
        driver.quit()


# Step 35: Ranking of the 6 locator strategies from MOST to LEAST preferred
# for maintainable automation, with justification.
#
# 1. ID              - Unique by HTML spec (should never repeat on a page),
#                       fastest lookup, and reads clearly in code. This is
#                       the gold standard whenever the element has one.
# 2. CSS_SELECTOR     - Almost as fast as ID, supports rich attribute and
#                       structural matching, and is generally less verbose
#                       and more readable than the equivalent XPath.
# 3. NAME              - Reliable for form fields specifically (inputs,
#                       selects), though "name" is less consistently
#                       present than "id" across arbitrary elements.
# 4. XPATH (relative, attribute-based) - More powerful than CSS for some
#                       cases (traversing to a parent, or matching by
#                       visible text), but generally slower and more
#                       verbose, so it's used only when CSS can't express
#                       the condition needed.
# 5. CLASS_NAME        - Classes are frequently reused across many elements
#                       for styling purposes, so a "class" locator is often
#                       not unique, making it more brittle.
# 6. TAG_NAME / XPATH (absolute path) - Least preferred. TAG_NAME almost
#                       never uniquely identifies one element on a real
#                       page. Absolute XPath is the single most brittle
#                       locator possible - it encodes the exact DOM
#                       hierarchy, so it breaks the moment a single <div>
#                       is added or removed anywhere above the target
#                       element.


if __name__ == "__main__":
    demonstrate_locators()
