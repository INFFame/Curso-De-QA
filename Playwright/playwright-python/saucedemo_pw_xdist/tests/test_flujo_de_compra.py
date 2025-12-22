from playwright.sync_api import expect

from pages.products_page import ProductsPage
from pages.cart_page import CartPage

# Prueba de flujo de compra completo
def test_login_exitoso(page, login_exitoso):
    login_exitoso.screenshot("01_productos_despues_login")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

# Prueba para agregar productos al carrito
def test_agregar_producto_al_carrito(page, login_exitoso):
    products = ProductsPage(page)
    products.agregar_todos_los_productos()
    products.screenshot("02_productos_agregados")
    expect(page.locator(".shopping_cart_badge")).to_have_text("6")

# Prueba para verificar productos en el carrito
def test_productos_en_carrito(page, productos_agregados):
    cart = CartPage(page)

    expect(page).to_have_url(
        "https://www.saucedemo.com/cart.html"
    )
    cart.screenshot("03_vista_carrito")

    productos_carrito = cart.obtener_productos_carrito()
    
    assert len(productos_carrito) == 6
    assert productos_carrito == productos_agregados