# -*- codeing = utf-8 -*-
# @Time : 2022/8/2 21:46
# @Author : wujinying
# @File : 7.4Playwright的使用
# @Software PyCharm

# pip3 install playwright，安装后需要初始化：playwright install

# 基本使用
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.baidu.com')
        page.screenshot(path=f'screenshot-{browser_type.name}.png')
        print(page.title())
        browser.close()

"""
"""
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            browser = await browser_type.launch(headless=False)
            page = await browser.new_page()
            await page.goto('https://www.baidu.com')
            await page.screenshot(path=f'screenshot-{browser_type.name}.png')
            print(await page.title())
            await browser.close()

asyncio.run(main())

"""


# 代码生成
"""
playwright codegen --help

 -o 代表输出的代码文件的名称；
 —target 代表使用的语言，默认是 python，即会生成同步模式的操作代码，如果传入 python-async 就会生成异步模式的代码；
 -b 代表的是使用的浏览器，默认是 Chromium，其他还有很多设置，比如 
 —device 可以模拟使用手机浏览器，比如 iPhone 11，
 —lang 代表设置浏览器的语言，
 —timeout 可以设置页面加载超时时间。
 
# 启动一个 Firefox 浏览器，然后将操作结果输出到 script.py 文件 
playwright codegen -o script.py -b firefox

"""


# 支持移动端浏览器
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    iphone_12_pro_max = p.devices['iPhone 12 Pro Max']
    browser = p.webkit.launch(headless=False)
    context = browser.new_context(
        **iphone_12_pro_max,
        locale='zh-CN',
        geolocation={'longitude': 116.39014, 'latitude': 39.913904},
        permissions=['geolocation']
    )
    page = context.new_page()
    page.goto('https://amap.com')
    page.wait_for_load_state(state='networkidle')
    page.screenshot(path='location-iphone.png')
    browser.close()
    
"""


# 选择器
# css选择器


# css选择器 + 文本


# css选择器 + 节点关系


# XPath



# 常用操作方法
# 常见的一些 API 如点击 click，输入 fill 等操作，这些方法都是属于 Page 对象的，
# 所以所有的方法都从 Page 对象的 API 文档查找就好了，文档地址：https://playwright.dev/python/docs/api/class-page


# 事件监听
"""
from playwright.sync_api import sync_playwright

def on_response(response):
    print(f'Statue {response.status}: {response.url}')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on('response', on_response)
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    browser.close()

"""
"""
from playwright.sync_api import sync_playwright

def on_response(response):
    if '/api/movie/' in response.url and response.status == 200:
        print(response.json())

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on('response', on_response)
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    browser.close()

"""


# 获取页面源代码
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    html = page.content()
    print(html)
    browser.close()

"""


# 页面点击
# page.click(selector, **kwargs)


# 文本输入
# page.fill(selector, value, **kwargs)


# 获取节点属性
# page.get_attribute(selector, name, **kwargs)
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    href = page.get_attribute('a.name', 'href')
    print(href)
    browser.close()

"""


# 获取多个节点
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    elements = page.query_selector_all('a.name')
    for element in elements:
        print(element.get_attribute('href'))
        print(element.text_content())
    browser.close()

"""


# 获取单个节点
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://spa6.scrape.center/')
    page.wait_for_load_state('networkidle')
    element = page.query_selector('a.name')
    print(element.get_attribute('href'))
    print(element.text_content())
    browser.close()

"""


# 网络劫持
"""
from playwright.sync_api import sync_playwright
import re

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    def cancel_request(route, request):
        route.abort()

    page.route(re.compile(r"(\.png)|(\.jpg)"), cancel_request)
    page.goto("https://spa6.scrape.center/")
    page.wait_for_load_state('networkidle')
    page.screenshot(path='no_picture.png')
    browser.close()

"""

