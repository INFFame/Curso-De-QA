import { test, expect } from '@playwright/test';

// ? Importar la funcion de leer CSV desde utils/leerCSV.ts
import readCSV from './utils/leerCSV';
import * as path from 'path';

// * Crear la ruta al archivo CSV con los datos de usuarios
const csvPath = path.join(__dirname, 'data', 'users.csv');

// * Leer los usuarios desde el archivo CSV
const users = readCSV(csvPath);

test.describe('Pruebas de inicio de sesion', () => {
    // * Iterar sobre cada usuario leido desde el CSV en formato array de objetos {username, password}
   for (const user of users) {
    test(`Login para el usuario: ${user.username}.`, async ({ page }) => {
        await test.step('Ir a la página Login de sauce demo', async () => {
            // Ir a la pagina de sauce demo
            await page.goto('');
            // Verificar que estamos en la pagina de sauce demo
            await expect(page).toHaveURL('https://www.saucedemo.com/');
        });
         
        await test.step(`Ingresar nombre de usuario: ${user.username}` , async () => {
            // Ingresar nombre de usuario
            await page.locator('[data-test="username"]').fill(user.username);
            // Verificar que el nombre de usuario fue ingresado
            await expect(page.locator('[data-test="username"]')).toHaveValue(user.username);
        });

        await test.step('Ingresar contraseña', async () => {
            // Ingresar contraseña
            await page.locator('[data-test="password"]').fill(user.password);
            // Verificar que la contraseña fue ingresada
            await expect(page.locator('[data-test="password"]')).toHaveValue(user.password);
        });

        await test.step('Hacer click en boton Login', async () => {
            // Hacer click en el botón de login
            await page.locator('[data-test="login-button"]').click();
            // Verificar el resultado del login
            if (user.username === 'locked_out_user') {
                // Si el usuario es 'locked_out_user', verificar que se muestra un error
                await expect(page.locator('[data-test="error"]'), 'No es visible').toBeVisible();
            } else {
                // Para otros usuarios, verificar que se navega a la página de inventario
                await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
            }
        });

    });
   };
});
