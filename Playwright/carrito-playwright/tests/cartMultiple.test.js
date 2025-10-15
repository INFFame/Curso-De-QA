const { test, expect } = require('@playwright/test');
const { LoginPage } = require('../pages/LoginPage');
const { ProductPage } = require('../pages/ProductPage');
const { CartPage } = require('../pages/CartPage');
const { credentials, products, toDelete } = require('./testData');

test('Agregar productos al carrito en saucedemo', async ({ page }) => {
  const loginPage = new LoginPage(page);
  const productPage = new ProductPage(page);
  const cartPage = new CartPage(page);

  // Paso 1: Login
  await loginPage.navigate();
  await loginPage.login(credentials.username, credentials.password);

  //Paso 2: Agregar productos en ciclo
  for (const product of products.list){
    await productPage.addProductByName(product);
  }
  // Paso 3: Ir al carrito
  await productPage.goToCart();

 // Paso 4: Verificar productoSSSS en el carrito
// for (const product of products.list){
 // expect(items).toContain(product);
 //}

 //Paso 5: Eliminar los productos en el carrito
 for (const productToBeDeleted of toDelete){
    await productPage.deleteProductByName(productToBeDeleted);
 }
});
