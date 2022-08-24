# -*- codeing = utf-8 -*-
# @Time : 2022/7/3 12:54
# @Author : wujinying
# @File : 2.3正则表达式.py
# @Software PyCharm

# 正则表达式测试工具 http://tool.oschina.net/regex/
# 常用匹配规则：p65

'''match方法：向其传入要匹配的字符串以及正则表达式，就可以匹配，不匹配返回none，匹配从字符串起始位置开始^
import re
content = 'hello 123 4567 world_this is a regex demo'
print(len(content))
result = re.match('^hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())   # group方法输出匹配到的内容
print(result.span())    # span方法输出匹配到的内容在原字符串中的位置范围

'''
'''匹配目标部分内容
import re
content = 'hello 1234567 world_this is a regex demo'    # 和上面字符串有区别
result = re.match('^hello\s(\d+)\sworld',content)
print(result)
print(result.group())   # 匹配的内容(包含正则表达式写的那部分)
print(result.group(1))  # 匹配的结果
print(result.span())
'''
'''通用匹配
import re
content = 'hello 123 4567 world_this is a regex demo'
result = re.match('^hello.*(\d+).*demo$',content)   # 贪婪模式
print(result)
print(result.group())
print(result.group(1))  # 贪婪模式匹配尽可能多的字符，.*拿到123 456，+拿到一个或多个，所以留下一个7匹配到了
print(result.span())
'''
'''非贪婪模式.*?
import re
content = 'hello 123 4567 world_this is a regex demo'
result = re.match('^hello.*?(\d+).*demo$',content)   # 非贪婪模式
print(result)
print(result.group())
print(result.group(1))  # 非贪婪模式匹配尽可能少的字符，就匹配走了空格，(\d+)拿到了123
'''
'''匹配中间的内容用.*?，匹配后面的内容就用.*
import re
content = 'http://weibo.com/comment/keracn'
result1 = re.match('http.*?comment/(.*?)',content)
result2 = re.match('http.*?comment/(.*)', content)
print('result1',result1.group(1))   # 匹配尽可能少的字符，无内容
print('result2',result2.group(1))
'''
"""修饰符re.I使匹配对大小写不敏感(p69有其他修饰符)
import re
content = '''hello 1234567 world_this
is a regex demo
'''
result = re.match('^he.*?(\d+).*?demo$',content,re.S)
print(result.group(1))      # re.S修饰符作用是使匹配内容包括换行在内的所有字符
"""
'''转义匹配 \ 例如：( .
import re
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com',content)
print(result)
print(result.group())
'''



'''search方法：匹配时依次以每个字符作为开头扫描后面字符串，返回匹配到的第一个结果(p70网页案例)
import re
content = 'extra stings hello 1234567 world_this is a regex demo extra  sting'
result = re.search('hello.*?(\d+).*?demo',content)   # 正则开头时hello，而字符串开头是extra
print(result)
print(result.group(1))
'''



html = '''<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

"""findall方法：获取正则表达式匹配的所有结果
import re
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
print(type(results))
for result in results:
    print(result)
    print(result[0],result[1],result[2])
"""



'''sub方法：第一个参数传入要被替换的格式第二个参数传入替换的内容，第三个参数是原字符串
import re
content = '2sfgs34543sdfg345yy'
content = re.sub('\d+','',content)  # 替换所有的数字为空
print(content)
'''
'''提取li节点的歌名正则提取和sub方法提取
import re
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
for result in results:
    print(result[1])

print("---------------------------")

html = re.sub('<a.*?>|</a>','',html)    # 先用sub方法将a节点去掉，只留下文本再用正则提取
print(html)
resultsss = re.findall('<li.*?>(.*?)</li>',html,re.S)
for resultss in resultsss:
    print(resultss.strip())
'''



# '''compile方法：上面的方法都是处理字符串的，该方法可以将正则字符串编译成正则表达式对象，以便后面可以复用
import re
content1 = '2019-12-15 12:00'
content2 = '2019-12-17 12:55'
content3 = '2019-12-22 12:21'
pattern = re.compile('\d{2}:\d{2}')     # 这样就不用重复写三次正则了
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
result4 = re.findall(pattern,content3)
print(result3,result1,result2,result4)
# '''