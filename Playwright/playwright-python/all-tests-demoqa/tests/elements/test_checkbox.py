# Importar la clase CheckBoxPage desde el módulo checkbox_page
from pages.elements.checkbox_page import CheckBoxPage


def test_home_checkbox(page):
    # Crear una instancia de la página de CheckBox
    checkbox = CheckBoxPage(page)
    
    # Navegar a la página de CheckBox
    page.goto("https://demoqa.com/checkbox")
    
    # Hacer clic en la casilla de verificación de Home
    checkbox.click_checkbox(checkbox.home_checkbox)
    
    # Verificar que la casilla de verificación de Home está marcada
    result = checkbox.is_checked()
    assert "home" in result.lower()
    
def test_desktop_checkbox(page):
    # Crear una instancia de la página de CheckBox
    checkbox = CheckBoxPage(page)
    
    # Navegar a la página de CheckBox
    page.goto("https://demoqa.com/checkbox")
    
    # Hacer clic en el botón para expandir las opciones
    checkbox.click_checkbox(checkbox.home_toggle)
    # Hacer clic en la casilla de verificación de Desktop
    checkbox.click_checkbox(checkbox.desktop_checkbox)
    
    # Verificar que la casilla de verificación de Desktop está marcada
    result = checkbox.is_checked()
    assert "desktop" in result.lower()
    
def test_documents_checkbox(page):
    # Crear una instancia de la página de CheckBox
    checkbox = CheckBoxPage(page)
    
    # Navegar a la página de CheckBox
    page.goto("https://demoqa.com/checkbox")
    # Hacer clic en el botón para expandir las opciones
    checkbox.click_checkbox(checkbox.home_toggle)
    # Hacer clic en la casilla de verificación de Documents
    checkbox.click_checkbox(checkbox.documents_checkbox)
    # Verificar que la casilla de verificación de Documents está marcada
    result = checkbox.is_checked()
    assert "documents" in result.lower()
    
def test_downloads_checkbox(page):
    # Crear una instancia de la página de CheckBox
    checkbox = CheckBoxPage(page)
    
    # Navegar a la página de checkbox
    page.goto("https://demoqa.com/checkbox")
    
    # Hacer clic en el botón para expandir las opciones
    checkbox.click_checkbox(checkbox.home_toggle)
    # Hacer clic en la casilla de verificación de Downloads
    checkbox.click_checkbox(checkbox.downloads_checkbox)
    # Verificar que la casilla de verificación de Downloads está marcada
    result = checkbox.is_checked()
    assert "downloads" in result.lower()