from pages.base_page import BasePage

class ProductsPage(BasePage):
    # Localizadores
    boton_agregar_producto = ".btn_inventory"
    link_carrito = ".shopping_cart_link"
    
    def agregar_todos_los_productos(self):
        #botones_agregar = self.page.query_selector_all(self.boton_agregar_producto)
        botones_agregar = self.page.locator("button.btn_inventory").all()
        for boton in botones_agregar:
            boton.click()
    
    def ir_al_carrito(self):
        self.page.click(self.link_carrito)
        
    def obtener_nombres_productos(self):
        nombres = []
        elementos_nombres = self.page.locator(".inventory_item_name").all()
        for elemento in elementos_nombres:
            nombre = elemento.text_content()
            nombres.append(nombre)
        return nombres