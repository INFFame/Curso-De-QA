# Importar las librerias necesarias
import pytest
# Importar librerias necesarias para Playwright asíncrono
from playwright.async_api import async_playwright, expect


# Fixture para proporcionar una página de Playwright a los tests
@pytest.mark.asyncio
# Test asíncrono para verificar el doble clic en un botón
async def test_boton_doble_click():
    # Iniciar Playwright de forma asíncrona
    async with async_playwright() as p:
        # Iniciar el navegador Chromium en modo no headless
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        
        # Navegar a la página de prueba
        await page.goto("https://demoqa.com/buttons")
        # Realizar doble clic en el botón
        await page.get_by_role("button", name="Double Click Me").dblclick()
        # Validar que el mensaje de doble clic sea visible
        await expect(page.get_by_text("You have done a double click")).to_be_visible()