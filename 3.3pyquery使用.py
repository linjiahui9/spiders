# -*- codeing = utf-8 -*-
# @Time : 2021/11/28 15:36
# @AUTHOR : wujinying
# @File : 3.3pyquery使用.py
# @Software : PyCharm

# 安装库：pip3 install pyquery

# 初始化
"""字符串初始化
html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq   # 引入PyQuery对象取别名pq
doc = pq(html)      # 传入字符串参数完成初始化
print(doc('li'))    # 初始化的对象传入css选择器，这个实例传入li节点，就可以获取所有li节点

"""

"""url初始化
from pyquery import PyQuery as pq
import requests
doc = pq(url = 'https://cuiqingcai.com')
print(doc('title'))
print("---------------------------------")
docc = pq(requests.get('https://cuiqingcai.com').text)  # 和上面效果一样，
# requests.get拿到网页源码，再text转成字符串
print(doc('title'))

"""

'''文件上传
from pyquery import PyQuery as pq
doc = pq(filename='test.html')  # filename参数指定上传文件名
print(doc('li'))                # 提取所有li节点

'''



html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
 </div>
'''

# css选择器
"""
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('#container .list li'))   # 拿到id为container的节点，再取其内部class值为list的节点下的所有li节点
print(type(doc('#container .list li')))     # 类型为PyQuery
for item in doc('#container .list li').items():
    print(item.text())
"""



# 查找节点
"""子节点
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')    # class为list的节点(ul)
print(type(items))      # 类型为PyQuery
print(items)
lis = items.find('li')  # find方法会将所有符合条件的子孙节点选择出来
print(type(lis))
print(lis)
print("--------------------------")
liss = items.children('.active') # children方法只找子节点(这里找class属性值为active的子节点)
print(type(liss))       # PyQuery类型
print(liss)

"""

"""父节点
from pyquery import PyQuery as pq
doc = pq(html)
items = doc('.list')        # 拿到class为list的节点
container = items.parent()  # parent方法拿到直接父类节点
print(type(container))
print(container)
print("--------------------------------")
parents = items.parents('.wrap')   # parents方法拿到class值为wrap的祖先节点，不指定css选择器会返回所有祖先节点
print(type(parents))
print(parents)

"""

"""兄弟节点
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.list .item-0.active')    # 选择class为list的节点内部class属性为item-0和active的节点(第三个li节点)
print(li.siblings())    # siblings方法获取兄弟节点，就其他四个li节点
print(li.siblings('.active'))       # 兄弟节点包含active的节点(第四个li节点)

"""



# 遍历节点
"""
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)       # pyquery库选择结果是多节点时也没有像bs4一样返回列表，单个节点可以直接输出
print(str(li))  # 也可以转换为字符串类型输出
print("----------------------------------")
lis = doc('li').items()     # 调用items方法会生成一个生成器
print(type(lis))
for li in lis:              # 对生成器遍历，逐个得到li节点对象，类型也还为PyQuery
    print(li,type(li))      # 类型为PyQuery就能对其继续查询操作

"""

"""获取属性
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')     # 提取class属性值为item-0和active的节点。该节点内部的a节点
print(a,type(a))
print(a.attr('href'))           # attr方法提取属性值
print(a.attr.href)              # attr属性获取属性值效果与上面相同
print("--------------------")
a = doc('a')
print(a,type(a))
print(a.attr('href'))           # 结果有多个时，调用attr方法只得到第一个节点信息
print(a.attr.href)
print("----------------------")
for item in a.items():          # 需要调用items方法会生成一个生成器，对生成器遍历
    print(item.attr('href'))
"""

"""获取文本
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a)
# 结果：<a href="link3.html"><span class="bold">third item</span></a>
print(a.text())     # text方法忽略节点所有html内容只返回其包裹的内容(结果：third item)
print(a.html())     # html方法获取该节点内部的html文本
# 结果：<span class="bold">third item</span>

print("------------------选中多节点-----------------------")
li = doc('li')
print(li.html())    # html方法返回的是第一个li节点内部的html文本(需要遍历获取)
print(li.text())    # text方法返回所有li节点内部的纯文本内容(text方法不用遍历但是要处理字符串，因为会合并结果到一个字符串用空格分隔)
print(type(li.text()))

print("------------------------")
for item in li.items():     # 需要调用items方法会生成一个生成器，对生成器遍历
    print(item.html())
    
"""



# 节点操作
"""addClass 和 removeClass方法能动态改变节点class属性
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')  # 选中第三个li节点
print(li)
li.removeClass('active')    # removeClass方法移除active这个class属性
print(li)
li.addClass('active')       # addClass方法将这个class属性添加回来
print(li)
"""

"""attr、text和html
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name','link')  # attr方法修改属性，第一个参数属性名，第二个参数属性值
print(li)   
li.html('<span>changed item</span>')    # html方法传入html文本，把li节点内部变成传入的html文本
print(li)
li.text('changed item') # text方法将传入的文本修改为li节点内部的文本内容
print(li)
li.text('<span>changed item</span>')    # 区别与上面html写法，这样写会把html特殊符号给转义的
print(li)   # &lt;span&gt;changed item&lt;/span&gt;

# 如果attr方法只传入第一个参数属性名则表示获取这个属性值，如果传入第二个参数属性值则可以来修改属性值
# text和html方法不传参，表示获取节点内的纯文本和html文本；传入参数表示赋值

"""

"""remove(移除节点，其他操作节点的方法append、empty、prepend)
html = '''
<div class="wrap">
    hello,world
    <p>This is a paragraph.</p>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')     # 这样会把class值为wrap的全部节点内容拿到包括子孙节点
print(wrap.text())      # hello,world This is a paragraph.
print("---------------------------")
wrap.find('p').remove()     # 上面，find方法查询所有子孙节点，查到该节点后remove方法去除子节点
print(wrap.text())

"""



# 伪类选择器
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('li:first-child')      # css3伪类选择器first-child选中文本中第一个li节点
print(li)
li = doc('li:last-child')       # 最后一个li节点
print(li)
li = doc('li:nth-child(2)')     # 第二个li节点
print(li)
print("---------------------------------")
li = doc('li:gt(2)')            # 第三个li之后的li节点
print(li)
li = doc('li:nth-child(2n)')    # 偶数位置的li节点
print(li)
li = doc('li:contains(second)') # 包含second文本的li节点
print(li)


# pyquery官方文档：http://pyquery.readthedocs.io








