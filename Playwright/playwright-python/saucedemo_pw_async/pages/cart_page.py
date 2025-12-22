from pages.base_page import BasePage

class CartPage(BasePage):
    # Localizadores
    nombre_item = ".inventory_item_name"
    
    async def obtener_productos_carrito(self):
        nombres = []
        #items = await self.page.query_selector_all(self.nombre_item)
        items = await self.page.locator(self.nombre_item).all()
        for item in items:
            nombre = await item.text_content()
            nombres.append(nombre)
        return nombres