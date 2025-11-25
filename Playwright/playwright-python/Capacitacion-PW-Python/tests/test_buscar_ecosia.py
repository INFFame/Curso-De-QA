from playwright.sync_api import sync_playwright

def test_busqueda_google():
    # 1. Iniciar Playwright (Gestor de recursos)
    with sync_playwright() as p:
        # 2. Abrir un navegador Chromium (no headless para ver la acción)
        browser = p.chromium.launch(headless=False)
        # 3. Crear un nuevo contexto de navegador (Sesión aislada)
        context = browser.new_context()
        # 4. Abrir una nueva página (Pestaña)
        page = context.new_page()
        # 5. Navegar a la página de Ecosia
        page.goto("https://www.ecosia.org/")
        # 6. Escribir el término de búsqueda en el campo de búsqueda
        page.get_by_placeholder('Busca en la web...').fill("Playwright Python")
        # 7. Hacer clic en el botón de búsqueda
        page.get_by_role('button', name='Buscar').click()
        # 8. Validar que buscó correctamente verificando que el título contiene el término de búsqueda
        page.wait_for_timeout(3000)  # Esperar un momento para que se vea el titulo actualizado
        assert "Playwright Python" in page.title()
        # 9. Cerrar el navegador (Manejado por 'with' o explícito)
        browser.close()
        