# Importar las librerías necesarias para Playwright
from playwright.sync_api import sync_playwright

def test_google_title():
    # 1. Iniciar Playwright (Gestor de recursos)
    with sync_playwright() as p:
        # 2. Abrir un navegador Chromium (no headless para ver la acción)
        browser = p.chromium.launch(headless=False)
        # 3. Crear un nuevo contexto de navegador (Sesión aislada)
        context = browser.new_context()
        # 4. Abrir una nueva página (Pestaña)
        page = context.new_page()
        
        # 5. Navegar a la página de Google
        page.goto("https://www.google.com")
        
        # 6. Esperar para observar (Solo para demostración)
        page.wait_for_timeout(3000)
        
        # 7. Validar el título de la página (Asersión)
        assert page.title() == "Google"
        
        # 8. Cerrar el navegador (Manejado por 'with' o explícito)
        browser.close()