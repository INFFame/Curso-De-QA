// Prueba de agregar 1 producto al carrito usando datos desde CSV

const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { ProductPage } = require('../pages/ProductPage');
const { CartPage } = require('../pages/CartPage');
const { credentials } = require('./data/testData');

const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

test('Agregar 1 producto al carrito en saucedemo desde CSV', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const productPage = new ProductPage(page);
    const cartPage = new CartPage(page);

    // Paso 1: Login
    await loginPage.navigate();
    await loginPage.login(credentials.username, credentials.password);

    // Paso 2: Leer el primer producto desde CSV y agregar al carrito
    const rutaCSV = path.resolve(__dirname, './data/productos.csv');
    let primerProducto = null;

    // Leer el primer producto del CSV de forma sincrona antes de continuar
    await new Promise((resolve, reject) => {
        fs.createReadStream(rutaCSV)
            .pipe(csv())
            .on('data', (row) => {
                if (!primerProducto && row.producto) {
                    primerProducto = row.producto;
                }
            })
            .on('end', resolve)
            .on('error', reject);
    });

    // Agregar solo el primer producto
    if (primerProducto) {
        await productPage.addProductByName(primerProducto);

        // Paso 3: Ir al carrito
        await productPage.goToCart();

        // Paso 4: Verificar producto en el carrito
        const itemsEnCarrito = await cartPage.getCartItems();
        expect(itemsEnCarrito).toContain(primerProducto);
    } else {
        throw new Error('No se encontró ningún producto en el CSV');
    }
});

