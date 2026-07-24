"""
test_input_form.py
Hands-On 7 - Task 2, Step 57: new test using InputFormPage.
"""

from pages.input_form_page import InputFormPage


def test_input_form_submit(driver, base_url):
    page = InputFormPage(driver)
    page.navigate_to(base_url)
    page.open_from_home()

    page.fill_form(
        name="Jordan Reyes",
        email="jordan.reyes@example.com",
        phone="9876543210",
        address="221B Baker Street",
    )
    page.submit_form()

    assert "success" in page.get_success_message().lower()
