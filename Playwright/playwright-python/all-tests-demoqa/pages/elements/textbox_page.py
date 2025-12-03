# Importar la clase BasePage
from pages.base_page import BasePage

class TextBoxPage(BasePage):
    # Definir los selectores de los elementos de la página
    full_name = "#userName"
    email = "#userEmail"
    current_address = "#currentAddress"
    permanent_address = "#permanentAddress"
    submit_button = "#submit"
    output_name = "#name"
    
    def fill_form(self, name, email, current, permanent):
        # Rellenar el formulario con los datos proporcionados
        self.ingresar_texto(self.full_name, name)
        self.ingresar_texto(self.email, email)
        self.ingresar_texto(self.current_address, current)
        self.ingresar_texto(self.permanent_address, permanent)
        self.hacer_click(self.submit_button)
        
    def get_output_name(self):
        # Obtener el texto del nombre de salida
        return self.obtener_texto(self.output_name)