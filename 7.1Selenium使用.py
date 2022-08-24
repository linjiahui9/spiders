# -*- codeing = utf-8 -*-
# @Time : 2021/11/26 11:27
# @Author : wujinying
# @File : 7.1Selenium使用.py
# @Software PyCharm

# 安装ChromeDriver的参考链接：https://setup.scrape.center/selenium

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ChromeOptions

'''基本使用
browser=webdriver.Chrome()  # 初始化一个browser对象驱动浏览器模拟动作
try:
    browser.get('https://www.baidu.com')
    # input=browser.find_element_by_id('kw')
    # 看这篇文章：https://blog.csdn.net/c_lanxiaofang/article/details/123873554
    input = browser.find_element(By.ID,'kw')      # 4.0版本的
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait=WebDriverWait(browser,10)
    wait.until(EC.presence_of_element_located((By.ID,'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

'''


# 访问页面
'''
browser=webdriver.Chrome()              # 初始化浏览器对象
browser.get('https://www.taobao.com')   # 采用get()方法请求网页，传入url
print(browser.page_source)              # 输出页面源码
# browser.close()                       # 关闭页面

'''


# 查找节点
# selenium可以驱动浏览器填充表单，模拟点击等...selenium提供找到这些操作节点的方法，以便以下操作

'''单个节点
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
# 浏览网页源码，选中搜索输入框，能发现input标签的id和class属性值都为q
input_first=browser.find_element(By.ID,'q')
# find_element通用方法，传入参数是查找的方式和方式的值，这个方法就是下面那些方法的通用函数模板，这里等价于find_element_by_id(id)

"""下面3种获取节点的方法(案例是获取淘宝输入框)  find_element_by_name()根据class值获取，这里淘宝的输入框的class属性值值也为q
input_first=browser.find_element_by_id('q')                     # id选择器
input_second=browser.find_element_by_css_selector('#q')         # css选择器
input_third=browser.find_element_by_xpath('//*[@id="q"]')       # Xpath选择器，匹配所有节点，选取id="q"的节点
print(input_first,input_second,input_third)
"""
print(input_first)
# browser.close()

'''


'''多个节点
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
# lis=browser.find_elements_by_css_selector('.service-bd li')   # class属性值为service-bd的节点下的li节点
lis=browser.find_elements(By.CSS_SELECTOR,'.service-bd li')     # class选择器,开发工具选取到左侧导航栏所有条目
print(lis)              # 结果为列表类型，列表中的每个节点都属于WebElement类型
browser.close()
# 使用find_element方法查找，只能匹配成功第一个节点，类型为WebElement，使用find_elements方法得到的是列表类型的结果

'''


# 节点交互(常用的有：send_keys方法输入文字；clear方法清空文字，click方法点击按钮...)
'''
browser=webdriver.Chrome()
browser.get('https://www.taobao.com')
# input=browser.find_element_by_id('q')
# input = browser.find_element(By.ID,'q')                   # id选择器指定是id了就不用#
input = browser.find_element(By.CSS_SELECTOR,'#q')          # css选择器效果同上两
input.send_keys('iPhone')
time.sleep(1)
input.clear()
input.send_keys('iPad')
# button=browser.find_element_by_class_name('btn-search')
button=browser.find_element(By.CLASS_NAME,'btn-search')     # class选择器
button.click()
browser.close()
'''


# 动作链(例如鼠标拖拽，键盘按键等一些没有特定的执行对象，需要使用)
'''将某个节点从一处拖拽到另一处
browser=webdriver.Chrome()
url='https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
browser.get(url)
browser.switch_to.frame('iframeResult')
# source=browser.find_element_by_css_selector('#draggable')
source = browser.find_element(By.CSS_SELECTOR,'#draggable')     # 拖拽对象
# target=browser.find_element_by_css_selector('#droppable')
target = browser.find_element(By.CSS_SELECTOR,'#droppable')     # 拖拽目标
actions=ActionChains(browser)                                   # 声明ActionChains对象
actions.drag_and_drop(source,target)                            # 利用对象的drag_and_drop方法声明选中的拖拽对象和拖拽目标
actions.perform()                                               # perform方法执行动作
# 更多动作链操作：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

'''


# 执行js脚本(还有一些操作是没有api的，例如下拉进度条等，需要在这种情况模拟运行js，使用execute_script方法实现)
'''
browser=webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
browser.execute_script('alert("To Bottom")')        # 显示弹窗提示To Botom
#利用该方法将进度条拉到最底部，然后弹出了警告提示框...

'''


# 获取节点信息(Selenium选取节点的方法结果类型是WebElement，要用其自己相关的方法获取节点信息)
'''获取属性
browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
# logo=browser.find_element_by_id('logo-image')     # 网页源码好像没有
logo=browser.find_element(By.CSS_SELECTOR,'.ExploreHomePage-ContentSection-header svg')     # 随便整个
print(logo)
print(logo.get_attribute('width'))                # get_attributeff传入属性名就拿到该节点的属性值

'''


'''获取文本值
browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
# input=browser.find_element_by_class_name('zu-top-add-question')       # 网页源码没有
input = browser.find_element(By.CSS_SELECTOR,'.ExploreHomePage-ContentSection-header span') 
# 拿到该属性值下的的span子节点
print(input.text)       # text方法获取节点内部的文本信息

'''


'''获取id、位置、标签名和大小
browser=webdriver.Chrome()
url='https://www.zhihu.com/explore'
browser.get(url)
# input=browser.find_element_by_class_name('zu-top-question')
input = browser.find_element(By.CSS_SELECTOR,'#js-clientConfig')
print(input.id)         # id属性用来获取节点id
print(input.location)   # location属性用来获取节点在页面中的相对位置
print(input.tag_name)   # 获取标签的名称
print(input.size)       # 获取节点的大小(宽高)

'''


# 切换Frame(页面的子页面叫做iframe，其结构和外部网页的结构完全一样，Selenium打开一个页面后默认在父Frame里面操作)
'''需要在iframe操作节点时，要使用switch_to.frame方法切换
browser=webdriver.Chrome()
url='http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'     # f12看网页源码有两对html标签
browser.get(url)
browser.switch_to.frame('iframeResult')     # switch_to.frame方法切换iframe子页面
try:
    logo=browser.find_element_by_class_name('logo')     # 子页面没有logo节点，会抛出下面写的异常
except NoSuchElementException:
    print('No Logo')
browser.switch_to.parent_frame()            # 切换回父页面，重新获取logo节点
logo=browser.find_element_by_class_name('logo')
print(logo)
print(logo.text)

'''


# 延时等待(Selenium中get方法会在网页框架加载完才执行，有可能会有某些页面还有额外的Ajax请求js渲染，可以设置浏览器延时等待确保节点加载)
'''隐式等待(如果Selenium没有在DOM中找到节点，将继续等待，超出设定的等待时间后才报 找不到的异常)
browser = webdriver.Chrome()
browser.implicitly_wait(10)     # implicitly_wait方法参数延时等待10秒
browser.get('https://www.zhihu.com/explore')
input=browser.find_element_by_class_name('LoadingBar')
print(input)
# 这里只是跳转，开新页面看下面
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://spa2.scrape.center/')
input = browser.find_element_by_class_name('logo-image')
print(input)

'''
# '''显示等待(这种方式会指定要查找的节点和最长等待时间，如果在规定的时间内找到该节点就返回，找不到抛出 时间异常)
browser = webdriver.Chrome()
browser.get('https://www.taobao.com/')
wait = WebDriverWait(browser, 10)   # WebDriverWait对象指定等待的时间
input = wait.until(EC.presence_of_element_located((By.ID, 'q')))    # 用上面对象的until方法传入等待条件
# EC.presence_of_element_located等待条件代表节点出现，参数是节点的定位元组(id为q的节点在10秒内加载出来，就返回)

button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# EC.element_to_be_clickable等待条件代表按钮可点击，所以查找按钮时要该节点的按钮能在10秒内能点击就返回，反之就抛出异常
print(input, button)

# 其他等待条件：p221；官方文档：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# '''


# 前进和后退
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com/')
browser.get('https://www.taobao.com/')
browser.get('https://www.python.org/')
browser.back()          # back方法实现后退
time.sleep(1)
browser.forward()       # forward方法实现前进
browser.close()

'''


# Cookie(对Cookie的操作)
'''
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/explore')
print(browser.get_cookies())        # get_cookies方法获取所有的Cookie
browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})  # 添加Cookie，传入一个字典
print(browser.get_cookies())        # 再次获取Cookie时会发现多了一项，就是上面新加的
browser.delete_all_cookies()        # 删除所有的Cookie
print(browser.get_cookies())        # 删除后再获取就为空了

'''


# 选项卡管理(访问页面会开启一个新的选项卡页面)
'''
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.execute_script('window.open()')     # 访问百度后execute_script方法传入参数window.open()这个js语句，表示新开起一个选项卡
print(browser.window_handles)               # window_handles属性用来获取当前开启的所有选项卡，返回值时选项卡的代号列表
browser.switch_to.window(browser.window_handles[1])     # switch_to.window方法切换选项卡，参数为选项卡的代号
browser.get('https://www.taobao.com')                   # 新选项卡改成淘宝
time.sleep(1)
browser.switch_to.window(browser.window_handles[0])     # 切换
browser.get('https://python.org')                       # 把百度改成py

'''


# 异常处理
'''用Selenium中try-except语句捕获异常
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time Out')
try:
    # browser.find_element_by_id('hello')     # 在百度中找一个不存在的节点，会遇到异常
    browser.find_element(By.CSS_SELECTOR,'#hello')     # 在百度中找一个不存在的节点，会遇到异常
except NoSuchElementException:              # 该异常表示节点未找到
    print('No Element')
finally:
    browser.close()

# 其他异常类型：http://selenium-python.readthedocs.io/api.html#module-selenium.common.exceptions

'''


# 反屏蔽(大多数对Selenium有检查的网站都会检测当前浏览器窗口下的window.navigator对象中是否包含webdriver属性)
'''正常浏览器该对象属性值为undefined
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)          # 添加选项隐藏webdriver提示条和自动化扩展信息
browser.execute_script('Object.defineProperty(navigator, "webdriver", {get: () => undefined})')
# execute_script方法传入参数Object.defineProperty(navigator, "webdriver", {get: () => undefined})这个js语句
# 把webdriver属性设置为空，虽然设置为空了但是太晚了，这条语句是在js渲染完才执行的...网站是在页面渲染之前就发现了webdriver属性了
browser.get('https://antispider1.scrape.center/')

'''
'''利用CDP解决问题：利用该协议可以实现在每个页面刚加载的时候就执行js语句，将webdriver属性置空
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])    
option.add_experimental_option('useAutomationExtension', False)
browser = webdriver.Chrome(options=option)          # 添加选项隐藏webdriver提示条和自动化扩展信息
# 执行的CDP方法叫做：Page.addScriptToEvaluateOnNewDocument，再传入上面的js语句即可
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})
browser.get('https://antispider1.scrape.center/')

'''


# 无头模式(单纯只有网页，没有选项卡，导航栏，弹窗之类的东西)
'''
option = ChromeOptions()
option.add_argument('--headless')           # 利用ChromeOptions对象的add_argument方法添加--headless参数开启无头模式
browser = webdriver.Chrome(options=option)  # 添加选项参数
browser.set_window_size(1366, 768)          # 无头模式最好调一下窗口大小
browser.get('https://www.baidu.com')
browser.get_screenshot_as_file('preview.png')   # get_screenshot_as_file方法输出页面截图
'''
