from playwright.sync_api import Page
import csv
from pathlib import Path
from datetime import datetime

def test_quotes_tag(page: Page) -> None:
    # Navegar a la pagina de quotes
    page.goto("/")
    
    # Tag especifico a filtrar
    target_tag = "love"
    
    # Lista de citas filtradas
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
            
            # Filtrar por el tag especifico
            if target_tag in [t.lower() for t in tags]:
                quotes_data.append({
                    "text": text,
                    "author": author,
                    "tags": ", ".join(tags)
                })
        
        # Boton para la siguiente pagina
        next_button = page.locator(".pager .next a")
        
        # Verificar si existe la siguiente pagina
        if next_button.count() == 0:
            print("No hay mas paginas. Finalizando la extraccion.")
            break
        # Si existe, navegar a la siguiente pagina
        else:
            next_button.click()
            page.wait_for_load_state("networkidle")
            
            
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