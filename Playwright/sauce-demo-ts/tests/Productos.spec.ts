import { test, expect } from '@playwright/test';
import readCSV from './utils/leerCSV';
import * as path from 'path';

// * Crear la ruta al archivo CSV con los datos de usuarios
const csvPath = path.join(__dirname, 'data', 'users.csv'); 

// * Leer los usuarios desde el archivo CSV
const users = readCSV(csvPath);


test.describe('Pruebas de productos de sauce demo', () => {
    for (const user of users) {
        if (user.username === 'locked_out_user') continue; // ! Saltar el usuario bloqueado
        test(`Agregar productos con el usuario: ${user.username}`, async ({ page }) => {
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
                    const addBtn = item.getByRole('button', { name: 'Add to cart'});
                    // Comprobar que existe el botón
                    if (await addBtn.count() > 0) {
                        // Comprobar si el botón es visible
                        await expect(addBtn).toBeVisible();
                        // Si existe hacer click al botón
                        await addBtn.click();
                        // Esperar que el boton cambie a 'Remove'
                        await expect(item.getByRole('button', { name: 'Remove' })).toBeVisible();
                    } else {
                        // ! Si no existe el botón, mostramos la advertencia
                        console.warn(`Botón Add to cart no encontrado para: ${name}`);
                    }


                };

            });      

            
        });
        
    };
});
