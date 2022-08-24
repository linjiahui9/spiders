# -*- codeing = utf-8 -*-
# @Time : 2021/11/18 17:07
# @AUTHOR : wujinying
# @File : 爬取猫眼电影排行.py
# @Software : PyCharm

import re
import requests
# 获取网页源代码
def get_one_page(url):
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
    }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

# 解析网页，正则提取
'''
<dd>
                        <i class="board-index board-index-11">11</i>
    <a href="/films/416" title="盗梦空间" class="image-link" data-act="boarditem-click" data-val="{movieId:416}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/moviemachine/c2496a7290a72eac6081321898c347693550574.jpg@160w_220h_1e_1c" alt="盗梦空间" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/416" title="盗梦空间" data-act="boarditem-click" data-val="{movieId:416}">盗梦空间</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,渡边谦,约瑟夫·高登-莱维特
        </p>
<p class="releasetime">上映时间：2010-09-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
'''
def parse_one_page(html):
    pattern=re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S
    )
    items=re.findall(pattern,html)
    print(items)

def main():
    url='http://maoyan.com/board/4'
    html=get_one_page(url)
    # 在network监听中找到数据包，选Response或者Preview查看网页源码，Elements上的可能经过js处理过的和网页源代码不一样
    # print(html)

if __name__ == '__main__':
    main();