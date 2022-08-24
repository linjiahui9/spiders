# -*- codeing = utf-8 -*-
# @Time : 2022/1/22 11:49
# @Author : wujinying
# @File : name_function.py
# @Software PyCharm

"""
def get_formatted_name(first,last):
    full_name=f"{first} {last}"     # 生成整洁的名字
    return full_name.title()
"""

"""
def get_formatted_name(first,middle,last):
    full_name=f"{first} {middle} {last}"     # 生成整洁的名字
    return full_name.title()
"""

def get_formatted_name(first,last,middle=''):
    if middle:
        full_name=f"{first} {middle} {last}"     # 生成整洁的名字
    else:
        full_name=f"{first} {last}"
    return full_name.title()



