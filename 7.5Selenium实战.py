# -*- codeing = utf-8 -*-
# @Time : 2022/7/30 9:51
# @Author : wujinying
# @File : 7.5Selenium实战
# @Software PyCharm

# 列表页ajax接口url：https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=MzA5NjE0NmQwY2JiNTRjN2VjYjFmN2VjODU1MzRiOGQ4MmYwMjA0YSwxNjU5MTQ2NjM2
# 详情页ajax接口url：https://spa2.scrape.center/api/movie/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx/?token=Y2I4ZGZhODM2YTdkNTRmMjA3NDMxOGE3OTE5YjU5Y2UxZTQ0NzEwNywxNjU5MTQ2NjQw
# 详情页url：https://spa2.scrape.center/detail/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx
# 接口中的token字段每次请求都会改变，这个字段是Base64编码加密而得，detail也是

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists
import json

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s')

INDEX_URL = 'https://spa2.scrape.center/page/{page}'
TIMEOUT = 10
TOTAL_PAGE = 10
RESULTS_DIR = 'results'

exists(RESULTS_DIR) or makedirs(RESULTS_DIR)

# 添加反屏蔽
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--headless')              # 无头模式

browser = webdriver.Chrome(options=options)     # 初始化一个browser对象驱动浏览器模拟动作
wait = WebDriverWait(browser, TIMEOUT)          # 显示等待(这种方式会指定要查找的节点和最长等待时间，如果在规定的时间内找到该节点就返回，找不到抛出 时间异常)

# 通用爬取方法，可对任意url爬取、监听、异常处理(页面加载完后用browser对象可进一步获取信息)
# 使用condition(页面加载成功判断条件)传入参数调用WebDriverWait对象的until方法传入等待条件，返回参数指定的节点
def scrape_page(url, condition, locator):
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)

# 直接使用visibility_of_all_elements_located判断条件加上css选择器，判断页面有没有加载成功，配合上面
def scrape_index(page):
    url = INDEX_URL.format(page=page)
    # 7.1的p207，注意：判断条件可以是Expected_Conditions中的某一项，如visibility_of_all_elements_located、visibility_of_element_located等；locator为定位器是Expected_Conditions的参数
    scrape_page(url, condition=EC.visibility_of_all_elements_located,
                locator=(By.CSS_SELECTOR, '#index .item'))

# 获取详情页url
def parse_index():
    elements = browser.find_elements_by_css_selector('#index .item .name')  # 浏览器ctrl+f 扔进css选择器搜索框，得到后半段url对比手动点进去详情页的url
    for element in elements:
        href = element.get_attribute('href')    # 遍历当前详情页所有url，get_attributeff传入属性名就拿到该节点的属性值
        yield urljoin(INDEX_URL, href)      # p42拼接url

# 爬取详情页
def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_element_located,        # visibility_of_element_located传入的判断条件是判断单个元素出现即可(h2节点，即电影名称节点)
                locator=(By.TAG_NAME, 'h2'))

# 解析详情页
def parse_detail():
    url = browser.current_url
    name = browser.find_element_by_tag_name('h2').text
    categories = [element.text for element in browser.find_elements_by_css_selector('.categories button span')]     # css选择器提取后多个类别节点，然后遍历这些节点，循环遍历后，再调用text属性获取其内部的文本
    cover = browser.find_element_by_css_selector('.cover').get_attribute('src')     # css选择器后，再用get_attributeff传入属性名就拿到该节点的属性值
    score = browser.find_element_by_class_name('score').text                        # 注意这个find_element_by_name()根据class值获取，这里指定是class值，不用写.号
    drama = browser.find_element_by_css_selector('.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }

# 数据存储(原理与2.5相同)
def save_data(data):
    name = data.get('name')
    data_path = f'{RESULTS_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    # dump方法两个参数：ensure_ascii=False保证中文不乱码，另一个indent设置保持json数据结构有两行缩进


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)                                  # 获取列表页
            detail_urls = parse_index()                         # 每次方法循环都返回一次详情页的url
            for detail_url in list(detail_urls):
                logging.info('get detail url %s', detail_url)
                scrape_detail(detail_url)                       # 爬取详情页
                detail_data = parse_detail()                    # 解析详情页
                logging.info('detail data %s', detail_data)
                save_data(detail_data)
    finally:
        browser.close()


if __name__ == '__main__':
    main()
