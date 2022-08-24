# -*- codeing = utf-8 -*-
# @Time : 2022/1/17 13:43
# @Author : wujinying
# @File : 列表.py
# @Software PyCharm

# 列表由一系列按照特定顺序排列的元素组成，元素之间没有任何关系，列表通常用[]表示，用逗号分隔其中的元素
bicycles=['trek','cannondale','redline','specialized']
print(bicycles)     # 直接输出列表会带方括号
print(bicycles[0])  # 带下标能取得列表下标对应元素，这样就不会包含括号
print(bicycles[0].title())  # 显示下标0的元素大写
print(bicycles[-1]) # 显示倒数第一个元素

# 使用列表中的各个值
message=f"first bicycle was a{bicycles[0].title()}."    # 提取列表第一个元素并插入字符串变量
print(message)

# 修改、添加和删除元素
bicycles[0]='treks'     # 修改下标为0的元素值
print(bicycles)

bicycles.append('ducati')   # 列表尾部追加元素
print(bicycles)

bicycles.insert(0,'ducatis')    # 插入表头(第0号下标)
print(bicycles)

del bicycles[1]     # 删除任意位置下标的元素(这里删除第二个元素treks)，这种方法删除后无法访问其元素
print(bicycles)

popped_bicycles=bicycles.pop()      # 弹出表尾元素，相当于弹出栈顶能再赋值于新变量保存，保存后仍然能访问改元素
print(popped_bicycles)
print(bicycles)
print(f"The last bicycles I owned was a {popped_bicycles.title()}.")     # 可以作用于访问最后的(按时间的话可以是最近)

first_pop=bicycles.pop(0)   # 可以在圆括号中填入下标，弹出任意下标的元素
print(first_pop.title())

re_bicycles='redline'
bicycles.remove(re_bicycles)      # 弹出列表中于re_bicycles值相同的元素，但还能通过re_bicycles 变量访问被弹出的值
# bicycles.remove('redline')      # 删除列表中第一个值为redline的元素，有多个相同的redline元素要用到循环remove
print(bicycles)
print(f"\nA {re_bicycles.title()} is too expensive for me.")

# 组织列表
cars=['bmw','audi','toyota','subaru']
cars.sort()     # 按照元素字母顺序来进行排序，并且是无法恢复原来的顺序的
print(cars)

cars.sort(reverse=True)     # sort方法传入reverse=True参数这样就可以按照逆序的方式排序
print(cars)

Cars=['bmw','audi','toyota','subaru']
print(sorted(Cars))     # 用sorted方法只是临时修改列表的顺序，不影响原来列表中的顺序，同样想逆序就传入reverse=True参数
print(sorted(Cars,reverse=True))
print(Cars)

cars.reverse()  # 反转列表元素，注意是反转列表当前顺序，并没有进行哪种排序
print(cars)

len(cars)       # 确认列表长度







