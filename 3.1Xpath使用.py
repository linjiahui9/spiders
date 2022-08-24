# -*- codeing = utf-8 -*-
# @Time : 2021/11/18 21:55
# @AUTHOR : wujinying
# @File : 3.1Xpath使用.py
# @Software : PyCharm

"""
nodename 选取此节点的所有子节点
/        从当前节点选取直接子节点
//       从当前节点选取子孙节点
.        选取当前节点
..       选取当前节点的父节点
@        选取属性

例如：//title[@lang='eng'] 选中所有名称为title，属性lang的值为eng的节点
# 利用lxml库，利用XPath对HTML解析：pip3 install lxml  py3.10用的是lxml-4.7.1版本的
"""


# 实例引用
"""
from lxml import etree      #导入lxml库的etree模块，用该模块解析能自动修正html文本
# 下面声明一段HTML文本(注意最后的li节点没有闭合)
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)   #调用HTML类对HTML文本初始化(解析html)，这样构造出一个XPath解析对象
result=etree.tostring(html)     #调用tostring()方法可以把修正好的HTML代码(最后的li后面少了</li>,还补全body。html节点)给result,但是结果是bytes类型
print(result.decode('utf-8'))   #利用decode()方法把bytes类型转换成str类型

"""


# 直接读取文本文件进行解析
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())      #parse解析文档，文档内容和上案例一样
result=etree.tostring(html)
print(result.decode('utf-8'))

'''


# 所有节点
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())  
result=html.xpath('//*')    #*代表匹配所有节点，返回形式为列表，每个元素是Element类型，类型其后跟着节点名字
print(result)

'''


# 匹配指定节点，获取所有
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li')    #直接调用xath，使用//后接节点名获取该名称的所有节点
print(result)
print(result[0])    # 拿到其中一个要用中括号索引的方式(列表)

'''


# 子节点
'''获取直接子节点
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li/a')    #追加/a即在所有li节点中找所有直接a的子节点     追加/用于选取直接子节点
print(result)

'''

'''获取子孙节点
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//ul//a')
#追加//a即在所有ul节点中找所有名为a子孙节点     追加//用于选取所有子孙节点，这里用/a会没结果，因为ul没有直接的子节点是a
print(result)   # ul的直接子节点是li，li的直接子节点才是a

'''


# 父节点
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//a[@href="link4.html"]/../@class')
# 选取href属性，属性值为link4.html的a节点，然后在通过..获取其父节点，再@的方式获取其class属性的值
print(result)   # item-1

'''

'''也可以通过parent::来获取父节点
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//a[@href="link4.html"]/parent::*/@class')
# result=html.xpath('//a[@href="link4.html"]/parent::/@class')  #要加*号，不清楚原因
print(result)

'''


# 属性匹配
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]')      #通过这个条件限制所选取li节点的class属性为item-0
print(result)

'''


# 文本获取
'''text方法获取节点中的文本
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li[@class="item-0"]/text()')     # 这里获取的文本为回车符换行符
print(result)   # 上面/text获取li的直接子节点文本内容，这样匹配到的是li节点自动修正的换行符
    
# li的直接子节点都是a节点，想要获取的文本在节点a内部，所以要先加/a获取到直接子节点a，再/text()拿到文本
# result=html.xpath('//li[@class="item-0"]/a/text()')

# 获取li节点中所有的子孙节点的文本，其中可能参杂着一些特殊字符
result=html.xpath('//li[@class="item-0"]//text()')      
print(result)

# <li class="item-0"><a href="link1.html">first item</a></li>
# <li class="item-0"><a href="link5.html">fifth item</a>    系统自动修正li的尾标签时，在</a>后加了换行，所以获取到的是换行符
# </li>

# 如果想获取子孙节点内部的所有文本，可以直接//test()，但会参杂一些特殊符号。
# 想获取某些子孙节点下的所有文本，可以先取到特定的子孙节点，再调用text()获取

'''


# 获取属性
'''
from lxml import etree
html=etree.parse('./test.html',etree.HTMLParser())
result=html.xpath('//li/a/@href')       # 区别与属性匹配，匹配是中括号加属性名和值来限定某个属性，这里是获取节点的某个属性
print(result)

'''


# 属性的多值匹配
"""contains常用于某个节点的某个属性有多个值时使用
from lxml import etree
text='''
<li class="li li-first"><a href="link.html">first item</a></li>
''' 
# li 和 li-first两个属性值
html=etree.HTML(text)
# result=html.xpath('//li[@class="li"]/a/text()')     #li节点里面class有多个属性值，无法直接匹配(=号)
result=html.xpath('//li[contains(@class,"li")]/a/text()')
#通过contains()方法，第一个参数传入属性名称,第二个参数传入属性值(,分隔参数)，只要该属性包含这个属性值就匹配上了
print(result)

"""


# 多属性匹配
"""多属性要用中括号把所有多属性条件选中来筛选
from lxml import etree
text='''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html=etree.HTML(text)
result=html.xpath('//li[contains(@class,"li") and @name="item"]/a/text()')      # 这里是又多值又多属性
#通过contains()方法，第一个参数传入属性名称,第二个参数传入属性值(,分隔参数)，再通过and(xpath运算符还有or等等 p96 )连接匹配多个属性，从而确定节点
print(result)

"""


# 按序选择
""""某些属性能匹配出多个节点，利用中括号传入索引方法获取特定次序节点
from lxml import etree      #导入lxml库的etree模块
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
result=html.xpath('//li[1]/a/text()')               # 选取第一个li节点
print(result)
result=html.xpath('//li[last()]/a/text()')          # 选取最后一个节点last方法
print(result)
result=html.xpath('//li[position()<3]/a/text()')    # 位置小于3的节点，拿到第1和第2个节点
print(result)
result=html.xpath('//li[last()-2]/a/text()')        # 倒数第3个li节点，last最后一个-2就倒数第三
print(result)

"""


# 节点轴选择
# """节点轴的选择方法：获取子元素、兄弟元素、父元素、祖先元素等
from lxml import etree      #导入lxml库的etree模块
# 下面声明一段HTML文本
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html=etree.HTML(text)
result=html.xpath('//li[1]/ancestor::*')        # ancestor轴获取所有祖先节点(包括自动修正的html,body和ul，div)，其后面要跟两个冒号，然后是节点的选择器(这里匹配所有节点)
print(result)                                   # 包含html，body，div，ul所有li的祖先节点
result=html.xpath('//li[1]/ancestor::div')      # 双冒号后加限定div只获取div祖先节点
print(result)
result=html.xpath('//li[1]/attribute::*')       # attribute轴，可以获取所有属性值，后面选择器还是*，获取节点的所有属性
print(result)                                   # 返回值就是li节点的所有属性值
result=html.xpath('//li[1]/child::a[@href="link1.html"]')   # child轴可以获取所有直接子节点，这里选取href属性值为link1.html的a节点
print(result)
result=html.xpath('//li[1]/descendant::span')   # descendant轴，可以获取所有子孙节点，这里限定获取span节点，所以不会包含a节点
print(result)

# result=html.xpath('//li[1]/following::*[2]')
# 可以获取当前节点之后的所有节点，后面加了选择器限定了：限定只获取当前节点后的所有节点中第2个节点(<Element a at 0x1d785ae2b40>)
# result=html.xpath('//li[1]/following::*[1]')     # <Element li at 0x171a1aa2a40>
result=html.xpath('//li[1]/following::*/text()')  # ['second item', 'third item', 'fourth item', 'fifth item', '\n']有一些节点没有text内容，为空，就没有在列表留有位置
# result=html.xpath('//li[1]/following::*')   # [<Element li at 0x1d8fd902ac0>, <Element a at 0x1d8fd902bc0>, <Element li at 0x1d8fd902c00>, <Element a at 0x1d8fd902c80>, <Element li at 0x1d8fd902cc0>, <Element a at 0x1d8fd902d40>, <Element li at 0x1d8fd902d80>, <Element a at 0x1d8fd902dc0>]

print(result)

result=html.xpath('//li[1]/following-sibling::*/a/text()')   #following-sibling可以获取当前节点之后所有同级节点，这里用*匹配获取所有后续同级节点(4个li)
print(result)   # li[2,3,4,5]

# """









