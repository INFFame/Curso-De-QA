# Importar la clase BasePage
from pages.base_page import BasePage

class RadioButtonPage(BasePage):
    # Definir los selectores de los elementos de la página
    yes_radio = 'label[for="yesRadio"]'
    impressive_radio = 'label[for="impressiveRadio"]'
    no_radio = 'label[for="noRadio"]'
    
    span_result = '.text-success'
    
    def click_radio(self, radio_btn):
        # Hacer clic en el botón de opción especificado
        self.hacer_click(radio_btn)
        
    def get_result(self):
        # Obtener el texto del resultado
        return self.obtener_texto(self.span_result)
    
    def is_no_radio_disabled(self, radio_btn):
        # Verificar si el botón de opción "No" está deshabilitado
        return self.esta_deshabilitado(radio_btn)