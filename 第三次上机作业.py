# -*- codeing = utf-8 -*-
# @Time : 2022/10/6 12:48
# @AUTHOR : wujinying
# @File : 第三次上机作业
# @Software : PyCharm

"""
1. 编写一个程序，提示输入整数X，然后计算从1开始，连续X个整数之和。
提示：reduce(参数1：函数要有两个参数，参数2：可迭代对象，参数3可选：初始参数)函数
"""
from functools import reduce

X = int(input("输入整数X求1到X之和："))
lst = [value for value in range(1, X)]
print(reduce(lambda x, y: x + y, lst))  # x.y参数和x+y匿名函数具体实现

'''
2. 已知：已知两个列表：citys = [“suzhou”, “shanghai”, “hangzhou”, “nanjing”]，codes = [“0512”, “021”, “0571”, “025”]
要求：创建一个字典，以citys中的元素为key，以codes中的元素为value
提示：创建字典的方法，zip()函数
根据上面所得到字典中，选出value不是三个数字的键值对组成一个新的字典。比如”shanghai”:”021”就不应该在新字典中出现。
提示：字典的update()、items()方法
'''
citys = ['suzhou', 'shanghai', 'hangzhou', 'nanjing']
codes = ['0512', '021', '0571', '025']
dic = {}
for key, value in dict(zip(citys, codes)).items():
    if len(value) != 3:
        dic[key] = value
print(dic)

'''
3. 为老师们编写一个处理全班考试成绩的程序：
要求：
（1）能够依次录入班级同学的姓名和分数；
（2）录入完毕，则打印出全班的平均分，最高分的同学姓名和分数。
'''
name_list = []
source_list = []
while True:
    name = input("请输入学生姓名：")
    if name == 'q':
        break
    else:
        source = input("请输入学生成绩：")
        source = int(source)
        name_list.append(name)
        source_list.append(source)
dic = dict(zip(name_list, source_list))
source_sum = sum(dic.values())
number = len(dic)
print("平均分%s" % (source_sum / number))
source_max = max(dic.values())
max_name = list(dic.keys())[list(dic.values()).index(source_max)]
print("最高分同学为姓名为：%s，成绩为：%d" % (max_name, source_max))

'''
4. 一个列表由若干个整数组成，
要求：将偶数放到前面，奇数放到后面，并输出该列表。
提示：filter()
'''
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
even = list(filter(lambda num: num % 2 == 0, lst))
odd = list(filter(lambda num: num % 2 == 1, lst))
print(even + odd)
