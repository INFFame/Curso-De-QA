# Importar librerias necesarias para Playwright
from playwright.sync_api import sync_playwright, expect

def test_checkbox():
    with sync_playwright() as p:
        # Iniciar el navegador
        browser = p.chromium.launch(headless=False)
        # Crear un nuevo contexto de navegador
        context = browser.new_context()
        # Comenzar la traza antes de abrir la página
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # Abrir una nueva página
        page = context.new_page()
        # Navegar a la página de ejemplo con checkboxes
        page.goto("https://demoqa.com/checkbox")
        # Interactuar con los checkboxes
        page.get_by_role("button", name="Toggle").click()  # Expandir el árbol
        page.check("label[for='tree-node-desktop']")  # Seleccionar el checkbox "Desktop"  
        # Verificar que el checkbox esté seleccionado
        assert page.is_checked('label[for="tree-node-desktop"]')
        
        # Provocamos un fallo intencional para ver el manejo de errores
        expect(page.locator("#result")).to_have_text("You have selected :home")  # Esto fallará intencionalmente
        
        # Crear una captura de pantalla después de la interacción
        page.screenshot(path="screenshots/checkbox_interaction.png")
        # Captura de pantalla de un elemento especifico
        elemento_fallo = page.locator("#result")
        # Guardar la captura de pantalla del elemento con fallo
        elemento_fallo.screenshot(path="screenshots/elemento_fallo.png")
        
        
        # Detener la traza y guardarla en un archivo
        context.tracing.stop(path = "logs/trace.zip")
        # Cerrar el navegador
        browser.close()     