# -*- codeing = utf-8 -*-
# @Time : 2022/1/18 16:48
# @Author : wujinying
# @File : if语句.py
# @Software PyCharm

#　平替ｉｆ－ｅｌｓｅ判断
# text[name] = text.get(name,0)+1
# text字典存在name值，就加一，不存在就创键赋值为0

# 检查多个条件
age_0=22
age_1=18
print(age_0>=21 and age_1>=21)  # 输出False，用and检查多个条件，一个错全错
(age_0>=21) and (age_1>=21)     # 可以添加圆括号增加可读性

print(age_0>=21 or age_1>=21)   # 当有一个条件满足时，就是对的了

# 检查特定的值是否包含在列表中('关键字'或者元素变量 in 列表变量)
requested_toppings=['mushrooms','onions','pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

# 检查特定值是否不包含在列表中(not in)
banned_users=['andrew','carolina','david']
user='marie'
if user not in banned_users:
    print(f"{user.title()}, you can a response if you wish.")

# 布尔表达式(True和False)
game_active=True    # 可以用该变量作为条件判断起逻辑判断的正确于否
can_edit=False

# if-elif-else结构(就是if-else if-else语句)
age=12
if age<4:
    price=0
elif age<18:
    price=25
elif age<65:
    price=40
elif age>=65:
# else: 可以不要else，用elif替代
    pirce=20
print(f"Your admission cost is ${price}.\n")

# 要测试多个选择条件还是用回多个if避免跳过以下的判断选择
requested_toppings.append('extra cheese')
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
else:
    print("None")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("Finished making your pizza!\n")

# 遍历列表查询特殊元素(使用多个列表)
requested_toppings.append('green peppers')
available_toppings=['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
for requested_topping in requested_toppings:    # 遍历列表
    if requested_topping == 'green peppers':    # 查询列表是否存在green peppers这个元素
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
    if requested_topping in available_toppings:     # 利用循环遍历的requested_topping找到在availale——topping中对应元素
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,we don't have {requested_topping}.")
print("Finished making your pizza!\n")

# 确定列表是否为空
requested_toppings=[]
if requested_toppings:  # 直接
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")





















