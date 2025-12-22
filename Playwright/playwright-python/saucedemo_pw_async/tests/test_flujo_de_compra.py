import pytest
from playwright.async_api import expect

from pages.products_page import ProductsPage
from pages.cart_page import CartPage

@pytest.mark.asyncio
async def test_login_exitoso(page, login_exitoso):
    await login_exitoso.screenshot("01_productos_despues_login")
    await expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

@pytest.mark.asyncio
async def test_agregar_producto_al_carrito(page, login_exitoso):
    products = ProductsPage(page)
    await products.agregar_todos_los_productos()
    await products.screenshot("02_productos_con_carrito")
    await expect(page.locator(".shopping_cart_badge")).to_have_text("6")
    
@pytest.mark.asyncio
async def test_productos_en_carrito(page, productos_agregados):
    cart = CartPage(page)

    await expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )
    
    await cart.screenshot("03_vista_carrito")

    productos_carrito = await cart.obtener_productos_carrito()
    
    assert len(productos_carrito) == 6
    assert productos_carrito == productos_agregados