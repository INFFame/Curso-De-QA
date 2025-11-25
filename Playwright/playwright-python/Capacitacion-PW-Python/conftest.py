# Importar las librerías necesarias
import pytest
from playwright.sync_api import Page # Importar Page para tipado

# Fixture para proporcionar una página de Playwright a los tests
@pytest.fixture(scope="function")
def login_successful(page: Page):
    # Navegación a la página de login
    page.goto("https://www.saucedemo.com/")
    # Realizar login con credenciales válidas
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    # Hacer clic en el botón de login
    page.get_by_role("button", name="Login").click()
    # Esperar a que la página de inventario cargue
    page.wait_for_url("https://www.saucedemo.com/inventory.html")
    
    # Retornar la página ya autenticada
    return page