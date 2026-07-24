# Hands-On 5 — Locators & Explicit Waits

**Level:** Intermediate
**Type:** Coding exercise

## What's in this folder

- `locator_demo.py` — Task 1: locates the Simple Form Demo message input using all 6 strategies (ID, NAME, CLASS_NAME, TAG_NAME, absolute XPath, relative XPath), then 3 different CSS selectors for the same element, then uses XPath `text()` and `contains()` on the Checkbox Demo labels. Ends with a ranked comment block explaining the most-to-least preferred locator order.
- `waits_demo.py` — Task 2: waits for the Bootstrap Alerts success message with `WebDriverWait` + `EC.visibility_of_element_located`, times a `time.sleep(3)` version against an explicit-wait version, demonstrates `EC.element_to_be_clickable`, and uses a FluentWait-style poll (every 500ms, ignoring `NoSuchElementException`) for a dynamically-loaded table row.

## How to run

```bash
python Handsons/Handson05/locator_demo.py
python Handsons/Handson05/waits_demo.py
```

No hard-coded `sleep()` is used anywhere except the one intentional demonstration in `waits_demo.py`, which exists specifically to contrast it against the explicit-wait version.
