import os
import urllib.parse
import asyncio
from pyppeteer import launch
from pyppeteer.errors import PageError, NetworkError

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class WebCapture:
    def __init__(self, width, height, mime_type='png'):
        self.width = width
        self.height = height
        self.mime_type = mime_type

    def get_links(self, url):
        domain = urlparse(url).netloc
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                parsed_href = urlparse(href)
                if parsed_href.netloc == domain or not parsed_href.netloc:
                    href = urljoin(url, href)
                    links.append(href)
        links = list(set(links))
        links = sorted(links, key=lambda x: len(x), reverse=True)
        return links

    async def screenshot(self, url, file_name):
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto(url, {'waitUntil': 'networkidle0'})
        try:
            if page.url != url:
                print(f"URL mismatch: {page.url} != {url}")
            else:
                height = await page.evaluate('() => document.documentElement.scrollHeight')
                viewport_height = page.viewport['height']
                if height > viewport_height:
                    num = height // self.height + (height % self.height > 0)
                    for i in range(num):
                        start = i * self.height
                        end = start + self.height
                        if end > height:
                            end = height
                        await page.setViewport({'width': self.width, 'height': end})
                        part_file_name = f"{file_name}_{i+1}.{self.mime_type}"
                        await page.screenshot({'path': part_file_name, 'clip': {'x': 0, 'y': start, 'width': self.width, 'height': self.height}, 'type': self.mime_type})
                else:
                    await page.setViewport({'width': self.width, 'height': height})
                    await page.screenshot({'path': file_name, 'fullPage': True, 'type': self.mime_type})
        except (PageError, NetworkError):
            print(f"Failed to capture screenshot for {url}")
        await browser.close()

    async def capture_website_screenshots(self, url, folder_path, file_name):
        links = self.get_links(url)
        for link in links:
            folder_name = urllib.parse.unquote(os.path.basename(os.path.dirname(link)))
            if folder_name != ' ':
                os.makedirs(os.path.join(folder_path, folder_name), exist_ok=True)
                file_path = os.path.join(folder_path, folder_name, file_name)
                await self.screenshot(link, file_path)