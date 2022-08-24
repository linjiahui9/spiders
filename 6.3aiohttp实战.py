# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 18:34
# @Author : wujinying
# @File : 6.3aiohttp实战
# @Software PyCharm

# 目标地址：https://spa5.scrape.center/  (ajax加载方式)
# 要实现完善的异步爬虫看p208介绍，其他源码：
# 此次采用分开两次异步获取，分别获取详情页和列表页ajax请求数据，需要将两次异步串行执行，并不是最佳的调度方法形式

# """
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 列表页ajax接口请求格式，limit的值为每一页包含多少本书，offset的值为每一页的偏移量计算公式：offset = limit * (page - 1)
INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'

# 详情页ajax接口请求格式，id可以在列表页ajax接口请求的数据中找到
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 1
CONCURRENCY = 5

session = None

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_COLLECTION_NAME]

# 声明信号量控制最大并发数量
semaphore = asyncio.Semaphore(CONCURRENCY)


# 获取页面
async def scrape_api(url):
    async with semaphore:       # saync with语句引入信号量作为上下文(6.2开头，先声明信号量控制，下面再声明请求)
        try:
            logging.info('scraping %s', url)
            async with session.get(url) as response:    # 查看6.1的使用aiohttp
                return await response.json()    # 查看6.2的响应
        except aiohttp.ClientError:
            logging.error('error occurred while scraping %s', url, exc_info=True)


# 爬取列表页
async def scrape_index(page):
    url = INDEX_URL.format(offset = PAGE_SIZE * (page - 1))
    return await scrape_api(url)    # 方法同样要用协程修饰，要加await，注意scrape_api方法返回的是协程对象


# 爬取详情页
async def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    data = await scrape_api(url)
    logging.info('saving data %s', data)
    # await save_data(data)
    return data


async def save_data(data):
    logging.info('saving data %s', data)
# '''
    if data:
        return await collection.update_one({
            'id': data.get('id')
        }, {
            '$set': data
        }, upsert=True)
# '''

async def main():
    # index tasks
    global session  # 声明为全局对象
    session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False))   # 6.1最后
    scrape_index_tasks = [asyncio.ensure_future(scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]  # 声明task列表，6.1的p141和p48
    results = await asyncio.gather(*scrape_index_tasks)     # 调用asyncio的gather方法，传入task列表参数(前面都没见过...和wait效果近似，但是返回结果略有差异，拿到的是dict类型)
    # results = await asyncio.wait(scrape_index_tasks)      # 拿到的是set类型，看下面输出结果，要提取键名，百度剔除wait方法提取到的set集合多余内容

    # detail tasks(没独立解析方法，直接main方法中解析传入...)
    print('results', results)
    ids = []
    for index_data in results:                  # 遍历每个列表页json
        if not index_data: continue
        print(type(index_data))
        for item in index_data.get('results'):  # 拿到所有列表页的results，看网页ajax请求的json数据
            # print(type(item))
            ids.append(item.get('id'))          # 再提取results字典下的id

    scrape_detail_tasks = [asyncio.ensure_future(scrape_detail(id)) for id in ids]      # 拿到详情页json
    result = await asyncio.wait(scrape_detail_tasks)     # 想获取多次请求，可以定义一个task列表，再使用asyncio包中的wait方法执行
    # result = await asyncio.gather(*scrape_detail_tasks)
    # print(result)
    await session.close()


if __name__ == '__main__':
    # loop.run_until_complete(main())     # ScrapeSpa5
    asyncio.get_event_loop().run_until_complete(main())     # 创建事件循环再把协程对象注册到事件循环中

    # asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # asyncio.run(main())

# """
"""
import asyncio
import json
import time

import aiohttp
import logging

from aiohttp import ContentTypeError
# 要实现MongoDB异步存储，离不开异步实现的MongoDB存储库motot：pip3 install motor
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa5.scrape.center/api/book/?limit=18&offset={offset}'
DETAIL_URL = 'https://spa5.scrape.center/api/book/{id}'
PAGE_SIZE = 18
PAGE_NUMBER = 1
CONCURRENCY = 5

MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'books'
MONGO_COLLECTION_NAME = 'books'

client = AsyncIOMotorClient(MONGO_CONNECTION_STRING)
db = client[MONGO_DB_NAME]
collection = db[MONGO_CONNECTION_STRING]

loop = asyncio.get_event_loop()


class Spider(object):

    def __init__(self):         # 干嘛的？
        self.semaphore = asyncio.Semaphore(CONCURRENCY)

    async def scrape_api(self, url):
        async with self.semaphore:
            try:
                logging.info('scraping %s', url)
                async with self.session.get(url) as response:
                    await asyncio.sleep(1)
                    return await response.json()
            except ContentTypeError as e:
                logging.error('error occurred while scraping %s', url, exc_info=True)

    async def scrape_index(self, page):
        url = INDEX_URL.format(offset=PAGE_SIZE * (page - 1))
        return await self.scrape_api(url)

    async def scrape_detail(self, id):
        url = DETAIL_URL.format(id=id)
        data = await self.scrape_api(url)
        # await self.save_data(data)

    async def save_data(self, data):
        logging.info('saving data %s', data)
        if data:
            return await collection.update_one({
                'id': data.get('id')
            }, {
                '$set': data
            }, upsert=True)

    async def main(self):
        self.session = aiohttp.ClientSession()
        # index tasks
        scrape_index_tasks = [asyncio.ensure_future(self.scrape_index(page)) for page in range(1, PAGE_NUMBER + 1)]
        results = await asyncio.gather(*scrape_index_tasks)

        # detail tasks
        print('results', results)
        ids = []
        for index_data in results:
            if not index_data: continue
            for item in index_data.get('results'):
                ids.append(item.get('id'))
        scrape_detail_tasks = [asyncio.ensure_future(self.scrape_detail(id)) for id in ids]
        await asyncio.wait(scrape_detail_tasks)
        await self.session.close()


if __name__ == '__main__':
    spider = Spider()
    loop.run_until_complete(spider.main())
    
"""

# 还有一个版本的