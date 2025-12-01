from playwright.sync_api import Page
import csv
from pathlib import Path
from datetime import datetime

def test_obtener_libros(page: Page) -> None:
    page.goto("/")
    
    # Guardar los datos de los libros en una lista
    all_books = []
    
    while True:
        # Obtener todos los libros de la página actual
        books = page.locator(".product_pod")
        # Obtener la cantidad de libros en la página actual
        count = books.count()
        
        # Imprimir título y precio de cada libro
        for i in range(count):
            book = books.nth(i)
            title = book.locator("h3 a").get_attribute("title")
            price = book.locator(".product_price .price_color").inner_text()
            stock = book.locator(".instock.availability").inner_text().strip()
            #print(f"Título: {title} - Precio: {price} - Stock: {stock}")
            
            all_books.append({
                "title": title,
                "price": price,
                "stock": stock
            })    
            
        # Buscar boton "next" para ir a la siguiente página
        next_button = page.locator(".pager .next a")
        
        if next_button.count() == 0:
            print("\nNo hay más páginas. Fin de la extracción.")
            break
        
        # Clic para ir a la siguiente página
        next_button.click()
        # Esperar a que la nueva página cargue
        page.wait_for_load_state("domcontentloaded")
        
    # Crear archivo CSV con los datos de los libros
    # Definir la ruta del archivo CSV
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Nombre del archivo con fecha y hora
    file_name = output_dir / f"libros_{datetime.now().date()}.csv"
    
    # Escribir los datos en el archivo CSV
    with file_name.open(mode="w", newline="", encoding="utf-8") as f:
        # Crear el escritor CSV
        writer = csv.DictWriter(f, fieldnames=["title", "price", "stock"])
        # Escribir la cabecera en el archivo CSV
        writer.writeheader()
        # Escribir los datos de los libros en el archivo CSV
        writer.writerows(all_books)
        
    print(f"\nDatos de libros guardados en {file_name}\n")