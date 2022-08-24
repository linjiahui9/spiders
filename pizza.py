# -*- codeing = utf-8 -*-
# @Time : 2022/1/20 21:50
# @Author : wujinying
# @File : pizza
# @Software PyCharm

# 将函数存储在模块中
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppongs:")
    for topping in toppings:
        print(f"- {topping}")

