class ProductPage {
  /**
   * @param {import('@playwright/test').Page} page
   */
  constructor(page) {
    this.page = page;
    this.addToCartButton = 'button[data-test="add-to-cart-sauce-labs-backpack"]';
    this.cartIcon = '.shopping_cart_link';
  }

//metodo para agregar productos por nombre
async addProductByName(productName){
  await this.page.click(`text=${productName}`);
  await this.page.click('button:has-text("Add to cart")');
  await this.page.click('button:has-text("Back to products")');
}

//metodo para eliminar producto del carro por nombre
async deleteProductByName(productName){
  //Encuentra todos los contenedores de productos en el carrito
  const productContainers = await this.page.$$('.cart_item');
  for (const container of productContainers) {
    //Busca el nombre del producto dentro del contenedor
    const nameElement = await container.$('.inventory_item_name');
    const nameText = await nameElement.textContent();

    //Compara con el nombre que se quiere eliminar
    if (nameText.trim() === productName) {
      //Encuentra el botón "Remove" dentro del mismo contenedor
      const removeButton = await container.$('button:has-text("Remove")');
      if (removeButton){
        await removeButton.click();
      }
      break; //Sale del ciclo una vez eliminado
    }
  }
}

//metodo para entrar al carrito
  async goToCart() {
    await this.page.click(this.cartIcon);
  }
}

module.exports = { ProductPage };