import { test, expect  } from '@playwright/test'


test.describe('Pruebas de inicio de sesión', () => {
    test('Ingreso correcto de usuario y contraseña', async ({ page }) => {
        await test.step('Ingreso a la página sauce demo', async () => {
            // Ir a la pagina de sauce demo
            await page.goto('');

            // Verificar que estamos en la pagina de sauce demo
            await expect(page).toHaveURL('https://www.saucedemo.com/');
        });
        
        await test.step('Ingreso nombre de usuario', async () => {
            // Ingresar nombre de usuario
            await page.locator('[data-test="username"]').fill('standard_user');
            // Verificar que el nombre de usuario fue ingresado
            await expect(page.locator('[data-test="username"]')).toHaveValue('standard_user');
            
        });

        await test.step('Ingreso contraseña', async () => {
            // Ingresar contraseña
            await page.locator('[data-test="password"]').fill('secret_sauce');

            // Verificar que la contraseña fue ingresada
            await expect(page.locator('[data-test="password"]')).toHaveValue('secret_sauce');
        });

        await test.step('Hacer click en Botón Login', async () => {
            // Hacer click en el botón de login
            await page.locator('[data-test="login-button"]').click();

            // Verificar que estamos en la pagina de productos
            await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
            
        });
        
        
        
    });
    
});
