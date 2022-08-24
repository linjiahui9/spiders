# -*- codeing = utf-8 -*-
# @Time : 2022/7/14 14:00
# @Author : wujinying
# @File : 5.3Ajax分析与实战
# @Software PyCharm

# Ajax + MongoDB 存储方式：https://github.com/Python3WebSpider/ScrapeSpa1/blob/master/spider2.py

import requests
import logging
import json
from os import makedirs
from os.path import exists

# 定义logging的基本配置
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 列表页ajax请求的内容：去到newwork看到xhr的包，看它的请求网址(Request URL)   预留limit和offset作为占位符
INDEX_URL = 'https://spa1.scrape.center/api/movie/?limit={limit}&offset={offset}'
# 详情页ajax请求的数据：能发现列表页预览数据中有id，详情页数据预览也有id，刚好id顺序对应每一个详情页的数据
DETAIL_URL = 'https://spa1.scrape.center/api/movie/{id}'
LIMIT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)


def scrape_api(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()          # 判断状态码为200就解析相应内容为json字符串
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 爬取列表页数据
def scrape_index(page):
    url = INDEX_URL.format(limit=LIMIT, offset=LIMIT * (page - 1))  # 字符串的format方法传入limit和offset的值
    return scrape_api(url)      # 传入完整url       例如第一页10 ，0，第二页10，10，第三页10，20
    # 这里用不着解析数据，因为这里拿到的就是异步加载的数据

# 爬取详情页的数据
def scrape_detail(id):
    url = DETAIL_URL.format(id=id)
    return scrape_api(url)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)


def main():
    for page in range(1, TOTAL_PAGE + 1):       # 1到10
        index_data = scrape_index(page)         # 循环拿到详情页的数据
        for item in index_data.get('results'):  # 循环，get方法传入键名(results)拿键值，这样即使键名不存在，也不会报错，而返回None
            id = item.get('id')                 # 看4数据存储
            detail_data = scrape_detail(id)     # 拿到详情页数据
            logging.info('detail data %s', detail_data)
            save_data(detail_data)


if __name__ == '__main__':
    main()

