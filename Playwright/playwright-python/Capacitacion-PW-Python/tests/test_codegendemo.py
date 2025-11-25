import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://demoqa.com/")
    page.locator("div").filter(has_text=re.compile(r"^Elements$")).nth(1).click()
    page.get_by_role("listitem").filter(has_text="Buttons").click()
    page.get_by_role("button", name="Click Me", exact=True).click()
    expect(page.locator("#dynamicClickMessage")).to_contain_text("You have done a dynamic click")

    
    
