from playwright.sync_api import Page
import csv
from pathlib import Path
from datetime import datetime

def test_quotes_scraping(page: Page) -> None:
    # Navegar a la pagina de quotes
    page.goto("/")
    
    # Lista de citas
    quotes_data = []
    
    # Bucle a traves de las páginas
    while True:
        # Extraer citas en la pagina actual
        quotes = page.locator(".quote")
        count = quotes.count()
        
        # Iterar sobre cada cita y extraer datos
        for i in range(count):
            quote = quotes.nth(i)
            text = quote.locator(".text").inner_text()
            author = quote.locator(".author").inner_text()
            tags = quote.locator(".tags .tag").all_inner_texts()
            
            quotes_data.append({
                "text": text,
                "author": author,
                "tags": ", ".join(tags)
            })
            
        # Verificar si hay una pagina siguiente
        next_button = page.locator(".pager .next a")
        
        # Verificar si el boton de siguiente existe
        if next_button.count() == 0:
            print("No hay más páginas.")
            break
        else:
            next_button.click()
            page.wait_for_load_state("networkidle")
            
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