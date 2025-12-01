import asyncio
from playwright.async_api import async_playwright
import csv
from pathlib import Path
from datetime import datetime


async def quotes_scraping():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # Navegar a la pagina de quotes
        await page.goto("https://quotes.toscrape.com/")
        
        # Lista de citas
        quotes_data = []
        
        # Bucle a traves de las páginas
        while True:
            # Extraer citas en la pagina actual
            quotes = await page.query_selector_all(".quote")
            
            # Iterar sobre cada cita y extraer datos
            for quote in quotes:
                text = await quote.query_selector(".text")
                author = await quote.query_selector(".author")
                tags = await quote.query_selector_all(".tags .tag")
                
                # Convertir los elementos en textos
                text = await text.inner_text() if text else ""
                author = await author.inner_text() if author else ""
                tags = [await t.inner_text() for t in tags]
                
                quotes_data.append({
                    "text": text,
                    "author": author,
                    "tags": ", ".join(tags)
                })
                
            # Verificar si hay una pagina siguiente
            next_button = await page.query_selector(".pager .next a")
            
            # Verificar si el boton de siguiente existe
            if next_button is None:
                print("No hay más páginas.")
                break
            else:
                await next_button.click()
                await page.wait_for_load_state("networkidle")
                
        # Guardar los datos en un archivo CSV
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        # Nombre del archivo con timestamp
        file_name = output_dir / f"quotes_{datetime.now().date()}.csv"
        
        # Escribir datos en el archivo CSV
        with file_name.open(mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
            writer.writeheader()
            writer.writerows(quotes_data)
            
        print(f"Datos guardados en {file_name}")
    
if __name__ == "__main__":
    asyncio.run(quotes_scraping())