# -*- codeing = utf-8 -*-
# @Time : 2022/7/15 14:24
# @Author : wujinying
# @File : 6.1协程的基本原理
# @Software PyCharm

# 定义协程
# async定义的方法会变成一个无法直接执行的协程对象，必须将此对象注册到事件循环中才能执行
# async关键字定义协程，await关键字用来挂起阻塞方法的执行
# coroutine：翻译为协程，py中指协程对象类型，可以将协程对象注册到事件循环中，就会被事件循环调用，所以用async定义方法
'''
import asyncio

async def execute(x):       # async关键字定义了一个execute方法
    print('Number:', x)

coroutine = execute(1)          # 调用execute方法，然而这个方法并没有执行，而是返回一个coroutine协程对象
print('Coroutine:', coroutine)
print('After calling execute')

# loop = asyncio.get_event_loop()     # get_event_loop方法创建一个事件循环loop

loop = asyncio.new_event_loop()       # py3.10版本需要改成这样写
asyncio.set_event_loop(loop)

loop.run_until_complete(coroutine)  # 调用run_until_complete方法将协程对象注册到事件循环中，接着启动，最后才能看见execute方法打印出了接收的数字
print('After calling loop')

'''


# 上面代码把协程对象coroutine传递给run_until_complete方法时，实际上执行了将coroutine封装成task对象，下面进行显示声明
# task：任务，这是对协程对象的进一步封装，包含协程对象的各个状态
'''
import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

# loop = asyncio.get_event_loop()

loop = asyncio.new_event_loop()       # py3.10版本需要改成这样写
asyncio.set_event_loop(loop)

task = loop.create_task(coroutine)    # 定义loop对象后调用其create_task方法，将协程对象转化为task对象，
print('Task:', task)                  # 输出一下它所处的状态
loop.run_until_complete(task)         # 添加task对象到事件循环中执行
print('Task:', task)                  # 状态变成finished，其result值变成1，这就是定义execute方法返回的结果
print('After calling loop')

'''


# 定义task对象的另一种方式，直接调用asyncio包中的ensure_future方法，返回结果也是task对象
# 这样也就可以不用借助loop对象，即使没有声明loop对象，也能提前定义好task对象
'''
import asyncio

async def execute(x):
    print('Number:', x)
    return x

coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
# loop = asyncio.new_event_loop()       # py3.10版本需要改成这样写
# asyncio.set_event_loop(loop)          # new_event_loop以及set_event_loop必须放在ensure_future上面，py3.10版本写法这里未知

loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')

'''


# 绑定回调
'''
import asyncio
import requests

async def request():                # 定义请求百度的协程方法
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

def callback(task):
    print('Status:', task.result()) # 打印task对象结果的回调方法

coroutine = request()               # 拿到协程对象
task = asyncio.ensure_future(coroutine)     # ensure_future方法直接定义一个task对象

task.add_done_callback(callback)            # 希望的效果是当协程对象执行完后，就去执行声明的callback方法
# 调用add_done_callback方法，把callback方法传递给封装好的task对象，这样执行完task后，就调用callback方法了，
# 同时，task对象还会作为参数(协程方法返回的结果)传递给callback方法，调用task对象的result方法就可以获得返回结果
print('Task:', task)

loop = asyncio.get_event_loop()             # 创建事件循环对象
loop.run_until_complete(task)               # 添加task对象到事件循环中执行
print('Task:', task)

'''
'''
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

coroutine = request()
task = asyncio.ensure_future(coroutine)
print('Task:', task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('Task Result:', task.result())    # task对象拿到协程方法的返回值，其实可以直接result方法拿到状态码

'''


# 多任务协程
'''上面的例子都是执行一次请求，想获取多次请求，可以定义一个task列表，再使用asyncio包中的wait方法执行
import asyncio
import requests

async def request():
    url = 'https://www.baidu.com'
    status = requests.get(url)
    return status

tasks = [asyncio.ensure_future(request()) for _ in range(5)]    # 定义一个for循环创建5个task组成列表
print('Tasks:', tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))        # 把列表传入asyncio包中的wait方法，再将其注册进事件循环中，就可以发起5个任务

for task in tasks:
    print('Task Result:', task.result())
    
'''


# 协程实现
'''
import asyncio
import requests
import time

start = time.time()

async def request():
    url = 'https://httpbin.org/delay/5'     # 该网站会在一次请求中等待5秒再回复
    print('Waiting for', url)
    response = requests.get(url)
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]   # 直接创建10个task对象
loop = asyncio.get_event_loop()                                 # 创建事件循环
loop.run_until_complete(asyncio.wait(tasks))                    # 利用wait方法将10个task对象扔进事件循环中

end = time.time()
print('Cost time:', end - start)

'''
'''
# 要实现异步处理，要先有挂起操作，当一个任务需要io等待结果时候，可以挂起当前任务，转而执行其他任务，上面的方法是一本正经的串行执行...
# await关键字，它可以将耗时等待的操作挂起来，让出控制权
# await后面的对象必须是如下格式之一：
    # 一个原生协程对象
    # 一个有type.coroutine修饰的生成器，这个生成器可以返回协程对象
    # 由一个包含__await__方法的对象返回的一个迭代器
import asyncio
import requests
import time

start = time.time()

"""
async def request():
    url = 'https://static4.scrape.cuiqingcai.com/'
    print('Waiting for', url)
    response = await requests.get(url)      # 这里直接用await不符合上面的要求
    print('Get response from', url, 'response', response)
"""

# 独立出来一个协程对象(方法)
async def get(url):
    return requests.get(url)

async def request():
    url = 'https://httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)               # 改成后面接协程对象，协程对象(方法)来执行请求
    print('Get response from', url, 'response', response)

tasks = [asyncio.ensure_future(request()) for _ in range(10)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)

# 结果协程还不是异步执行的，也就是说仅仅将涉及的io操作代码封装到async修饰的方法中是不行的，
# 只有使用支持异步操作的请求方式才能实现真正的异步操作，要使用aiohttp...

'''


# 使用aiohttp(aiohttp是一个支持异步请求的库，和asyncio结合使用，能实现异步请求操作)
# pip3 install aiohttp  官方文档：https://aiohttp.readthedocs.io/    文档有两部分，Client和Server
# '''
import asyncio
import aiohttp
import time

start = time.time()

async def get(url):
    session = aiohttp.ClientSession()   # 这里换成aiohttp库中ClientSession类的get方法来请求
    response = await session.get(url)   # 前面调用get进方法这里请求有阻塞请求要等待，马上被挂起

    await response.text()
    await session.close()
    return response

async def request():
    url = 'https://httpbin.org/delay/5'
    print('Waiting for', url)
    response = await get(url)                   # 执行到这里有阻塞的话还没进方法就被挂起了
    print('Get response from', url, 'response')

tasks = [asyncio.ensure_future(request()) for _ in range(100)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
"""
开始运行时，事件循环会运行第一个task，对于第一个task来说，当执行到第一个await跟着的get方法时，它会被挂起，但是这个get方法第一步的执行时非阻塞的，
挂起之后会立刻被唤醒，立即又进入执行，并创建了ClientSession对象，接着遇到第二个await，调用session.get请求方法，然后就被挂起了。
由于请求需要等待很久，所以一直没被唤醒，好在第一个task被挂起了，接下来事件循环会寻找当前未被挂起的协程继续执行，于是转到去执行第二个task，
流程操作和第一个task一模一样，直到执行第100个task的session.get方法之后，全部的task都被挂起了，只能等待了...5秒后有几个请求同时有了响应，
然后几个task也被唤醒继续执行
"""

# '''
# '''
import asyncio
import aiohttp
import time

def test(number):
    start = time.time()

    async def get(url):
        session = aiohttp.ClientSession()

        response = await session.get(url)
        await response.text()
        await session.close()
        return response

    async def request():
        url = 'https://www.baidu.com/'
        await get(url)

    tasks = [asyncio.ensure_future(request()) for _ in range(number)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

    end = time.time()
    print('Number:', number, 'Cost time:', end - start)

for number in [1, 3, 5, 10, 15, 30, 50, 75, 100, 200, 500]:
    test(number)    # 结果能看出来一般服务器上百次高并发是能抗下来的
# '''