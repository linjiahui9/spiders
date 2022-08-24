# -*- codeing = utf-8 -*-
# @Time : 2021/11/25 14:37
# @Author : wujinying
# @File : 5.2Ajax数据爬取.py
# @Software PyCharm

# Ajax有特殊的请求类型，叫xhr，开发者工具直接选取Fetch/XHR

# 打开https://m.weibo.cn/u/2830678474,查看Network找到类型为xhr的包，在Request Headers中能发现一个信息是X-Requested-With: XMLHttpRequest，这个就是Ajax请求

# 在这个包中Preview能看见响应内容json格式，里面返回的结果有个人信息，Response查看真实的返回数据

# 滑动网页让网页加载，拿出一个名字相似多的包，查看Request URL发现能有相同的参数：type，value，containerid，page，能发现其中containerid的参数就是107603加上用户的id

# 在Preview中查看data其实有两个关键信息，cardlistInfo和cards，前者有包括一个total信息是微博的总数目，可以用这个估计页面数，后者是一个列表，包含10个元素
# 展开cards可以发现attitudes_count点赞数，comment_count评论数目，reposts_count转发数目，created_at发布时间,text微博正文
# 请求一次这个接口就可以获取10条微博改变，有10条cards

# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1005052830678474
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&since_id=4774091682746723
# https://m.weibo.cn/api/container/getIndex?type=uid&value=2830678474&containerid=1076032830678474&since_id=4769670743984120

# 爬取前10页微博
from urllib.parse import urlencode
import requests
base_url='https://m.weibo.cn/api/container/getIndex?'

headers={
    # 'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(page):
    params={
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474'
        # 'page': page
    }
    url=base_url+urlencode(params)
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            # print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

# base_url加上利用urlencode()方法将params构造参数字典转换为URL的GET请求参数，判断响应状态码，200直接解析成json返回

from pyquery import PyQuery as pq
def parse_page(json):
    if json:
        items=json.get('data').get('cards')     # 提取json中data节点的cards
        for item in items:                      # 遍历cards
            item=item.get('mblog')             # 再从item获取到mblog节点里面的信息
            # print(item)
            weibo={}
            weibo['id']=item.get('id')          # 把对应的信息赋值于新的字典返回
            weibo['text']=pq(item.get('text')).text()   # 利用pyquery库的pq方法把text的html标签去掉，后再.text()获取文本
            # weibo['text']=item.get('text')
            weibo['attitudes']=item.get('attitudes_count')
            weibo['comments']=item.get('comments_count')
            weibo['reposts']=item.get('reposts_count')
            yield weibo
'''保存再MongoDB上
from pymongo import MongoClient
client=MongoClient()
db=client['weibo']
collection=db['weibo']

def save_to_mongo(result):
    if collection.insert(result):
        print('Save to Mongo')
'''
if __name__ == '__main__':
    for page in range(1,11):
        json=get_page(page)
        results=parse_page(json)
        for result in results:
            print(result)

# 完善地方，页码的动态计算，微博查看全文等...






