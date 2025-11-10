from playwright.sync_api import Page
import pytest

# Manera de ejecutar solamente en un navegador específico
#@pytest.mark.only_browser("chromium")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"

# Manera de saltar una prueba en un navegador específico
#@pytest.mark.skip_browser("chromium")  
def test_inventory_page(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text("h3") == "Epic sadface: You can only access '/inventory.html' when you are logged in."