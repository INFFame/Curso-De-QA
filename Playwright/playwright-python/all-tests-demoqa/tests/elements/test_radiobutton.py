# Importar la clase RadioButtonPage desde el módulo radiobutton_page
from pages.elements.radiobutton_page import RadioButtonPage

def test_radio_button_yes(page):
    # Crear una instancia de la página de RadioButton
    radio_button = RadioButtonPage(page)
    
    # Navegar a la página de RadioButton
    page.goto("https://demoqa.com/radio-button")
    
    # Hacer click en el botón de opción "Yes"
    radio_button.click_radio(radio_button.yes_radio)
    # Verificar que el resultado es "Yes"
    result = radio_button.get_result()
    assert "Yes" in result
    
def test_radio_button_impressive(page):
    # Crear una instancia de la página de RadioButton
    radio_button = RadioButtonPage(page)
    
    # Navegar a la página de RadioButton
    page.goto("https://demoqa.com/radio-button")
    
    # Hacer click en el botón de opción "Impressive"
    radio_button.click_radio(radio_button.impressive_radio)
    # Verificar que el resultado es "Impressive"
    result = radio_button.get_result()
    assert "Impressive" in result
    
def test_radio_button_no_disabled(page):
    # Crear una instancia de la página de RadioButton
    radio_button = RadioButtonPage(page)
    
    # Navegar a la página de RadioButton
    page.goto("https://demoqa.com/radio-button")
    
    # Verificar que el botón de opción "No" está deshabilitado
    assert radio_button.is_no_radio_disabled(radio_button.no_radio)