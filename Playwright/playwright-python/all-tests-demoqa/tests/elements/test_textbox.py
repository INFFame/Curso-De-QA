# Importar la clase TextBoxPage desde el módulo textbox_page
from pages.elements.textbox_page import TextBoxPage

# Prueba para verificar el llenado del formulario de TextBox
def test_textbox_form(page):
    # Crear una instancia de la página de TextBox
    textbox = TextBoxPage(page)
    
    # Navegar a la página de TextBox
    page.goto("https://demoqa.com/text-box")
    
    # Llenar el formulario con datos de prueba
    textbox.fill_form(
        name="Marco García",
        email="marco@example.com",
        current="123 Calle Principal",
        permanent="456 Avenida Secundaria"
    )
    
    # Validar que el nombre se muestra correctamente en la salida
    output = textbox.get_output_name()
    assert "Marco García" in output
    