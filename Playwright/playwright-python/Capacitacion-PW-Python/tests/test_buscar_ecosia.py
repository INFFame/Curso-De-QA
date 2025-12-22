from playwright.sync_api import Page

def test_busqueda_google(page: Page):
    # 1. Navegar a la página de Ecosia
    page.goto("https://www.ecosia.org/")
    # 2. Escribir el término de búsqueda en el campo de búsqueda
    page.get_by_placeholder('Busca en la web...').fill("Playwright Python")
    # 3. Hacer clic en el botón de búsqueda
    page.get_by_role('button', name='Buscar').click()
    # 4. Validar que buscó correctamente verificando que el título contiene el término de búsqueda
    page.wait_for_timeout(3000)  # Esperar un momento para que se vea el titulo actualizado
    assert "Playwright Python" in page.title()
    # El navegador se cierra automáticamente gracias a pytest-playwright
        