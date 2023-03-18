import asyncio
from webcapture import WebCapture

wc = WebCapture(800, 1800)
url = 'https://www.example.com'
folder_path = 'screenshots'
file_name = 'filename'
asyncio.run(wc.capture_website_screenshots(url, folder_path, file_name))
