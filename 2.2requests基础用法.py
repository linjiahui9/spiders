# -*- codeing = utf-8 -*-
# @Time : 2021/11/18 14:44
# @AUTHOR : wujinying
# @File : 2.2requests基础用法.py
# @Software : PyCharm

# 基础
'''
import requests
r=requests.get('https://baidu.com/')    # 通过get()方法实现与urlopen()相同的操作，得到一个Response对象r
print(type(r))  # Response对象的类型
print(r.status_code)    #对象的状态码
print(type(r.text))     #对象的响应体类型是字符串str
print(r.text)           # 相应内容
print(r.cookies)        #对象Cookies的类型

'''

# Get请求
import requests

'''
import requests
data = {
    'name':'germey',
    'age':22
}
r =requests.get("http://httpbin.org/get",params=data)   #get请求添加信息，一般以字典方式存储，利用params参数
print(r.text)   #网页返回的类型是str类型，json格式
print(r.json()) #调用json方法，解析结果得到字典格式，将返回结果是json格式的字符串转换成字典，不是json格式的话用后会出错
print(type(r.json()))

'''

'''抓取网页
import requests
import re
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore",headers=headers)   # 添加请求头，利用get方法中的headers参数，这里添加了上面User-Agent字段信息
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)     #findall第一个参数填匹配表达式，第二个是要被匹配的内容
print(titles)

'''
'''
import requests
import re
r = requests.get('https://ssr1.scrape.center/')
pattern = re.compile('<h2.*?>(.*?)</h2>',re.S)
titles = re.findall(pattern,r.text)
print(titles)

'''

'''抓取二进制数据
import requests
r = requests.get("https://github.com/favicon.ico")
print(r.text)       #输出为str类型，把二进制转成str会乱码
print(r.content)    #结果的最前面有个b，代表是bytes类型数据
with open('favicon.ico','wb') as f:     #open()的方法，第一个参数是文件名称，第二个参数代表以二进制的形式打开，向文件内写入二进制数据
    f.write(r.content)

'''
'''
import requests
r = requests.get('https://scrape.center/favicon.ico')
print(r.text)
print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)
'''



# Post请求
'''
import requests
data = {'name' : 'germey','age' : '22'}
r = requests.post("https://www.httpbin.org/post",data=data)  #返回结果中form部分就是提交的数据
print(r.text)   # 上面的网站可以判断请求方式是否为post方式，是就返回相关信息

'''



'''响应
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
r = requests.get('http://www.jianshu.com',headers=headers)
print(type(r.status_code),r.status_code)    # status_code属性得到状态码
print(type(r.headers),r.headers)    #响应头
print(type(r.cookies),r.cookies)    
print(type(r.url),r.url)
print(type(r.history),r.history)    # 获取请求历史
# request内置的状态码查询对象requests.codes；这里通过比较返回码和内置的表示成功的状态码，来保证 请求是否正确相应
exit() if not r.status_code==requests.codes.ok else print('Request Successfully')   #这里用了.ok是200的返回的码

'''



# 文件上传
'''
import requests
files = {'file':open('favicon.ico','wb')}   # 用的是当前目录下的文件
r=requests.post("http://httpbin.org/post",files=files)
print(r.text)   #返回结果里面有files的字段标识为上传的文件

'''



# Cookies
'''还有另一种方法在书p57
import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    'Host': 'www.baidu.com',
    'Cookie': 'BIDUPSID=B9C4D930A81E4EB396FE66B140D12CE3; PSTM=1631449579; BD_UPN=12314753; __yjs_duid=1_5f279ee4d3ede4948bcd15160f4b553f1631451928150; BDUSS=JibWpOWVhjblF-T29lflAtQlJLWn5zYn4wa1Q5ZEN5N3JRd1dFRkg5LWN5SE5oSVFBQUFBJCQAAAAAAAAAAAEAAABU1AWldb7NuPq49gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJw7TGGcO0xhZn; BDUSS_BFESS=JibWpOWVhjblF-T29lflAtQlJLWn5zYn4wa1Q5ZEN5N3JRd1dFRkg5LWN5SE5oSVFBQUFBJCQAAAAAAAAAAAEAAABU1AWldb7NuPq49gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJw7TGGcO0xhZn; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID_BFESS=sy0OJeC62GIgTM5HuW2i8gB5F7CcgYrTH6ao1RQtIo7EpYApy_bTEG0PSx8g0Ku-MSrBogKK3gOTH4DF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=JbFtVCD-JIv-jttkMJQE2tcH-UnLqbJ8tgOZ0l8Ktq3zeUbEjf7h3TDteMJGtxKf0K7Mh4omWIQHDIj-0JOzhT-kKbrCbncdKHn4KKJxL-PWeIJo5DcY0nDYhUJiB5JMBan7_pbIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbRO4-TFae55y3H; BAIDUID=7FBA73026E4C0F250312AEF27AE82433:FG=1; COOKIE_SESSION=146955_3_6_6_10_13_1_0_6_4_4_7_146969_0_30_0_1637054791_1636871087_1637054761%7C9%23484631_13_1636871084%7C8; BAIDUID_BFESS=0030F0F44255301D5A14023EB2779B54:FG=1; BDRCVFR[n9IS1zhFc9f]=mk3SLVN4HKm; delPer=0; BD_CK_SAM=1; PSINO=6; BD_HOME=1; H_PS_PSSID=35105_31254_35049_35097_34584_34504_34578_34812_26350_35113_35128; sug=3; sugstore=0; ORIGIN=0; bdime=0; BA_HECTOR=21a42g8ha4040l2gm11gpc1e90r'
}
r=requests.get("https://www.baidu.com",headers=headers)
print(r.cookies)
for key,value in r.cookies.items():
    #上方调用Cookies属性得到Cookie，类型为RequestCookieJar类型，用items()的方法将其转换成元组组成的列表
    print(key+'='+value)

'''



# 会话维持
'''
import requests
s=requests.Session()
# 利用Session()可以做到模拟同一个会话而不用担心Cookies问题,常用于模拟登录成功后进行下一步操作
# 也可以模拟在一个浏览器中打开同一个站点不同的页面
s.get('http://httpbin.org/cookies/set/number/123456')   #测试网站，设置了Cookie，名称叫number，内容为123456
r=s.get('http://httpbin.org/cookies')   #访问请求这网站可以获取当前Cookies
print(r.text)

requests.get('http://httpbin.org/cookies/set/number/123456')
rr = requests.get('http://httpbin.org/cookies')     # 没有用会话只是相当于打开两个相同页面罢了
print(rr.text)  # 获取到的内容为空

'''



# SSL证书验证
'''设置忽略警告的方式来屏蔽SSl证书警告
import requests
from requests.packages import urllib3
urllib3.disable_warnings()
response=requests.get('https://www.12306.cn',verify=False)  #verify参数默认是true，要检查证书
print(response.status_code)

'''

'''通过捕获警告到日记的方式忽略警告
import logging
import requests
logging.captureWarnings(True)
response=requests.get('https://www.12306.cn',verify=False)
print(response.status_code)

'''

'''指定本地证书作为客户端证书
import requests
response=requests.get('https://www.12306.cn',cert=('/path/server.crt','/ath/key'))      #演示的
# 需要有crt和key文件，并且指定路径，key必须要解密状态
print(response.status_code)

'''

# 代理设置



# 超时设置
'''
import requests
r=requests.get("https//www.taobao.com",timeout=1)       #1秒内请求没有响应，就抛出异常，设置值为None(默认值)就长时间等待或者不设置timeout参数
R=requests.get("https//www.taobao.com",timeout=(5,30))  #请求分为两个阶段，即连接和读取，可以单独指定，传入元组作为参数
print(r.status_code)

'''



# 身份认证
'''
import requests
from requests.auth import HTTPBasicAuth     #request自带的认证功能
r=requests.get('http://ssr3.scrape.center/',auth=HTTPBasicAuth('admin','admin'))       #测试,该网站用户名和密码一样
# r=requests.get('http://ssr3.scrape.center/',auth=('username','password'))
# 可以使用精简写法传入一个元组，会默认用HTTPBasicAuth这个类认证
print(r.status_code)

'''

'''OAuth认证方法 pip3 install requests_oauthlib   有问题
import requests
from requests_oauthlib import OAuth1
from requests.packages import urllib3
urllib3.disable_warnings()
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY','YOUR_APP_SECRET','USER_OAUTH_TOKEN','USER_OAUTH_TOKEN_SECRET')
rr = requests.get(url,auth=auth)
print(rr.status_code)
'''

# Prepared Request(可以同样达到Post请求的效果)
# '''urllib中可以将请求表示为数据结构，其中各个参数都可以通过Request对象表示，在request也可以用Prepared Request表达这个数据结构
from requests import  Request,Session
url = 'https://www.httpbin.org/'
data={
    'name': 'germey'
}
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
# 下面的流程和requests的post请求一样的效果
# requests再发送请求的时候，在内部构造一个Request对象，并赋值参数(url、headers、data等)，在发送Request对象，请求成功载返回Response对象，解析该对象即可
s=Session()
req=Request('POST',url,data=data,headers=headers)   #引入Request类，然后用url，data和headers参数构造Request对象
prepped=s.prepare_request(req)      #再调用Session类的prepare_request()方法将其转换为一个Prepared Request对象
r=s.send(prepped)       #最后用send()方法发送
print(r.text)
# '''
