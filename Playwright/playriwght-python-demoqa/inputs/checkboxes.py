import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        # Iniciar el navegador
        browser = await p.chromium.launch(headless=False)
        # Crear un nuevo contexto de navegador
        context = await browser.new_context()
        # Comenzar la traza antes de abrir la página
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)
        # Abrir una nueva página
        page = await context.new_page()
        
        # Darle tamaño a la ventana
        await page.set_viewport_size({"width": 1800, "height": 1200})
        
        # Navegar a la página de ejemplo con checkboxes
        await page.goto("https://demoqa.com/checkbox")
        
        # Acciones
        
        await page.check('label[for="tree-node-home"]')
        
        await page.screenshot(path = "screenshots/checkboxes.png")
        
        # Aserciones
        
        await page.is_checked('label[for="tree-node-home"]') is True
        
        await expect(page.locator("#result")).to_contain_text("You have selected :homedesktopnotescommandsdocumentsworkspacereactangularveuofficepublicprivateclassifiedgeneraldownloadswordFileexcelFile")
        
        # Detener la traza y guardarla en un archivo
        await context.tracing.stop(path = "logs/trace.zip")
        
        # Cerrar el navegador
        await browser.close()     
               
asyncio.run(main())