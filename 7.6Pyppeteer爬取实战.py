# -*- codeing = utf-8 -*-
# @Time : 2022/7/30 14:26
# @Author : wujinying
# @File : 7.6Pyppeteer爬取实战
# @Software PyCharm

# 列表页ajax接口url：https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=MzA5NjE0NmQwY2JiNTRjN2VjYjFmN2VjODU1MzRiOGQ4MmYwMjA0YSwxNjU5MTQ2NjM2
# 详情页ajax接口url：https://spa2.scrape.center/api/movie/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx/?token=Y2I4ZGZhODM2YTdkNTRmMjA3NDMxOGE3OTE5YjU5Y2UxZTQ0NzEwNywxNjU5MTQ2NjQw
# 详情页url：https://spa2.scrape.center/detail/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx
# 接口中的token字段每次请求都会改变，这个字段是Base64编码加密而得，detail也是

import logging
from os.path import exists
from os import makedirs
import json
import asyncio
from pyppeteer import launch
from pyppeteer.errors import TimeoutError

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
WINDOW_WIDTH, WINDOW_HEIGHT = 1366, 768

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

browser, tab = None, None
HEADLESS = False     # 无头模式

# 初始化Pyppeteer
async def init():
    global browser, tab     # 全局变量设置浏览器对象和新建选项卡对象
    browser = await launch(headless=HEADLESS,
                           args=['--disable-infobars', f'--window-size={WINDOW_WIDTH},{WINDOW_HEIGHT}'], devtools=True)     # 禁用提示，无头模式，浏览器宽高，开启调试
    tab = await browser.newPage()           # 新建选项卡
    await tab.setViewport({'width': WINDOW_WIDTH, 'height': WINDOW_HEIGHT})     # 页面显示宽高

# 通用爬取方法
async def scrape_page(url, selector):
    logging.info('scraping %s', url)
    try:
        await tab.goto(url)     # 选项卡对象的goto方法访问对应url
        # 调用page变量的waitForSelector方法，传入selector选择器，页面就等待选择器对应的节点选项加载出来，加载出来后就立即返回，否则持续等待到超时
        await tab.waitForSelector(selector, options={   # 通过options指定最长等待时间(10秒，毫秒为单位)
            'timeout': TIMEOUT * 1000
        })
    except TimeoutError:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页
async def scrape_index(page):
    url = INDEX_URL.format(page=page)
    await scrape_page(url, '.item .name')   # 传入的选择器是指定列表页中的电影名称，意味着电影名加载出来就代表加载成功了，一般选择点击详情页的链接的父节点即可

# 解析列表页
async def parse_index():
    # querySelectorAllEval方法第一个参数是selector代表选择器，第二个参数pageFunction代表要执行的js方法，
    # 该参数的js方法作用是找出和选择器匹配的节点，然后根据pageFunction定义的逻辑从这些节点中抽取对应的结果并返回
    return await tab.querySelectorAllEval('.item .name', 'nodes => nodes.map(node => node.href)')   # 返回结果是拼接好的href...

# 爬取详情页
async def scrape_detail(url):
    await scrape_page(url, 'h2')

# 解析详情页
async def parse_detail():
    url = tab.url       # url提取直接调用tab对象(选项卡)的ur属性获取当前页面的url

    # 名称在详情页只涉及一个节点，所以用querySelectorEval方法，传入参数节点，或者css选择器，第二个参数pageFunction，这里调用node的innerText属性，提取文本值
    name = await tab.querySelectorEval('h2', 'node => node.innerText')

    # 类别有多个用querySelectorAllEval方法，第一个参数混用了css选择器和节点，第二个参数使用nodes方法，然后调用map方法提取node的innerText属性就可以得到所有电影类型
    categories = await tab.querySelectorAllEval('.categories button span', 'nodes => nodes.map(node => node.innerText)')

    # 封面同样传入其节点，封面的url对应的是src属性，这里调用node的src属性来提取
    cover = await tab.querySelectorEval('.cover', 'node => node.src')

    # 分数同样传入css选择器，在调用node的innerText提取文本
    score = await tab.querySelectorEval('.score', 'node => node.innerText')

    # 同上
    drama = await tab.querySelectorEval('.drama p', 'node => node.innerText')
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }                           # 最后汇总成字典返回

# 数据存储
async def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # dump方法两个参数：ensure_ascii=False保证中文不乱码，另一个indent设置保持json数据结构有两行缩进

async def main():
    await init()
    try:
        for page in range(1, TOTAL_PAGE + 1):
            await scrape_index(page)                    # 爬取列表页
            detail_urls = await parse_index()           # 解析列表页
            print(detail_urls)
            for detail_url in detail_urls:
                await scrape_detail(detail_url)         # 爬取详情页
                detail_data = await parse_detail()      # 解析详情页
                logging.info('data %s', detail_data)
                await save_data(detail_data)
    finally:
        await browser.close()

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# Pyppeteer本身存在问题，运行超过20秒会出现问题：
# 原因Pyppeteer内部使用了WebSocket，如果WebSocket客户端发送ping信号20秒后仍然为收到pong应答，就会中断连接
# 问题解决方法和详情描述见：https://github.com/miyakogi/pyppeteer/issues/178，此时可以通过修改Pyppeteer源码解决问题，
# 对应源码修改见：https://github.com/miyakogi/pyppeteer/pull/160/files，即给connect方法添加 ping_interval=None 和 ping_timeout=None 这两个参数
# 也可以选择覆写connect方法的实现：https://github.com/miyakogi/pyppeteer/pull/160 中找到，例如patch_pyppeteer的定义
