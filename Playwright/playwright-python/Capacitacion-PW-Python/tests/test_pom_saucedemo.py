# Importar las librerias necesarias
from playwright.sync_api import expect
from pages.LoginPage import LoginPage

def test_login_saucedemo(page):
    # Crear una instancia de la página de Login
    login_page = LoginPage(page)
    
    # Navegar a la página de login
    page.goto("https://www.saucedemo.com/")
    # Realizar login con credenciales válidas
    login_page.login("standard_user", "secret_sauce")
    # Verificar que el login fue exitoso comprobando la URL actual
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Agregar el primer producto al carrito
    page.get_by_role("button", name="Add to cart").nth(0).click()
    # Verificar que el botón haya cambiado a "Remove"
    expect(page.get_by_role("button", name="Remove").nth(0)).to_have_text("Remove")