# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 18:10
# @Author : wujinying
# @File : 6.2aiohttp的使用
# @Software PyCharm


# 基本案例
'''
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.status
        # 对于要返回协程对象的操作要在前面加await来修饰，例如response调用text方法，查询api能发现返回值是协程对象，对于状态码返回值就是数值
        # 参考官方文档，看看其对应的返回值是怎样的类型，决定加不加

async def main():
    # with as 语句前面同样需要加async来修饰。该语句用于声明一个上下文管理器，能帮助自动分配和释放资源。异步方法中要声明一个支持异步的上下文管理器
    # conn = aiohttp.TCPConnector(verify_ssl=False)  # 防止ssl报错
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,verify_ssl=False)) as session:
        html, status = await fetch(session, 'https://cuiqingcai.com')
        print(f'html: {html[:100]}...')
        print(f'status: {status}')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main()) # 实际上是main方法在调用协程方法，就把main方法扔进事件循环
    # asyncio.run(main())     # py3.7后可以直接使用run方法替代最后的启动操作，不需要显示声明循环事件()
    """"报错的原因：aiohttp 内部使用了 _ProactorBasePipeTransport ，程序退出释放内存时自动调用其 __del__ 方法导致二次关闭事件循环。
    一般的协程程序是不会使用_ProactorBasePipeTransport 的，所以asyncio.run() 还是可以正常运行。而且这种情况仅在Windows上发生"""

'''


# url参数设置
'''对于url参数设置可以借助params参数传入字典即可
import aiohttp
import asyncio

async def main():
    params = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get', params=params) as response:
            print(await response.text())
            # 实际url："https://httpbin.org/get?name=germey&age=25"

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    
'''

# 其他请求类型(p203)

# post请求
'''post json数据提交，其对应的请求头中的"Content-Type" 为 "application/json"，post方法中的参数设置成json
import aiohttp
import asyncio

async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', json=data) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

'''
'''post表单提交，其对应的请求头中的"Content-Type" 为 "application/x-www-form-urlencoded"，post方法中的参数为data
import aiohttp
import asyncio

async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print(await response.text())

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

'''


# 响应
'''
import aiohttp
import asyncio

async def main():
    data = {'name': 'germey', 'age': 25}
    async with aiohttp.ClientSession() as session:
        async with session.post('https://httpbin.org/post', data=data) as response:
            print('status:', response.status)       # 状态码
            print('headers:', response.headers)     # 响应头
            print('body:', await response.text())   # 响应体
            print('bytes:', await response.read())  # 响应体二进制内容
            print('json:', await response.json())   # 响应体json结果

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# 有些字段前面要加await，有些不用。原则是如果返回的是一个协程对象(如有async修饰的方法)，那么前面就要加await，具体可以看
# aiohttp的api：https://docs.aiohttp.org/en/stable/client_reference.html

'''


# 超时设置
'''借助ClientTimeout对象设置超时，例如要设置1秒的超时时间
import aiohttp
import asyncio

async def main():
    timeout = aiohttp.ClientTimeout(total=1)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        async with session.get('https://httpbin.org/get') as response:
            print('status:', response.status)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())

# 超时抛出asyncio.exceptions.TimeoutError异常，ClientTimeout对象其他参数，例如connnect、socket_connect等
# 详情官方文档：https://docs.aiohttp.org/en/stable/client_quickstart.html#timeouts

'''


# 并发限制
import asyncio
import aiohttp

CONCURRENCY = 5
url = 'http://www.baidu.com'

semaphore = asyncio.Semaphore(CONCURRENCY)  # 借助Semaphore创建一个信号量对象，将其赋值为semaphore，来控制最大并发量
session = None

async def scrape_api():
    async with semaphore:
        print('scraping',url)
        async with session.get(url) as response:
            await asyncio.sleep(1)
            return await response.text()

async def main():
    global session      # 声明用全局？
    session = aiohttp.ClientSession()
    scrape_index_tasks = [asyncio.ensure_future(scrape_api()) for _ in range(10000)]

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())













