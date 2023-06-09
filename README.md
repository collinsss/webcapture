# Web Capture

Web Capture is a Python tool for capturing screenshots of web pages in batch. This tool was independently developed by ChatGPT3.5 based on the provided ideas. Further improvements and new features will be added in the future.

## Installation

You can install WebCapture using pip:
```
pip install webcapture
```
## Usage

Here is an example of how to use WebCapture:

```python
import asyncio
from webcapture import WebCapture

wc = WebCapture(800, 1800)
url = 'https://www.example.com'
folder_path = 'screenshots'
file_name = 'filename'
asyncio.run(wc.capture_website_screenshots(url, folder_path, file_name))
```

# Web Capture

Web Capture是用于批量捕获网页截图的Python工具。该工具由基于提供的想法独立开发的ChatGPT3.5。未来将添加进一步改进和新功能。

## 安装

您可以使用pip安装WebCapture：

```
pip install webcapture
```
## 使用

这是使用WebCapture的示例：


```python
import asyncio
from webcapture import WebCapture

wc = WebCapture(800, 1800)
url = 'https://www.example.com'
folder_path = 'screenshots'
file_name = 'filename'
asyncio.run(wc.capture_website_screenshots(url, folder_path, file_name))
```

