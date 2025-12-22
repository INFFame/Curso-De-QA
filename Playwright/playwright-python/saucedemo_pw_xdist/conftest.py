import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import os
# Crear el directorio para las trazas si no existe
os.makedirs("traces", exist_ok=True)


# Fixtures para configurar Playwright con pytest
# Scope de sesión para reutilizar el navegador en todas las pruebas
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()
        
# Hook para adjuntar capturas de pantalla en caso de fallo
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

# Scope de función para crear un nuevo contexto y página para cada prueba
@pytest.fixture
def context(browser, request, worker_id):
    context = browser.new_context()

    # Iniciar la grabación de trazas
    context.tracing.start(
        screenshots=True,
        snapshots=True
    )

    yield context

    # Si la prueba falla, guardar la traza con un nombre basado en el worker y el nombre de la prueba
    if request.node.rep_call.failed:
        context.tracing.stop(
            path=f"traces/{worker_id}_{request.node.name}.zip"
        )
    else:
        context.tracing.stop()

    context.close()
# Scope de función para crear una nueva página para cada prueba
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

# Scope de función para realizar un login exitoso código reutilizable
@pytest.fixture
def login_exitoso(page):
    login = LoginPage(page)
    login.navegar()
    login.screenshot("00_pantalla_login")
    login.login("standard_user", "secret_sauce")
    
    return login
# Scope de función para agregar productos al carrito codigo reutilizable
@pytest.fixture
def productos_agregados(page, login_exitoso):
    products = ProductsPage(page)
    
    nombres_productos = products.obtener_nombres_productos()
    products.agregar_todos_los_productos()
    products.ir_al_carrito()
    
    return nombres_productos