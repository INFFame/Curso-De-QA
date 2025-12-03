# Importar librerias necesarias
import pytest
from playwright.sync_api import sync_playwright

# Configurar el navegador para las pruebas
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        # Iniciar el navegador Chromium en modo no headless con una pequeña demora
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        # Proporcionar el navegador a las pruebas
        yield browser
        # Cerrar el navegador después de las pruebas
        browser.close()
        
# Configurar la página para las pruebas        
@pytest.fixture
def page(browser):
    # Crear un nuevo contexto y página para cada prueba
    context = browser.new_context()
    page = context.new_page()
    # Navegar a la URL base antes de cada prueba
    page.goto("https://demoqa.com/")
    # Proporcionar la página a las pruebas
    yield page
    # Cerrar el contexto después de cada prueba
    context.close()