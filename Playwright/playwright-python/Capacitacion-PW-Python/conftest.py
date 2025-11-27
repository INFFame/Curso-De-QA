# Importar las librerías necesarias
import pytest
from typing import Generator
from playwright.sync_api import Page, APIRequestContext, Playwright # Importar Page para tipado

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

# Esta fixture se ejecuta una sola vez por sesión de pruebas
@pytest.fixture(scope="session")
def api_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    
    # Crear un contexto de API usando el fixture de pytest-playwright
    api_context = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            # Encabezados HTTP adicionales si es necesario
            "Accept": "application/json",
        },
    )
    
    # Proveer el contexto de API a los tests
    yield api_context
    # Cerrar el contexto de API y Playwright al finalizar la sesión de pruebas
    api_context.dispose()