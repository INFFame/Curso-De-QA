from pages.base_page import BasePage

class ProductsPage(BasePage):
    # Localizadores
    boton_agregar_producto = ".btn_inventory"
    link_carrito = ".shopping_cart_link"
    
    async def agregar_todos_los_productos(self):
        #botones_agregar = await self.page.query_selector_all(self.boton_agregar_producto)
        botones_agregar = await self.page.locator("button.btn_inventory").all()
        for boton in botones_agregar:
            await boton.click()
    
    async def ir_al_carrito(self):
        await self.page.click(self.link_carrito)
        
    async def obtener_nombres_productos(self):
        nombres = []
        elementos_nombres = await self.page.locator(".inventory_item_name").all()
        for elemento in elementos_nombres:
            nombre = await elemento.text_content()
            nombres.append(nombre)
        return nombres