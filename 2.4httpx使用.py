# -*- codeing = utf-8 -*-
# @Time : 2022/7/4 17:28
# @Author : wujinying
# @File : httpx使用
# @Software PyCharm

# urllib和requests无法访问http2.0协议的网页，使用httpx的请求库，requests有的httpx几乎都有
# 安装：pip3 install httpx，但是这样安装是不支持http2.0的要写成 'httpx[http2]'，这样写才支持2.0

#基本使用
'''
import httpx
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response = httpx.get('https://www.httpbin.org/get')
# response = httpx.get('https://www.httpbin.org/get',headers=headers)
print(response.status_code) # 状态码
print(response.headers)     # 响应头，结果类似一个字典
print(response.text)        # 响应体"User-Agent": "python-httpx/0.23.0"代表用httpx请求的
'''
'''
import httpx
client = httpx.Client(http2=True)   # httpx默认是使用1.1的，需要声明使用的是2.0
# 声明Client对象，赋值为client的变量，再显示的把http2参数设置成True
response = client.get('https://spa16.scrape.center')
print(response.text)
print(response.http_version)    # requests中没有http_version属性，该属性能获取当前连接的http版本
'''
'''
status_code：状态码
text：响应体的文本内容
content：响应体的二进制内容，当前请求的目标数据是二进制数据时使用该属性获取
headers：响应头，可以像获取字典中的内容一样获取其中某个header的值
json：调用该方法将文本结果转换为json对象
其他方法：https://www.python-httpx.org/quickstart/
'''



# Client对象(类比requests中的Session对象)
'''两种写法对Client对象使用官方推荐用with as写法，另一种写法要在最后显示调用close方法关闭CLient对象
import httpx
with httpx.Client() as client:
    response = client.get('https://www.httpbin.org/get')
    print(response)

print("----------------------------------------------")

# clients = httpx.Client()
# try:
#     responses = clients.get('https://www.httpbin.org/get')
# finally:
#     clients.close()
'''

'''指定会话的参数
import httpx
url = 'http://www.httpbin.org/headers'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'}
with httpx.Client(headers=headers) as client:
    r = client.get(url)
    print(r.json()['headers']['User-Agent'])

# Client其他用法：https://www.python-httpx.org/advanced/
'''



# 支持http2.0(基本使用小节中有)
# 如果客户端用2.0连接仅支持http1.1的服务器，那么它也需要该用http1.1



# 支持异步请求(即AsyncClient，支持py中async请求模式)
'''httpx异步请求官方文档：https://www.python-httpx.org/async/
import httpx
import asyncio
async def fetch(url):
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url)
        print(response.text)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(fetch('https://www.httpbin.org/get'))
'''