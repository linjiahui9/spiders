# -*- codeing = utf-8 -*-
# @Time : 2022/1/17 12:57
# @Author : wujinying
# @File : 变量和简单数据类型.py
# @Software PyCharm

import this

# 字符串 引号括起来的都是字符串，可以是单引号，也可以是双引号

"""使用方法修改字符串大小写
name="aba lovelace"
print(name.title())     # .title方法能把各单词首字母都改成大写
print(name.upper())     # .upper方法能把字符全改成大写
print(name.lower())     # .lower方法能把字符全改成小写

"""

# """在字符串中使用变量
first_name='aba'
last_name='lovelace'
full_name=f'{first_name} {last_name}'    # 字符串中插入变量的值，可以在引号前加f(format设置格式)，再将要插入的变量放在花括号内，这样py显示字符串时，将把每一个变量都替换为其值
# print(full_name)    # 引号中间有空格，所以输出时有空格
print(f"Hello,{full_name.title()}!")    # 套娃
mesage=f"Hello,{full_name.title()}!"
print(mesage)

# 在3.7版本之前的要用format方法替代这种方式，
full_name="{} {}".format(first_name,last_name)  # 圆括号内列出字符串变量，前面被引用的一个花括号对应一个变量

# """

"""删除空白
language=' python '
print(language.rsplit())
print(language)
language=language.rsplit()  #rstrip方法能删除字符串末尾的空格，但是如果没有把删除操作关联 赋值回原变量，就只能输出显示时删除，变量本身并没有删除末尾的空格
print(language)

language=' python '
print(language.lstrip())    # 删除字符串开头的空格
print(language.strip())     # 删除两端的空格

"""

























