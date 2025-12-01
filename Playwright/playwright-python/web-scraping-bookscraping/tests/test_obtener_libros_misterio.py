from playwright.sync_api import Page
import csv
from pathlib import Path
from datetime import datetime

def test_obtener_libros_misterio(page: Page) -> None:
    page.goto("/catalogue/category/books/mystery_3/index.html")

    # Guardar los datos de los libros en una lista
    libros_misterio = []
    
    # Bucle para recorrer todas las páginas de la categoría "Misterio"
    while True:
        # Obtener todos los libros de la página actual
        books = page.locator(".product_pod")
        
        # Obtener la cantidad de libros en la página actual
        count = books.count()
        
        # Agregar los libros de la página actual a la lista
        for i in range(count):
            book = books.nth(i)
            title = book.locator("h3 a").get_attribute("title")
            price = book.locator(".product_price .price_color").inner_text()
            stock = book.locator(".instock.availability").inner_text().strip()
            
            libros_misterio.append({
                "title": title,
                "price": price,
                "stock": stock
            })
            
        # Buscar botón "next" para ir a la siguiente página
        next_button = page.locator(".pager .next a")
        
        if next_button.count() == 0:
            print("\nNo hay más páginas en la categoría 'Misterio'. Fin de la extracción.")
            break
        
        # Clic para ir a la siguiente página
        next_button.click()
        
        # Esperar a que la nueva página cargue
        page.wait_for_load_state("domcontentloaded")
        
        
    # Crear archivo CSV con los datos de los libros de misterio
    # Definir la ruta del archivo CSV
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    # Nombre del archivo con fecha y hora
    file_name = output_dir / f"Libros_misterio_{datetime.now().date()}.csv"
    
    # Escribir los datos en el archivo CSV
    with file_name.open(mode="w", newline="", encoding="utf_8") as f:
        # Crear el escritor CSV
        writer = csv.DictWriter(f, fieldnames=["title", "price", "stock"])
        # Escribir la cabecera en el archivo CSV
        writer.writeheader()
        # Escribir los datos de los libros en un archivo CSV
        writer.writerows(libros_misterio)
        
    print(f"\nDatos de libros de misterio guardados en {file_name}\n")