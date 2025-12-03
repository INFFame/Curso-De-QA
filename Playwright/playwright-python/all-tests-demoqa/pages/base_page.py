class BasePage:
    def __init__(self,page):
        self.page = page
        
    def hacer_click(self, locator):
        self.page.locator(locator).click()
        
    def ingresar_texto(self, locator, text):
        self.page.locator(locator).fill(text)
        
    def obtener_texto(self, locator):
        return self.page.locator(locator).inner_text()
    
    def es_visible(self, locator):
        return self.page.locator(locator).is_visible()
    
    def esta_habilitado(self, locator):
        return self.page.locator(locator).is_enabled()
    
    def esta_deshabilitado(self, locator):
        return self.page.locator(locator).is_disabled()
    
    def es_checkeado(self, locator):
        return self.page.locator(locator).is_checked()
    
    def no_es_checkeado(self, locator):
        return self.page.locator(locator).is_unchecked()