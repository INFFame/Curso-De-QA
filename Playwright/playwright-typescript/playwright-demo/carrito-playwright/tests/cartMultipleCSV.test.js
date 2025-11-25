// Prueba para agregar múltiples productos al carrito usando datos desde CSV

const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { ProductPage } = require('../pages/ProductPage');
const { CartPage } = require('../pages/CartPage');
const { credentials } = require('./data/testData');

const fs = require('fs');
const csv = require('csv-parser');
const path = require('path');

test('Agregar múltiples productos al carrito en saucedemo desde CSV', async ({ page }) => {
    const loginPage = new LoginPage(page);
    const productPage = new ProductPage(page);
    const cartPage = new CartPage(page);

    // Paso 1: Login
    await loginPage.navigate();
    await loginPage.login(credentials.username, credentials.password);
    // Paso 2: Leer productos desde CSV y agregarlos al carrito
    const rutaCSV = path.resolve(__dirname, './data/productos.csv');
    const productos = [];
    await new Promise((resolve, reject) => {
        fs.createReadStream(rutaCSV)
            .pipe(csv())
            .on('data', (row) => {
                if (row.producto) {
                    productos.push(row.producto);
                }
            })
            .on('end', resolve)
            .on('error', reject);
    });

    // Agregar cada producto al carrito
    for (const producto of productos) {
        await productPage.addProductByName(producto);
    }
    // Paso 3: Ir al carrito
    await productPage.goToCart();
    // Paso 4: Verificar productos en el carrito
    const itemsEnCarrito = await cartPage.getCartItems();
    for (const producto of productos) {
        expect(itemsEnCarrito).toContain(producto);
    }
    
});