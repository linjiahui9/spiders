# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 0:15
# @AUTHOR : wujinying
# @File : 3.2BeautifulSoup使用.py
# @Software : PyCharm

# 声明变量html，存储HTML字符串，但不完整，有body和html节点没有闭合
'''
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>,
<a href="http://example.com/lacie" class="sister" id="link2"><Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
'''

'''基本用法(4种解析器 p99)
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')     #lxml解析器，需要安装c语言库，有着解析HTML和xml的功能   初始化时BeautifulSoup会自动修正缺失的节点
print(soup.prettify())              #调用prettify方法可以把要解析的字符串以标准缩进的格式输出，也能自动更正html格式
print(soup.title.string)            #输出HTML中title节点的文本内容(string)

'''


# 节点选择器
'''选择元素
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.title)   # 节点及其内容
print(type(soup.title))     #bs4.element.Tag类型
print(soup.title.string)    # 节点的文本内容
print(soup.head)            
print(soup.p)               # 多个相同节点时，这样写只能匹配到出现的第一个节点

# 提取信息   (下面操作都是获取第一个节点的)
print(soup.title.name)  # 选取节点，再利用name属性获取节点名字
print(soup.p.attrs)     # 每个节点可能有多个属性，id和class属性等，可以用attrs获取所有属性，获取的结果返回是字典形式，属性和属性值
print(soup.p.attrs['name'])     #想获取特定属性的属性值，相当于从字典获取某个键值，只需要用中括号加上属性名就可以
print(soup.p['name'])
print(soup.p['class'])          #可以省略attrs直接写节点并传入属性就行
# 注意：attrs的返回值可能为字符串列表，也可能是字符串，取决于属性的属性值是否存在多个，例如节点中的class属性可能存在多个，就返回列表
'''


'''嵌套选择
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)   #可以嵌套，选择玩head节点元素后继续调用head来选取title节点，并输出其内容

'''


# 关联选择
# '''
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

# '''
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.p.contents)      #contents属性可以在选取的节点中获取到它的直接子节点，但是也可以把子孙节点当成它父节点列表的一项，同时写入，例如这里把span孙节点内容归到它父节点a的内容里面去了

'''
'''     ？
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.p.children)      # children属性也能得到相同结果，得到的是生成器类型-
for i,child in enumerate(soup.p.children):  #？
    print(i,child)

'''
'''   ？
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.p.descendants)       # descendants属性拿到所有子孙节点，返回结果还是生成器
for i,child in enumerate(soup.p.descendants):   # 遍历输出：descendants会递归查询所有子节点，得到所有子孙节点 
    print(i,child)

'''


# 父节点和祖先节点
'''
html="""
<html>
<head>
<title>The DOrmouse's story</tilte>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
# print(soup.a.parent)    #选取a节点的直接父节点p，输出p节点及其内部所有内容
print(type(soup.a.parents))     #返回结果是生成器类型
print(list(enumerate(soup.a.parents)))      #用列表的方式输出索引和内容，列表的元素就是所选节点的祖先节点，0是父节点，1是p的父节点body，2是body的父节点html

'''


# 兄弟节点(列表结果显示：同级节点和同级节点包裹的内容分开单独算的)
'''
html="""
<html>
<body>
<p class="story">
    Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class=sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
</p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print('Next Sibling',soup.a.next_sibling)   #next_sibling获取节点的下一个兄弟元素
print('Prev Sibling',soup.a.previous_sibling)   #previous_sibling获取节点的上一个兄弟元素
print('Next Siblings',list(enumerate(soup.a.next_siblings)))    #next_siblings返回后面所有的兄弟节点
print('Prev Siblings',list(enumerate(soup.a.previous_siblings)))    #previous_Siblings返回前面所有的兄弟节点

'''


# 提取信息
'''
html="""
<html>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">Bob</a><a href=
            "http://example.com/lacie" class="sister" id=Link2">Lacie</a>
        </p>
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)      # 兄弟节点的下一个
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))     # 拿到祖先节点
print(list(soup.a.parents)[0])  # 索引为0的祖先节点，看上面
print(list(soup.a.parents)[0].attrs['class'])
# 返回的是单个节点，才可以直接调用string、attrs等属性获取其文本和属性；
# 返回的是多个节点的生成器，则可以转换为列表后取出某个元素，再调用那些属性来获取对应的节点文本和属性

'''


# 方法选择器(返回列表类型)

# find_all(name,attrs,recursive,text,**kwargs)    查询所有符合条件的元素。再传入一些属性或文本，就可以得到符合条件的元素，返回值为列表
# (1)name
"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))     # 传入name参数，值为ul，查询所有ul节点，返回结果是 列表类型，长度为2
print(type(soup.find_all(name='ul')[0]))    # 每个元素依然是bs4.element.Tag类型
print("------------------------------------------")
for ul in soup.find_all(name='ul'):         # 因为是Tag类型所有嵌套查询，查询ul节点内部的li节点
    print(ul.find_all(name='li'))           # 返回的还是Tag类型
    for li in ul.find_all(name='li'):       # tag类型可以继续嵌套查询下去
        print(li.string)                    # 提取li节点内容

"""

# attrs 传入属性查询(传入字典类型，返回列表)
"""
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={'id':'list-1'}))     # 传入参数是attrs，参数类型是 字典类型，查询id为list-1的节点，得到返回值是，列表形式内容包含其所有节点
print(soup.find_all(attrs={'name':'elements'})) # 结果上面相同(属性拿到一样的ul)
print(soup.find_all(id='list-1'))       # 对于常用属性，例如id和class等，可以不用attrs传递，这里的id没有引号
print(soup.find_all(class_='element'))  # class是py的关键字所以要class_

"""


# text 匹配节点文本，传入形式可以是字符串，也可以是正则表达式对象
"""
import re
html='''
<div class="panel">
    <div class="panel_body">
        <a>Hello,this is a link</a>
        <a>Hello,this is a link,too</a>
    </div>
</div>
'''
from bs4 import BeautifulSoup
import re
pattern = re.compile('link',re.S);  # 注意匹配换行符操作要在表达式对象那写
result = re.findall(pattern,html)
print(result[1])    # link
print("------------------------")
soup=BeautifulSoup(html,'lxml')
print(soup.find_all(text=re.compile('link')))   # 两个a节点，其文本都包含link，用find_all方法传入text参数，该参数值为正则表达式对象，返回结果为列表

"""


# find() 返回单个元素，也就是第一个匹配到的元素
"""
html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.find(name='ul'))         # 返回值不为列表，为第一个ul节点的所有内容，类型仍为tag
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

"""


# p111有其他查询方法


# CSS选择器    select()方法，传入相关的CSS选择器即可(属性值)
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
"""
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
print(soup.select('.panel .panel-heading'))     # 返回值结果均为css选择器的节点组成列表
print(soup.select('.panel #list-2'))            # 拿到class为panel的节点下id为list-2的所有节点(自己和子孙节点)
print("-------------------------------")
print(soup.select('ul li'))     #选择所有ul节点下面的所有li节点，结果是所有li节点组成的列表
print(soup.select('#list-2 .element'))      # 选择id为list-2下，class为element的所有节点
print(type(soup.select('ul')[0]))       # 输出列表元素类型，Tag
print(soup.select('ul')[0])                 # 拿到ul节点所有内容包含子孙节点的

"""


# 获取节点属性
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):    # 获取每个ul节点
    print(ul['id'])
    print(ul.attrs['id'])       # 直接将属性名传入中括号和通过attrs属性传入属性查询属性值效果一样

'''


# 获取文本
'''
from bs4 import BeautifulSoup
soup=BeautifulSoup(html,'lxml')
for li in soup.select('li'):            # 循环获取列表中每个li节点
    print('Get Text:',li.get_text())    # get_text()获取节点文本，或者string，效果相同
    print('String:',li.string)
'''

# 总结p113





