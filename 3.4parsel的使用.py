# -*- codeing = utf-8 -*-
# @Time : 2022/7/6 14:45
# @Author : wujinying
# @File : 3.4parsel的使用
# @Software PyCharm

# 安装parsel库：pip3 install parsel

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

# 初始化
"""
from parsel import Selector
selector = Selector(text=html)      # 创建一个Selector对象，向其传入text参数
items = selector.css('.item-0')     # 拿到Selector对象用css选择器进行节点提取
print(len(items),type(items),items) # 提取的是第1、3、5个li节点
items2 = selector.xpath('//li[contains(@class,"item-0")]')  # Xpath方法和之前的用法一样
print(len(items2),type(items),items2)   # 拿到的类型是SelectorList对象，可迭代对象

# 拿到的都是1、3、5li节点内容，为啥有写不一样？p125

"""

# 'parsel.selector.SelectorList'这对象完整写法



# 提取文本
"""
from parsel import Selector
selector = Selector(text=html)
items = selector.css('.item-0')     # 拿到class为item-0的节点(结果是个集合)
for item in items:      
    text = item.xpath('.//text()').get()    # 这里拿到的对象还是SelectorList类型对象可以用css或xpath提取内容
    # //text()直接拿li节点的子孙节点所有内容，SelectorList类型对象有get方法可以将SelectorList包含的Selector对象中的内容提取出来
    print(text)         # get方法从SelectorList里面提取第一个Selector对象结果

print("-------------------------------")

# result = selector.xpath('//li[contains(@class,"item-0")]//text()').get()
result = selector.xpath('//li[contains(@class,"item-0")]//text()').getall()
print(result)   # 用getall就能拿到所有Selector返回的结果，用列表存储
result = selector.css('.item-0 *::text').getall()       # 效果同上，这里*提取所有子节点(包括纯文本节点)，提取文本要加上::text
print(result)

print("-----------------cs---------------------")
result = selector.css('.item-0.active ::text').get()        # 要留空格emm...
print(result)
results = selector.css('.item-0.active')
# result = results.xpath('.//text()').get()                 # 同上
result = results.css('::text').get()                        # 同上
print(result)

"""



# 提取属性
"""
from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0.active a::attr(href)').get()     # css选择器提取属性要加::attr()方法传入对应的属性名
print(result)
result = selector.xpath('//li[contains(@class,"item-0") and contains(@class, "active")]/a/@href').get()
print(result)           # 对于xpath直接用/@再加属性名称即可选取，拿到的都是第三个li节点下的a节点href属性值

"""



# 正则提取
from parsel import Selector
selector = Selector(text=html)
result = selector.css('.item-0').re('link.*')   # css选择器拿到的是集合，正则re再匹配剩下的结果也是集合
print(result)

print('--------------------------')
result = selector.css('.item-0 *::text').re('.*item')
print(result)

result = selector.css('.item-0').re_first('<span class="bold">(.*?)</span>')
# css拿到的是集合，re_first拿到的不是了，是单个结果，re拿到的是多个结果
print(result)


# 官方文档：https://parsel.readthedocs.io/























