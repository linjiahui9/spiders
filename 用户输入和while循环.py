# -*- codeing = utf-8 -*-
# @Time : 2022/1/19 11:35
# @Author : wujinying
# @File : 用户输入和while循环.py
# @Software PyCharm

# input原理：函数让程序暂停运行，等待用户输入文本回车后，赋值回车前数据于变量(参数填入的是提示说明,或变量说明)
# 使用int()方法来获取数值输入
"""
height=input("How tall are you,in inches?")     # 获取键盘输入内容，默认为字符串
height=int(height)      # 把字符串强制类型转换整形
if height >= 48:        # py无法直接用字符串于整形比较
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you;re a little older.")

"""

# 使用while循环
current_number = 1
while current_number < 10:    # 循环判断条件是小于10
    current_number += 1
    if current_number % 2 == 0: # 找奇数
        continue            # 跳过本次循环
    print(current_number)

# 使用标志(布尔)
"""
prompt="\nTell me something, and I will repeat it back to you:"
prompt+="\nEnter 'quit' to end the program."

message=""      # 创建空字符串
active=True     # 标志(布尔)
# while active:   # 另一种方法(再或者直接写True，下面else写break)
while message != 'quit':
    message=input(prompt)
    if message !='quit':
        print(message)
    # else:
        # active=False
        # break

"""

# 使用while循环处理列表
unconfirmed_users=['alice','brian','candace']   # 待验证的列表
confirmed_users=[]      # 完成验证的列表

while unconfirmed_users:        # 执行到unconfirmed_users为空表为止
    current_user=unconfirmed_users.pop()  # 弹出(列表.py 31行)

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)    # 追加进新列表
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:  # confirmed_user 循环创建的变量
    print(confirmed_user.title())

# 删除列表中所有的特定值
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')      # 列表.py 41行
print(pets)

# 使用用户写入的数据填充字典
responses={}    # 创建空字典
while True:     # 两次输入
    name=input("\nWhat is your name?")
    response=input("Which mountain would you like to climb someday?")

    responses[name]=response    # 把回答的值写入对应的键

    repeat=input("Would you like to let another person respond?(yes/no)")
    if repeat=='no':    # 判断是否跳出循环
        break
print("\n--- Poll Results ---")
for name, response in responses.items():    # 字典.py 54行
    print(f"{name} would like to climb {response}.")
































