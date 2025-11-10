import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    api_request_context = await playwright.request.new_context(base_url="http://localhost:3000")
    data = {
        "completed" : False,
        "title" : "test",
        "id" : 102,
    }
    
    response = await api_request_context.post("/todos", data=data)
    assert response.ok
    print(f"todo Var: {response}")
    
async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())