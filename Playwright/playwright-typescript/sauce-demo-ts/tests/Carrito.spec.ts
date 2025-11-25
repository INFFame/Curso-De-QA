import { test, expect } from '@playwright/test';
import readCSV from './utils/leerCSV';
import * as path from 'path';

// * Crear la ruta de archivo al CSV de usuarios
const csvPath = path.join(__dirname, 'data', 'users.csv');

// * Leer los usuarios del archivo CSV
const users = readCSV(csvPath);

// * Lista de productos
const listaProductos: string[] = [];

test.describe('Pruebas del carrito de compras de sauce demo', () => {
   for (const user of users) {
        if (user.username === 'locked_out_user') continue; // ! Saltar el usuario bloqueado
        test(`El carrito contiene los productos agregados: ${user.username}`, async ({ page }) => {
            await test.step('Ingresar a la pagina Login de sauce demo', async () => {
                // Ir a la pagina de sauce demo
                await page.goto('');
                await expect(page).toHaveURL('https://www.saucedemo.com/');  
            });
            
            await test.step('Ingresar con usuario y contraseña', async () => {
                // Ingresar nombre de usuario
                await page.locator('[data-test="username"]').fill(user.username);
                // Verificar que el nombre de usuario fue ingresado
                await expect(page.locator('[data-test="username"]')).toHaveValue(user.username);

                // Ingresar contraseña
                await page.locator('[data-test="password"]').fill(user.password);
                // Verificar que la contraseña fue ingresada
                await expect(page.locator('[data-test="password"]')).toHaveValue(user.password);

                // Hacer click en el botón de login
                await page.locator('[data-test="login-button"]').click();
            });

            await test.step('Verificar estar en la pagina de productos', async () => {
                await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html')
            });

            await test.step('Añadir productos al carrito', async () => {
                // * Obtener los contenedores de cada producto y recorrerlos
                // Obtener el item completo por su test id
                const items = await page.locator('.inventory_item');
                // Obtener la cantidad total de items
                const total = await items.count();

                // Recorrer lista de items
                for (let i = 0 ; i < total ; i++) {
                    // Obtener el item de la lista de items segun su posición
                    const item = items.nth(i);
                    // Obtener el nombre del producto(item)
                    const name = await item.locator('.inventory_item_name').innerText();
                    // Buscar el botón 'add-to-cart' dentro del contenedor y clickearlo
                    const addBtn =  item.getByRole('button', { name: 'Add to cart'});
                    // Comprobar que existe el botón
                    if (await addBtn.count() > 0) {
                        // Comprobar si el botón es visible
                        await expect(addBtn).toBeVisible();
                        // Agregar productos a una lista
                        listaProductos.push(name)
                        // Si existe hacer click al botón
                        await addBtn.click();
                    } else {
                        // ! Si no existe el botón, mostramos la advertencia
                        console.warn(`Botón Add to cart no encontrado para: ${name}`);
                    }

                };
            });

            await test.step('Ir al carrito de compras', async () => {
                await page.goto('cart.html')
                await expect(page).toHaveURL('https://www.saucedemo.com/cart.html')
            })
            
            
            await test.step('Comprobar que existen los productos en el carrito de compras', async () => {
                // * Obtener los contenedores de cada producto
                // Identificamos cada producto
                const items = page.locator('.cart_item');
                // Verificar que la cantidad de productos coincide con los productos añadidos
                await expect(items).toHaveCount(listaProductos.length);

                // Verificar que cada producto añadido aparece en el carrito
                for (const producto of listaProductos) {
                    // Busca dentro de cada .cart_item un .inventory_item_name
                    await expect(page.locator('.inventory_item_name', { hasText: producto })).toBeVisible();
                }

            });
        
            
        });
        
    };
});

