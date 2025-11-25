# Importar las librerías necesarias para Playwright
from playwright.sync_api import sync_playwright

def test_texto_playwright():
    # 1. Iniciar Playwright (Gestor de recursos)
    with sync_playwright() as p:
        # 2. Abrir un navegador Chromium (no headless para ver la acción)
        browser = p.chromium.launch(headless=False)
        # 3. Crear un nuevo contexto de navegador (Sesión aislada)
        context = browser.new_context()
        # 4. Abrir una nueva página (Pestaña)
        page = context.new_page()
        # 5. Navegar a la página de Playwright
        page.goto("https://playwright.dev/") 
        # 6. Localizar el texto específico en la página
        texto = page.get_by_text("Playwright enables reliable end-to-end testing for modern web apps.")
        # 7. Validar que el texto esté visible en la página (Asersión)
        assert texto.is_visible()
        # 8. Cerrar el navegador (Manejado por 'with' o explícito)
        browser.close()