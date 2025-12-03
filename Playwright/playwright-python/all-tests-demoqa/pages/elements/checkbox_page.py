# Importar la clase BasePage
from pages.base_page import BasePage

class CheckBoxPage(BasePage):
    # Definir los selectores de los elementos de la página
    home_checkbox = 'label:has-text("Home")'
    desktop_checkbox = 'label:has-text("Desktop")'
    documents_checkbox = 'label:has-text("Documents")'
    downloads_checkbox = 'label:has-text("Downloads")'
    
    home_toggle = 'button[aria-label="Toggle"]'
    result = "#result"
    
    def click_checkbox(self, checkbox):
        # Hacer clic en la casilla de verificación especificada
        self.hacer_click(checkbox)
        
    def is_checked(self):
        # Verificar si la casilla de verificación está marcada
        return self.obtener_texto(self.result)