# Hands-On 4 — Selenium WebDriver Setup, Browser Drivers & Basic Commands

**Level:** Intermediate
**Type:** Coding exercise

## What's in this folder

- `setup_test.py` — Task 1: explains the three Selenium components (WebDriver, Grid, IDE) in a comment block, opens Chrome via `webdriver-manager`, navigates to the playground, prints the title, demonstrates implicit wait (with an explanation of why it's discouraged), and runs headless.
- `navigation_test.py` — Task 2: navigates to Simple Form Demo, asserts the URL, goes back, opens a second tab, switches between window handles, takes a screenshot, and demonstrates `get_window_size()` / `set_window_size()`.
- `screenshots/` — created automatically at runtime by `navigation_test.py`.

## How to run

From the project root (after installing `requirements.txt`):

```bash
python Handsons/Handson04/setup_test.py
python Handsons/Handson04/navigation_test.py
```

Both scripts run Chrome in headless mode by default, so no visible browser window is required.
