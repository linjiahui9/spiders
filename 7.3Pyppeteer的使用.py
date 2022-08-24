# -*- codeing = utf-8 -*-
# @Time : 2022/7/27 9:12
# @Author : wujinying
# @File : Pyppeteer的使用
# @Software PyCharm

# pip3 install pyppeteer
# 官方文档：https://pyppeteer.github.io/pyppeteer/reference.html

#快速上手
'''
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq


async def main():
    browser = await launch()        # 调用launch方法新建Browser对象赋值给browser变量，这步相当于启动浏览器
    page = await browser.newPage()  # 调用Browser对象的newPage方法新建一个Page对象，相当于在浏览器新建一个选项卡

    # 调用Page对象的goto方法，方法中传入参数url，浏览器加载对应页面
    await page.goto('https://spa2.scrape.center/')      # 该页面用js渲染一些ajax接口自带加密

    # 调用page变量的waitForSelector方法，传入选择器，页面就等待选择器对应的节点选项加载出来，加载出来后就立即返回，否则持续等待到超时
    await page.waitForSelector('.item .name')
    doc = pq(await page.content())  # 页面加载完后，调用content方法可以获取当前浏览器页面的源代码，js渲染后的代码

    names = [item.text() for item in doc('.item .name').items()]    # pyquery解析
    print('Names:', names)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())     # 这其中还实现了异步(是异步的请求方式？)...

'''
"""
import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})      # 该方法设置窗口大小
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)                                          # 协程的休眠方法
    await page.screenshot(path='example.png')                       # 页面截图，该方法参数传入截图保存路径及名称，也可以指定其他参数
    # type：保存格式     quality：清晰度     fullPage：是否全屏       clip：裁切等参数

    # evaluate方法执行js语句并返回对应数据(传入一个js函数，使用return方法返回页面宽、高、像素大小比例三个值，为json格式)
    # Pyppeteer还有exposeFunction、evaluateOnNewDocument、evaluateHandle方法了解一下...
    dimensions = await page.evaluate('''() => {                     
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')

    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())

"""


# launch方法
# launch方法api：https://pyppeteer.github.io/pyppeteer/reference.html#launcher
# 看书p246...


# 无头模式(headless参数默认为True或者不用设置)
"""
import asyncio
from pyppeteer import launch

async def main():
    await launch(headless=False)        # 设置为False启动浏览器时能看见界面了
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

"""


# 调试模式
"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(devtools=True)
    # devtools参数设置为True开启调试工具(每开启一个页面都弹出一个调试窗口，同时无头模式也会关闭)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

"""


# 禁用提示条lanunch方法中args参数传入list形式参数(例如：args=['--disable-infobars'])


# 防止检测
"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False, args=['--disable-infobars'])
    page = await browser.newPage()
    # Page对象有个evaluateOnNewDocument方法，意思是在每次加载页面是执行某条语句，可以利用来隐藏Webdriver属性(方法)
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

"""


# 页面大小设置
"""
import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])      # 这里的args参数设置浏览器宽高
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})      # Page对象的setViewport方法设置页面显示大小，用的单位是像素
    await page.evaluateOnNewDocument('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

"""


# 用户数据持久化(启动浏览器时设置userDataDir属性)
"""
import asyncio
from pyppeteer import launch

width, height = 1366, 768

async def main():
    # userDataDir属性值设置成./userdata
    browser = await launch(headless=False, userDataDir='./userdata',
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

# ./userdata在当前目录生成名为这个的文件夹，该文件夹具体介绍看官方文档(要代理)：https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md

"""


# Browser对象(launch方法返回的浏览器对象)
# 开启无痕模式
# 关闭
"""
import asyncio
from pyppeteer import launch

width, height = 1200, 768

async def main():
    browser = await launch(headless=False,
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    context = await browser.createIncognitoBrowserContext()     # createIncognitoBrowserContext方法开启无痕模式
    page = await context.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(10)
    await browser.close()                                       # 页面关闭

asyncio.get_event_loop().run_until_complete(main())

"""


# Page对象
# 选择器
# """
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')
    j_result1 = await page.J('.item .name')
    j_result2 = await page.querySelector('.item .name')
    jj_result1 = await page.JJ('.item .name')
    jj_result2 = await page.querySelectorAll('.item .name')
    print('J Result1:', j_result1)      # J方法和querySelector方法返回结果都是和传入选择器相匹配的单节点，返回值为ElementHandle对象
    print('J Result1:', j_result2)      # JJ方法和querySelectorAll方法返回的都是选择器匹配的节点组成的列表，列表内容是ElementHandle对象
    print('J Result1:', jj_result1)
    print('J Result1:', jj_result2)
    # await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# """


# 选项卡操作
"""
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')
    page = await browser.newPage()
    await page.goto('https://www.bing.com')
    pages = await browser.pages()       # 先用Browser对象的pages方法获取所有打开的页面
    print('Pages:', pages)
    page1 = pages[1]                    # 选中第二个页面(看上面输出结果有3个页面，第二个是百度，第三个才是bing)
    await page1.bringToFront()          # 再调用bringToFront方法切换
    await asyncio.sleep(100)

asyncio.get_event_loop().run_until_complete(main())

"""


# 页面操作
"""
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    await page.goto('https://spa2.scrape.center/')
    # 后退
    await page.goBack()
    # 前进
    await page.goForward()
    # 刷新
    await page.reload()
    # 保存 PDF
    # await page.pdf()
    # 截图
    await page.screenshot()
    # 设置页面 HTML
    await page.setContent('<h2>Hello World</h2>')
    # 设置 User-Agent
    await page.setUserAgent('Python')
    # 设置 Headers
    await page.setExtraHTTPHeaders(headers={})
    # 关闭
    await asyncio.sleep(100)
    # await page.close()
    # await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# Future exception was never retrieved

# future: <Future finished exception=NetworkError('Protocol error (Target.sendMessageToTarget): No session with given id')>
# pyppeteer.errors.NetworkError: Protocol error (Target.sendMessageToTarget): No session with given id
# 两行报错

"""


# 点击
"""
import asyncio
from pyppeteer import launch
from pyquery import PyQuery as pq

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://spa2.scrape.center/')
    await page.waitForSelector('.item .name')

    # click方法中第一个参数就是选择器，即在哪里操作，第二个参数是配置：
    # button：鼠标按钮，取值有left、middle、right
    # clickCount：点击次数，取值有1和2，表示单击和双击
    # delay：延时点击
    await page.click('.item .name', options={
        'button': 'left',
        'clickCount': 1,  # 1 or 2
        'delay': 3000,  # 毫秒
    })
    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

"""


# 输入文本
"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.taobao.com')

    # type方法输入文本，第一个参数传入选择器，第二个参数传入要输入的文本内容
    await page.type('#q', 'iPad')

    # 点击搜索
    await page.click('.btn-search.tb-bg', options={
        'button': 'left',
        'clickCount': 1,  # 1 or 2
        'delay': 3000,  # 毫秒
    })
    # 关闭
    await asyncio.sleep(100)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

"""


# 获取信息
"""
import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://www.baidu.com/')
    print('HTML:', await page.content())        # Page对象调用content方法获取源码
    print('Cookies:', await page.cookies())     # 调用cookies方法获取cookie
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

"""

# 执行(看上面evaluate方法...)

# 延时等待

