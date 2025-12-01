import asyncio
from playwright.async_api import async_playwright
import csv
from pathlib import Path
from datetime import datetime

async def test_quotes_tag():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        # Navegar a la pagina de quotes
        await page.goto("https://quotes.toscrape.com/")
        
        # Tag especifico a filtrar
        target_tag = "love"
        
        # Lista de citas filtradas
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
                
                # Filtrar por el tag especifico
                if target_tag in [t.lower() for t in tags]:
                    quotes_data.append({
                        "text": text,
                        "author": author,
                        "tags": ", ".join(tags)
                    })
            
            # Boton para la siguiente pagina
            next_button = await page.query_selector(".pager .next a")
            
            # Verificar si existe la siguiente pagina
            if next_button is None:
                print("No hay mas paginas. Finalizando la extraccion.")
                break
            # Si existe, navegar a la siguiente pagina
            else:
                await next_button.click()
                await page.wait_for_load_state("networkidle")
                
                
        # Guardar los datos en un archivo CSV
        output_dir = Path("output")
        output_dir.mkdir(exist_ok=True)
        # Nombre del archivo
        file_name = output_dir / f"quotess_tag_{target_tag}_{datetime.now().date()}.csv"
        
        # Escribir datos en el archivo CSV
        with file_name.open(mode="w", newline="", encoding="utf-8") as f:
            # Definir los nombres de las columnas
            writer = csv.DictWriter(f, fieldnames=["text", "author", "tags"])
            writer.writeheader()
            writer.writerows(quotes_data)
            
        print(f"Datos guardados en {file_name}")
        
if __name__ == "__main__":
    asyncio.run(test_quotes_tag())