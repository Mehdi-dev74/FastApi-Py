import os
from playwright.async_api import async_playwright
import asyncio
from typing import Dict, Any

class StealthBrowser:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None
    
    async def start(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch(
            headless=False,
            args=[
                '--no-sandbox',
                '--disable-blink-features=AutomationControlled',
                '--disable-dev-shm-usage'
            ]
        )
        self.context = await self.browser.new_context(
            viewport={'width': 1366, 'height': 768},
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        )
        self.page = await self.context.new_page()
        # Hide automation flags
        await self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            window.chrome = {runtime: {}};
        """)
    
    async def goto(self, url: str):
        await self.page.goto(url, wait_until='networkidle')
    
    async def screenshot(self, path: str = "screenshot.png"):
        await self.page.screenshot(path=path)
    
    async def get_text(self, selector: str) -> str:
        return await self.page.text_content(selector) or ""
    
    async def fill(self, selector: str, text: str):
        await self.page.fill(selector, text)
    
    async def click(self, selector: str):
        await self.page.click(selector)
    
    async def close(self):
        if self.browser:
            await self.browser.close()
