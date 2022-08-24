# -*- codeing = utf-8 -*-
# @Time : 2022/7/31 15:18
# @Author : wujinying
# @File : GitHub爬取实战
# @Software PyCharm


import requests
from pyquery import PyQuery as pq


class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        ## 维持会话，自动处理cookies
        self.session = requests.Session()

    ## 解析出登录所需要的
    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = pq(response.text)
        token = selector('input[name="authenticity_token"]').attr('value')
        return token

    def login(self, email, password):
        # print(self.token())
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        response = self.session.get(self.feed_url, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
            # print(response.text)
        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            self.profile(response.text)

    ## 关注人的动态信息
    def dynamics(self, html):
        selector = pq(html)
        # print(selector.text())
        dynamics = selector('div[class="d-flex flex-items-baseline"] div')
        dynamics.find('span').remove()
        # print(dynamics.text())
        for item in dynamics.items():
            dynamic = item.text().strip()
            print(dynamic)

    ## 详情页面
    def profile(self, html):
        selector = pq(html)
        # print(selector.text())
        name = selector('input[id="user_profile_name"]').attr('value')
        email = selector('select[id="user_profile_email"] option[selected="selected"]').text()
        print(name, email)

"""邮件验证有422的情况，偶尔可以正常浏览。

import requests
from lxml import etree

class Login(object):
	# 初始化函数
  def __init__(self):
  	# 设置http协议header头信息
    self.headers = {
      'Referer': 'https://github.com/',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
      'Host': 'github.com'
    }
    # 设置登录的url地址
    self.login_url = 'https://github.com/login'
    # 设置session的url地址
    self.post_url = 'https://github.com/session'
    # 设置profile的url地址
    self.logined_url = 'https://github.com/settings/profile'
    # 从请求中获取session
    self.session = requests.Session()
    # 设置email验证的url地址
    self.email_url = 'https://github.com/sessions/verified-device'
  
  def token(self):
  	# session的get函数获取响应
    response = self.session.get(self.login_url, headers=self.headers)
    ## 将响应文件保存到本地
    fhandle = open("./github_xpath.html","wb")
    fhandle.write(response.text.encode('utf-8'))
    fhandle.close()
    ## 获取选择器
    selector = etree.HTML(response.text)
    #print(response.text)
    #xpath在线工具正常，lxml解析为空
    #token = selector.xpath('//div//input[2]/@value')
    # 使用选择器获取响应的token
    token = selector.xpath('//div//input[1]/@value')
    print(token)
    return token
  
  def login(self, email, password):
    #print(self.token())
    # post传递的数据
    post_data = {
      'commit': 'Sign in',
      'utf8': '✓',
      'authenticity_token': self.token()[0],
      'login': email,
      'password': password,
      'trusted_device': '',
      'webauthn-support': 'supported',
      'webauthn-iuvpaa-support': 'unsupported'
    }
    ## session的post函数获取响应
    response = self.session.post(self.post_url, data=post_data, headers=self.headers)
    if response.status_code == 200:
      print(response.url)
      self.dynamics(response.text)
    ## session的get函数获取响应
    response = self.session.get(self.logined_url, headers=self.headers)
    if response.status_code == 200:
      self.profile(response.text)

  def dynamics(self, html):
    fhandle = open("./github_xpath_dynamics.html","wb")
    fhandle.write(html.encode('utf-8'))
    fhandle.close()
    opt = input("请输入邮箱验证码")
    post_data = {
      'authenticity_token': self.token()[0],
      'opt': opt
    }
    response = self.session.post(self.logined_url, data=post_data)
    print(response.status_code)
    if response.status_code == 200:
      html = response.text
      #fhandle = open("./github_xpath_422.html","wb")
      #fhandle.write(html.encode('utf-8'))
      #fhandle.close()
      selector = etree.HTML(html)
      dynamics = selector.xpath('//div[contains(@class, "news")]//div[contains(@class, "alert")]')
      for item in dynamics:
        dynamic = ' '.join(item.xpath('.//div[@class="title"]//text()')).strip()
        print(dynamic)
    elif response.status_code == 422:
      fhandle = open("./github_xpath_422.html","wb")
      fhandle.write(html.encode('utf-8'))
      fhandle.close()
      
  def profile(self, html):
    fhandle = open("./github_xpath_profile.html","wb")
    fhandle.write(html.encode('utf-8'))
    fhandle.close()
    selector = etree.HTML(html)
    name = selector.xpath('//input[@id="user_profile_name"]/@value')
    email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')
    print(name, email)

if __name__ == "__main__":
  login = Login()
  login.login(email='email', password='password')
  
"""

"""xpath版本

import requests, re
from lxml import etree
class Login(object):
    def __init__(self):
        self.headers = {
            'Referer': 'https://github.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'Host': 'github.com'
        }
        self.login_url = 'https://github.com/login'
        self.post_url = 'https://github.com/session'
        self.feed_url = 'https://github.com/dashboard-feed'
        self.logined_url = 'https://github.com/settings/profile'
        self.session = requests.Session()

    def dynamics(self, html):
        print('*'*10+'dynamicing'+'*'*10)
        selector = etree.HTML(html)
        # print("*"*20, etree.tostring(selector).decode('utf-8'))
        # print(selector.xpath('//div[@class="d-flex flex-items-baseline"]'))
        dynamics = selector.xpath('//div[@class="d-flex flex-items-baseline"]//div')
        # print(dynamics)
        for item in dynamics:
            etree.strip_elements(item, 'span')
            dynamic = ' '.join(item.xpath('.//text()')).replace('\n', ' ').strip()
            dynamic = re.sub(' +', '  ', dynamic)
            print(dynamic)
        print('*' * 10 + 'dynamic end' + '*' * 10)

    def profile(self, html):
        print('*'*10+'profileing'+'*'*10)
        selector = etree.HTML(html)
        name = selector.xpath('//input[@id="user_profile_name"]/@value')[0]
        email = selector.xpath('//select[@id="user_profile_email"]/option[@value!=""]/text()')[0]
        print(name, email)

    def token(self):
        response = self.session.get(self.login_url, headers=self.headers)
        selector = etree.HTML(response.text)
        token = selector.xpath('//div//input[2]/@value')[0]
        return token

    def login(self, email, password):
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': self.token(),
            'login': email,
            'password': password
        }
        response = self.session.post(self.post_url, data=post_data, headers=self.headers)
        response = self.session.get(self.feed_url, headers=self.headers)
        if response.status_code == 200:
            self.dynamics(response.text)
            # print('response.text', response.text)

        response = self.session.get(self.logined_url, headers=self.headers)
        if response.status_code == 200:
            # print(response.text)
            self.profile(response.text)

if __name__ == '__main__':
    login = Login()
    login.login(email='email', password='password')


"""

