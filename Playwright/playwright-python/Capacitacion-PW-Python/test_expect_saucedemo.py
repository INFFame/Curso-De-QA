# Importar librerias necesarias para Playwright
from playwright.sync_api import sync_playwright, expect

def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        
        # Navegar a la página de Saucedemo
        page.goto("https://www.saucedemo.com/")
        
        # Rellenar el formulario de login
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        
        # Hacer clic en el botón de login
        page.get_by_role("button", name="Login").click()
        
        page.wait_for_timeout(3000)  # Esperar un momento para que se vea la página después del login
        
        # Que la URL contenga /inventory.html después del login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        
        # Cerrar el navegador
        browser.close()