# -*- codeing = utf-8 -*-
# @Time : 2022/1/18 16:31
# @Author : wujinying
# @File : 元组.py
# @Software PyCharm

# 列表中的元素是可以修改的，而元组中的元素是不可以修改的(用圆括号)，不可修改的列表(用中括号)也称之为元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])
# dimensions[0]=250     这里是不允许修改的
my_t=(3,)       # 严格来说元组是由逗号标识的，圆括号只是杨元组看起来更整洁清晰。定义一个元素的元组基本没有什么意义，而且注意必须要在元素后加上逗号才能表示一个元素的元组

# 修改元组变量
# 元组不能修改其内部元素，但是可以修改其变量。可以重新定义整个元组，给变量赋值
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions=(400,100)
print("\nModified fimensions:")
for dimension in dimensions:
    print(dimension)

# 元组用于存储一组数在程序的整个生命周期内都不变























































