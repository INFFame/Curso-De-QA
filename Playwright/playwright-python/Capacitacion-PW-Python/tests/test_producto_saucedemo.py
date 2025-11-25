# Importar librerias necesarias para Playwright y Pytest
from playwright.sync_api import expect

# Test para agregar un producto al carrito en Saucedemo
def test_agregar_producto(login_successful):
    # Usar la página autenticada proporcionada por el fixture
    page = login_successful
    
    # Agregar el primer producto al carrito
    page.get_by_role("button", name="Add to cart").nth(0).click()
    # Verificar que el botón haya cambiado a "Remove"
    expect(page.get_by_role("button", name="Remove").nth(0)).to_have_text("Remove")

    