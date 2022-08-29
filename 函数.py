# -*- codeing = utf-8 -*-
# @Time : 2022/1/20 16:01
# @Author : wujinying
# @File : 函数.py
# @Software PyCharm

# 关键字实参(def 函数名(形参):)
def describe_pet(animal_type,pet_name='willie'):    # 与大多数语言一样，有默认参数的形参只能在没有默认参数的形参右边
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')     # 注意实参顺序
describe_pet(pet_name='harry',animal_type='hamster')    # 显示调用关键字实参时，实参顺序不重要了
describe_pet('dog')     # 这里只填一个实参，如果默认形参参数写在靠左边，这个dog就会覆盖默认参数，而后面的第二个形参将没有任何参数

# 函数返回值(让实参变成可选的)
def get_formatted_name(first_name,last_name,middle_name=''):
    if middle_name:     # py会将非空字符解读为True，把最后一个形参作为判断条件(形参的默认参数为空)，借此判断是否填写最后的实参
        full_name=f"{first_name} {middle_name} {last_name}"
    else:
        full_name=f"{first_name} {last_name}"
    return full_name.title()    # 返回首字母大写的字符串
musician=get_formatted_name('jimi','hendrix')   # 取得返回值
print(musician)

musician=get_formatted_name('john','hooker', 'lee')   # 取得返回值
print(musician)

# 返回字典
def build_person(first_name,last_name,age=None):
    person={'first':first_name, 'last': last_name}
    if age:
        person['age']=age   # 字典的追加...
        return person
musician=build_person('jimi', 'hendrix', age=27)
print(musician)

# 函数结合while循环
"""
def get_name(first_name,last_name):
    full_name=f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' zt any time to quit")

    f_name=input("First name:")
    if f_name=='q':
        break

    l_name=input("Last name:")
    if l_name=='q':
        break

    formatted_name=get_name(f_name,l_name)
    print(f"\nHello, {formatted_name.title()}!")

"""

# 传递列表
unprinted_designs=['phone case','robbot pendant','dodecahedron']
completed_models=[]

def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()      # 弹出元素，保存
        print(f"Printing model:{current_design}")
        completed_models.append(current_design)     # 添加到新列表中

def show_completed_models(completed_models,unprinted_designs='None'):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:        # 遍历输出新列表
        print(completed_model)

    for unprinted_design in unprinted_designs:
        print(unprinted_design)
# print_models(unprinted_designs,completed_models)
print_models(unprinted_designs[:],completed_models)  # 切片表示法[:]：以切片表示法填入实参，实际上传递过去的是列表的副本，pop弹出元素后，并不会改变原来的unprinted_designs中元素个数
show_completed_models(completed_models,unprinted_designs)

# 传递任意数量的实参
def make_paizza(*toppings):     # 这里的星号让py创建一个名为toppings的空元组，并且把收到的所有值都封装到这个元组中(这里的元组有点像字符型动态数组)
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_paizza('pepperoni')
make_paizza('mushrooms','green pepppers','extra cheese')

# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):     # 基于这种情况，py首先将第一个实参给size，然后后面的都是topping这个元组里面了
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_paizza(16,'pepperoni')
make_paizza(12,'mushrooms','green peppers','extra cheese')

# 使用任意数目的关键字实参
def build_profile(first,last,**user_info):      # 两个星号让py创建名为user_info的空字典，并且能把收到的所有键值对都放入字典当中
    # 创建一个字典，其中包含我们知道有关用户的一切
    user_info['first_name']=first
    user_info['last_name']=last
    return user_info

user_profile=build_profile('albert','einstein',location='princeton',field='physics')    # 传入两对键值对
print(f"\n {user_profile}")

# 导入整个模块(module_name.function_name()：导入module_name的文件)
import pizza
pizza.make_pizza(16,'pepperoni')
pizza.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 导入特定的函数(from module__name import function_name：导入文件中的函数，直接调用就好，效果于上面的方法相同,如果想导入该模块所有函数import后面写*匹配所有就行)
from pizza import make_pizza
make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green pepppers','extra cheese')

# 使用as给函数指定别名
from pizza import make_pizza as mp
mp(16,'pepperoni')
mp(12,'mushrooms','green pepppers','extra cheese')

# 使用as给模块指定别名
import pizza as p
p.make_pizza(16,'pepperoni')
p.make_pizza(12,'mushrooms','green peppers','extra cheese')

# 给形参写默认值时，等号两边不要有空格，对于函数调用是用关键字实参(显示调用)，也是如此
# import引用其他文件和库时一般写开头

































