# -*- codeing = utf-8 -*-
# @Time : 2022/7/9 22:12
# @Author : wujinying
# @File : 4.数据存储
# @Software PyCharm

# txt文本存储
"""
import requests
from pyquery import PyQuery as pq
import re

url = 'https://static1.scrape.center/'
html = requests.get(url).text       # requests.get拿到网页源码，再text转成字符串
doc = pq(html)
items = doc('.el-card').items()     # 拿到class属性值为el-card的所有节点(拿到每一个完整电影的div)，调用items方法会生成一个生成器

file = open('movies.txt', 'w', encoding='utf-8')
for item in items:  # # 对生成器遍历，逐个得到div节点对象，类型也还为PyQuery，类型为PyQuery就能对其继续查询操作
    # 名称
    # name = item.find('a > h2').text()   # find方法查询所有子孙节点(书上写的版本应该是a节点下的h2节点？)
    name = item.find('.m-b-sm').text()   # find方法查询所有子孙节点
    file.write(f'名称: {name}\n')
    # 类别(有多个值用列表)
    categories = [item.text()
                  for item in item.find('.categories button span').items()] # 看3.3第67行，还有这for循环上面回事
    file.write(f'类别: {categories}\n')
    # 上映时间
    published_at = item.find('.info:contains(上映)').text()   # 包含"上映"文本的class属性值为info的节点(3.3最后)
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('\d{4}-\d{2}-\d{2}', published_at) else None  # 2.3第25行
    file.write(f'上映时间: {published_at}\n')
    # 评分
    # score = item.find('p.score').text()   # 书上写法
    score = item.find('.score').text()      # 直接找class属性值就行了，score这个属性值唯一
    file.write(f'评分: {score}\n')
    file.write(f'{"=" * 50}\n')
file.close()

# with open('movies.txt', 'w', encoding='utf-8'):
#     file.write(f'名称: {name}\n')
#     file.write(f'类别: {categories}\n')
#     file.write(f'上映时间: {published_at}\n')
#     file.write(f'评分: {score}\n')
# with as 写法with控制语句结束后文件会自动关闭，不用调用close方法

"""



# json文件存储
'''
js语言中一切皆为对象，因此任何数据都能通过json表示，
对象在js中是指用花括号包围的内容，{key:value}键值对结构，key只能用整型和字符串，value随意
数组在js中用中括号包围的内容，有索引，也可以像对象那样使用键值对结构，但是索引结构用的多
'''
"""读取json
import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''     # 数组中的元素是对象(json的数据要用双引号包裹，单引号用loads方法会解析json失败)
print(type(str))
data = json.loads(str)  # loads方法将字符串转换成json对象，由于最外层是中括号，所以最终的数据类型是列表
print(data)
print(type(data))

print("----------------------")
print(data[0]['name'])         # 中括号加索引得到第一个字典元素，在用键名拿到对应值
print(data[0].get('name'))     # 推荐get方法传入键名拿键值，这样即使键名不存在，也不会报错，而返回None
print(data[0].get('name',18))  # 第二个参数为默认值，不存在时返回

print('-----------读取json文件，并解析--------------')
with open('data.json',encoding='utf-8') as file:    # open方法打开文件，并将文件操作对象赋给file
    str = file.read()   # read方法读取文件中全部内容
    data = json.loads(str)
    print(type(data))

print("-----load方法传入文件操作对象，能直接将文本转换为json对象---------")
data = json.load(open('data.json',encoding='utf-8'))
print(type(data))

# """

"""输出json
import json

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
print(type(data))       # list类型的json对象
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data))    # dumps方法将json对象转为字符串，在用write方法将字符串写入文件

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2))  # indent参数是保留json格式的缩进格数(dumps方法会把单引号转成双引号，写入的文件内容都是双引号的)

"""
"""
import json
# json对象中包含中文字符
data = [{
    'name': ' 王伟 ',
    'gender': ' 男 ',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2))
    
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))  # 需要指定第三个参数ensure_ascii的值为False(文件输出编码一定要定)
    
print("------dump方法可以直接将json对象全部写入文件中，类比loads与loads方法--------")
json.dump(data, open('data.json', 'w', encoding='utf-8'), indent=2, ensure_ascii=False)

"""



# csv文件存储
"""写入csv
import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)            # 调用csv库的writer方法初始化写入对象
    # writer = csv.writer(csvfile,delimiter=' ')            # delimiter参数修改默认分隔符
    writer.writerow(['id', 'name', 'age'])  # 调用writerow方法传入每一行数据
    writer.writerow(['10001', 'Mike', 20])  # 写入的csv的文本默认以逗号分隔每条记录 
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])    # writerows方法可以同时写入多行，需要传入二维列表
    writer.writerows([['10001', 'Mike', 20], ['10002', 'Bob', 22], ['10003', 'Jordan', 21]])
    
"""
"""字典的写入方式
import csv
# 爬取的数据是结构化数据时，一般会用字典表示这种数据类型
with open('data.csv', 'a',encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']  # 定义三个字段(类似数据库的字段)
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames) # DictWriter方法初始化字典对象
    writer.writeheader()                # writeheader方法写入头信息后再用writerow写入数据(写入的数据会根据键名对应字段名存储)
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})
    writer.writerow({'id': '10004', 'name': '李四', 'age': 18})   # 中文记得指定encoding

"""
"""
import pandas as pd

data = [
    {'id': '10001', 'name': 'Mike', 'age': 20},
    {'id': '10002', 'name': 'Bob', 'age': 22},
    {'id': '10003', 'name': 'Jordan', 'age': 21},
]
df = pd.DataFrame(data)             # 用pandas库中的DataFrame方法创建一个对象，传入列表
df.to_csv('data.csv', index=False)  # to_csv方法可以将数据写入 csv文件
"""

"""读取csv
import csv

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)    # 构建reader对象，再遍历文件 每一行 内容(一行一个列表)
    for row in reader:
        print(type(row))
        
"""
# '''
import pandas as pd

df = pd.read_csv('data.csv')    # pandas库中的read_csv方法构建读取对象
print(type(df))
data = df.values.tolist()       # 调用values属性，再调用tolist方法即可把数据转成列表形式
print(type(data))
print(data)

for index, row in df.iterrows():    # 对列表进行遍历也能得到列表类型结果         iterrows?
    print(row.tolist())

# '''




