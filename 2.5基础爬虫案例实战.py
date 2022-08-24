# -*- codeing = utf-8 -*-
# @Time : 2022/7/4 19:46
# @Author : wujinying
# @File : 基础爬虫案例实战
# @Software PyCharm

'''目标链接：https://ssr1.scrape.center/

1.要爬取电影详情页就要观察每个电影怎么进去详情页面f12点左上角箭头移动到电影标题
    发现在a标签中有href进入详情页(/detail/1)

2.要爬取所有电影，有多页，移到下面列表页选择页面中选中发现在li标签中class属性为number active
    的a标签又有href进入分页的(/page/2)

3.爬取详情页内容分析：封面img节点其class属性为cover、名称h2节点、
类别span节点，span节点外侧时button节点，在外侧是class为categories的div节点、
上映时间是span节点，外侧是class为info的div节点，另外提取结果还多了"上映"二字，用正则提取日期、
评分是p节点，节点属性为score、剧情简介是p节点，其外侧是class为drama的div节点

'''
import json
from os.path import exists
from os import makedirs

import requests
import logging  # logging库输出信息
import re
from urllib.parse import urljoin    # urljoin模块来做url的拼接

import multiprocessing  # 线程池

# 定义日志输出级别和输出格式
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
BASE_URL = 'https://ssr1.scrape.center' # 当前站点的根url
TOTAL_PAGE = 10     # 要爬取的总页数

RESULTS_DIR = 'results'     # 定义保持数据的文件夹results_dir
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)    # 判断该文件夹是否存在，不存在就创建一个

# 爬取页面
def scrape_page(url):
    logging.info('scraping %s...',url)
    try:
        response = requests.get(url)        # get方法请求
        if response.status_code == 200:     # 状态码200就返回爬取网页内容，不是就输出错误日志信息
            return response.text
        logging.error('get invalid status code %s while scraping %s',response.status_code,url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s',url,exc_info=True)
        # 把logging库中error方法的exc_info参数设置为True，可以打印出Traceback错误栈信息

# 爬取列表页(拼接连接)
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)

# 拿到一页详情页的全部电影的完整url
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">')
    items = re.findall(pattern,html)    # 正则表达式提取href内容
    if not items:   # 如果为空，则返回空列表
        return []
    for item in items:  # 不是空就遍历
        detail_url = urljoin(BASE_URL,item)     # 借助urljoin拼接列表(根)url和获取的href，获取完整详情页的url
        logging.info('get detail url %s',detail_url)
        yield detail_url    # 拿到完整url后调用yield返回url(类似return，但是yield函数在下一次迭代时，从上一次迭代遇到的yield后面的代码(下一行)开始执行)
        # 就是这次循环拿到一次完整url返回，在拿到循环到的下一条完整url也继续返回

# 爬取详情页
def scrape_detail(url):
    return scrape_page(url)     # 直接复用爬取页面方法

# 解析详情页(以字典的形式返回数据)
def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?class="cover">', re.S)

    name_pattern = re.compile('<h2.*?>(.*?)</h2>')

    categories_pattern = re.compile('<button.*?category.*?<span>(.*?)</span>.*?</button>', re.S)

    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')

    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)

    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)

    cover = re.search(cover_pattern, html).group(1).strip() if re.\
        search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.\
        search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.\
        findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) if re.\
        search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.\
        search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()) if re.\
        search(score_pattern, html) else None
    return {
        'cover': cover,
        'name': name,
        'categories': categories,
        'published at': published_at,
        'drama': drama,
        'score': score
    }


# 保存数据
def save_data(data):
    name = data.get('name')     # 拿到解析数据中name字段
    data_path = f'{RESULTS_DIR}/{name}.json'    # 构建json文件路径
    json.dump(data, open(data_path, 'w', encoding='utf-8'),ensure_ascii=False,indent=2)
    # dump方法两个参数：ensure_ascii=False保证中文不乱码，另一个indent设置保持json数据结构有两行缩进


# 主方法
def main(page):
    # for page in range(1,TOTAL_PAGE + 1):            # 从第一页开始，到11页
        index_html = scrape_index(page)             # 拼接链接
        detail_urls = parse_index(index_html)        # 传入列表页链接，拿到全部详情页链接
        # logging.info('detail urls %s',list(detail_urls))     # 每一页都输出一遍获取到该页的全部详情页链接

        for detail_url in detail_urls:
            detail_html = scrape_detail(detail_url)     # 拿到循环的详情页链接爬取子页面
            data = parse_detail(detail_html)            # 拿到详情页面去解析数据
            logging.info('get detail data %s',data)
            logging.info('saving data to json file')
            save_data(data)                             # 保存为json文件
            logging.info('data saved successfully!')



if __name__ == '__main__':
    pool = multiprocessing.Pool()       # 看看线程池这么用吧？
    pages = range(1, TOTAL_PAGE + 1)    # ？
    pool.map(main,pages)                # ？
    pool.close()
    pool.join()

# https://github.com/Python3WebSpider/ScrapeSsr1/blob/master/spider2.py
# https://github.com/Python3WebSpider/ScrapeSsr1/blob/master/spider.py
# spider.py版本是用PyQuery+MongoDB+多线程

