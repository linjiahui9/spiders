# -*- codeing = utf-8 -*-
# @Time : 2021/11/25 16:09
# @Author : wujinying
# @File : Ajax爬取pixivic美图.py
# @Software PyCharm

import requests
import json
from urllib.parse import urlencode
import pprint
import xlwt
import os
import logging
from os.path import exists
from os import makedirs

# os.makedirs(r'D://图片')
headers={
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJwZXJtaXNzaW9uTGV2ZWwiOjEsInJlZnJlc2hDb3VudCI6MiwiaXNDaGVja1Bob25lIjowLCJ1c2VySWQiOjI0NzkzMSwiaWF0IjoxNjU4ODg4OTU0LCJleHAiOjE2NTk0MDczNTR9.Qn-PdD4jV0ibmlSj2vVzmi5kTPMHpbYx8XXSu_BvXUx19ddxUTBA-ITREXV4T4TdrYS7SDWsut7Cy-8S3u8x2A',
    'dnt': '1',
    'origin': 'https://pixivic.com',
    'referer': 'https://pixivic.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

# 列表页ajax请求内容
# https://api.bbmang.me/ranks?page=1&date=2022-07-11&mode=day&pageSize=30
INDEX_URL = 'https://api.bbmang.me/ranks?'

# 详情页
# https://api.bbmang.me/artists/604231/illusts/illust?page=1&pageSize=10&maxSanityLevel=3
DETAIL_URL = 'https://api.bbmang.me/artists/{id}/illusts/illust?page=1&pageSize=10&maxSanityLevel=3'
TOTAL_PAGE = 10
RESULTS_DIR = 'pictiures'
exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 获取json数据
def scrape_api(url):
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            print(response.json())
            return response.json()
        logging.error('get invalid status code %s while scraping %s',
                      response.status_code, url)
    except requests.ConnectionError:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 拿到列表页
def get_page(page):
    params = {
        'page': page,
        'date': '2022-07-24',
        'mode': 'day',
        'pageSize': '30'
    }
    url = INDEX_URL + urlencode(params)
    return scrape_api(url)
    # print(url)


# 获取详情页数据
def sccrape_detail(info):
    id = get_id(info)
    url = DETAIL_URL.format(id=id)
    # print(url)
    return scrape_api(url)


def download(result):
    response = result.get('imageUrls')
    print(response)     # 查看链接是否与详情页查看图片的链接一致
    image = scrape_api(response).content
    #  https://api.bbmang.me/artists/None/illusts/illust?page=1&pageSize=10&maxSanityLevel=3
    title = result.get('title')
    titles = f'D://图片/{title}.jpg'
    f = open(titles, 'wb')
    f.write(image)
    f.close()

# 拿到详情页的id
def get_id(info):
    if info:
        items = info.get('data')
        for item in items:
            ArtistId = item.get('artistId')
    return ArtistId

# 解析详情页信息
def get_info(child_info):
    i=0
    data = {}
    datas = []
    if child_info:
        items = child_info.get('data')
        for item in items:
            i+=1
            data['title'] = item.get('title')
            data['imageUrls'] = item['imageUrls'][0]['original']
            data['id'] = item.get('id')
            yield data




def get_images(info):
    i=0
    print(type(info))
    pixivic=[]
    data=[]
    if info:
        items=info.get('data')
        # print(items)
        for item in items:
            i+=1
            title=item.get('title')
            # print(title)
            data.append(title)

            imageUrls=item['imageUrls'][0]['original']
            # print(type(imageUrls))

            id=item['artistPreView']['id']
            # print(id)
            data.append(id)

            url=imageUrls.replace('https://i.pximg.net/','https://o.acgpic.net/')
            # print(url)
            data.append(url)

            download(url,title,i)

        pixivic.append(data)
        print(pixivic)
    return pixivic


def save_info(result):
    title = result.get('title')
    data_path = f'{RESULTS_DIR}/{title}.json'
    json.dump(result, open(data_path, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)


# def save_image(results):
#     title = results.get('title')



'''
    print(type(results))
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet('pixivic',cell_overwrite_ok=True)
    col=("title","id","url")
    for i in range(0,3):
        sheet.write(0,i,col[i])
    for i in range(0,108):
        print("第%d条数据"%(i+1))
        data=results[i]
        for j in range(0,3):
            sheet.write(i+1,j,data[j])
    book.save('info.xls')
'''
def main():
    # for page in range(1,6):
        info = get_page(1)
        child_info = sccrape_detail(info)
        results = get_info(child_info)
        for result in results:
            print(result)
            save_info(result)
            download(result)

        # results = get_images(info)

    # savepath=".\\info.xls"
    # save_info(results,savepath)

if __name__ == '__main__':
    main()

        # for result in results:
        #     print(result)


# https://api.bbmang.me/ranks?page=1&date=2022-07-11&mode=day&pageSize=30
# https://api.bbmang.me/ranks?page=2&date=2022-07-11&mode=day&pageSize=30
# https://api.bbmang.me/ranks?page=3&date=2022-07-11&mode=day&pageSize=30
# https://api.bbmang.me/artists/604231/illusts/illust?page=1&pageSize=10&maxSanityLevel=3
# https://api.bbmang.me/artists/1878082/illusts/illust?page=1&pageSize=10&maxSanityLevel=3
# https://api.bbmang.me/artists/19560796/illusts/illust?page=1&pageSize=10&maxSanityLevel=3

# https://api.bbmang.me/artists/5300811/illusts/illust?page=1&pageSize=10&maxSanityLevel=3
# https://api.bbmang.me/artists/16462721/illusts/illust?page=1&pageSize=10&maxSanityLevel=3

# https://o.acgpic.net/img-original/img/2022/07/23/10/56/46/99928488_p0.jpg
# https://i.pximg.net/img-original/img/2022/07/23/18/00/53/99936203_p0.png

