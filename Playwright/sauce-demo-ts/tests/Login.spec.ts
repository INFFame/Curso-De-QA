import { test, expect } from '@playwright/test';

test.describe('Pruebas iterando usernames desde la página', () => {
    test('Obtener usernames listados en la página y probar login con cada uno', async ({ page }) => {
        await test.step('Ingresar a la pagina de Sauce Demo', async () => {
            // Ir a la página de login
            await page.goto('');
            await expect(page).toHaveURL('https://www.saucedemo.com/');
        });
        

        await test.step('Obtener usernames de la página', async () => {
            // Localizar el contenedor donde se muestran los "Accepted usernames"
            const usersLocator = page.locator('.login_credentials');
            await expect(usersLocator).toBeVisible();

            // Extraer texto y procesar usernames
            const text = await usersLocator.innerText();
            // Dividir el texto en líneas y filtrar usernames
            const usernames = text
                .split('\n') // divide por líneas
                .map(line => line.trim()) // elimina espacios en blanco
                .filter(line => /^[a-z0-9_]+$/i.test(line)); // filtra solo palabras tipo usernames

                
            // Iterar sobre cada username encontrado en la página
            for (const username of usernames) {
                await test.step(`Probar login con el username: ${username}`, async () => {
                    await test.step('Ingresar usuario', async () => {
                        // Ingresar usuario y verificar
                        await page.locator('[data-test="username"]').fill(username);
                        await expect(page.locator('[data-test="username"]')).toHaveValue(username);
                    });
                    
                    await test.step('Ingresar contraseña', async () => {
                        // Ingresar la contraseña y verificar
                        const demoPassword = 'secret_sauce';
                        await page.locator('[data-test="password"]').fill(demoPassword);
                        await expect(page.locator('[data-test="password"]')).toHaveValue(demoPassword); 
                    });
                    
                    await test.step('Hacer click en botón Login', async () => {
                        // Hacer click en login y verificar resultado según usuario
                        await page.locator('[data-test="login-button"]').click();

                        // Verificar resultado del login
                        if (username === 'locked_out_user') {
                            // Usuario bloqueado debe mostrar error
                            await expect(page.locator('[data-test="error"]')).toBeVisible();
                            // Volver a la página de login para la siguiente iteración
                            await page.goto('');
                            await expect(page).toHaveURL('https://www.saucedemo.com/');

                        } else {
                            // Para los demás usuarios, debemos llegar al inventario
                            await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');
                            // Volver a la página de login para la siguiente iteración
                            await page.goto('');
                            await expect(page).toHaveURL('https://www.saucedemo.com/');

                        }
                    })

                });
            }
        });

    });
});