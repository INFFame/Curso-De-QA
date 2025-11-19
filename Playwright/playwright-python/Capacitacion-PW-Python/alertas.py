# Importar las librerías necesarias para Playwright
from playwright.sync_api import sync_playwright

def test_alerta():
    # 1. Iniciar Playwright (Gestor de recursos)
    with sync_playwright() as p:
        # 2. Abrir un navegador Chromium (no headless para ver la acción)
        browser = p.chromium.launch(headless=False)
        # 3. Crear un nuevo contexto de navegador (Sesión aislada)
        context = browser.new_context()
        # 4. Abrir una nueva página (Pestaña)
        page = context.new_page()
        # 5. Navegar a la página de demoqa con alertas
        page.goto("https://demoqa.com/alerts")
        # 6. Hacer que la alerta sea aceptada automáticamente
        page.on("dialog", lambda dialog: dialog.accept())        
        # 7. Hacer clic en el botón para mostrar la alerta
        page.get_by_role("button", name="Click me").nth(0).click()
        # 8. Cerrar el navegador (Manejado por 'with' o explícito)
        browser.close()