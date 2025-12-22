import pytest
from playwright.async_api import async_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import os
# Crear carpeta para guardar trazas si no existe
os.makedirs("traces", exist_ok=True)


# Fixtures para configurar Playwright con pytest
# Scope de sesión para reutilizar el navegador en todas las pruebas
@pytest.fixture
async def browser():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        yield browser
        await browser.close()
        
# Hook para adjuntar capturas de pantalla en caso de fallo
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Scope de función para crear un nuevo contexto y página para cada prueba
@pytest.fixture
async def context(browser, request):
    context = await browser.new_context()
    # Habilitar trazas para cada contexto de prueba en caso de fallos
    await context.tracing.start(
        screenshots=True,
        snapshots=True
    )
    yield context
    # Detener la traza y guardarla en un archivo
        #! SOLO guardar la traza si el test FALLÓ
    if request.node.rep_call.failed:
        await context.tracing.stop(
            path=f"traces/{request.node.name}.zip"
        )
    else:
        await context.tracing.stop()
        
    await context.close()

# Scope de función para crear una nueva página para cada prueba
@pytest.fixture
async def page(context):
    page = await context.new_page()
    yield page
    await page.close()
    
@pytest.fixture
async def login_exitoso(page):
    login = LoginPage(page)
    await login.navegar()
    await login.screenshot("00_pantalla_login")
    await login.login("standard_user", "secret_sauce")
    
    return login

@pytest.fixture
async def productos_agregados(page, login_exitoso):
    products = ProductsPage(page)
    
    nombres_productos = await products.obtener_nombres_productos()
    await products.agregar_todos_los_productos()
    await products.ir_al_carrito()
    
    return nombres_productos