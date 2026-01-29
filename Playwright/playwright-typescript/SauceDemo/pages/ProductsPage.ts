import { Page, Locator } from '@playwright/test';

export class ProductsPage {
    readonly page: Page;
    readonly productsTitle: Locator;

    constructor(page: Page) {
        this.page = page;
        this.productsTitle = page.getByText('Products');
    }

    async isLoaded() {
        await this.productsTitle.waitFor();
    }
}