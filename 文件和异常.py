# -*- codeing = utf-8 -*-
# @Time : 2022/1/21 14:11
# @Author : wujinying
# @File : 文件和异常.py
# @Software PyCharm

# 读取整个文件
with open('pi_digits.txt') as file_object:  # open()填入文件的目录地址，然后open会返回一个表示文件的对象，赋值给名为file_object的变量
    contents=file_object.read()             # 关键字with会在不需要访问文件后将其文件关闭，这里我没有调用close()，文件关闭可以让py去判断，你只管开就行
                                            # 注意:如果用open和close来打开和关闭文件，当程序遇上bug时，将导致close无法正常执行，会导致更多错误
    # read()方法能读取这个文件的全部内容，并将其作为一个长字符串赋值给变量
print(contents.rstrip())         # 输出时可以发现多了一空行，是因为read到达文件尾部时返回返回一个空字符串，显示出来就是空行,可以添加rstrip方法删除字符串尾部空白

# 逐行读取
filename='pi_digits.txt'        # 把文件(路径)赋值给变量
with open(filename) as file_object:
    for line in file_object:
        print(line)             # 会看到有两行空白，文件每行末尾会有一个看不见的换行符，print循环时又带一个

# 创建一个包含文件各行内容的列表
filename='pi_digits.txt'
with open(filename) as file_object:
    lines=file_object.readlines()       # readlines方法冲文件中独缺每一行，并且将其存储在一个列表中，该列表被赋给变量lines，与c++不同的是，lines变量能在with代码块外使用
for line in lines:              # lines列表中每一个元素对应文件的一行
    print(line.rstrip())

# 使用文件的内容
pi_string=''
for line in lines:
    pi_string+=line.strip()     # 源文件中第二和第三行左边开始都有两个空格，可以用strip删除空格
print(f"{pi_string[:22]}")      # 显示qina20位小数点
print(len(pi_string))   # 长度包含个位和小数点

# 写入文件
filename='programming.txt'
with open(filename,'a') as file_object:     # open可以指定文件的访问模式，w写入，a追加，r+读写，r读取，不写第二个参数默认为r读取，a追加不会覆盖原文件内容，文件不存在时自动创建
    file_object.write("I love programmming.\n")
    file_object.write("I love creating new games.\n")



# 处理ZeroDivisionError异常
# print(5/0)    # 分母不能为0

# 运行后错误提示
# Traceback (most recent call last):
#   File "C:\Users\文档\网络爬虫开发\文件和异常.py", line 44, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero

# 使用try-except代码块(当认为可能出现错误时，可以编写这代码块处理可能会发生的异常)
try:
    print(5/0)      # 如果try下的代码块没有问题，将会跳过except代码块，如果发生错误，就会匹配except代码块并运行其中的代码
except ZeroDivisionError:       # 看上面的运行错误的Traceback能找到能找到匹配的异常对象
    print("You can't divide by zero!")

# 程序崩溃会出现Traceback，这样会让别有用心的人通过这个获取到该文件名称和路径，还能看见部分不正确的代码
'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number=input("\nFirst number:")
    if first_number=='q':
        break
    second_number=input("Second number:")
    if second_number=='q':
        break
    try:    # 待测试的代码块
        answer=float(first_number)/float(second_number)
    except ZeroDivisionError:   # 出现错误时执行
        print("You can't divide by 0!")
    else:       # 正确时执行
        print(answer)

'''

# 处理文件FileNotFoundError异常
def count_words(filenname):
    # 计算文件内有多少个单词
    try:
        with open(filename,encoding='utf-8') as f:      # 以只读的方式打开不存在的文件就会报错
            contents=f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass        # 静默失败，什么都不干，pass可以理解成执行这个模块时只当占位符，什么都不干
    else:
        words=contents.split()      # split()方法以空格为间隔符将字符串拆分成多个部分，并且存储在一个列表中，这样就能获取文章的所有单词数目
        num_words=len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames=['alice.txt','siddhartha.txt','moby_dick.txt','little_women.txt']
for filename in filenames:
    count_words(filename)


# 数据存储
import json     # json最初是js开发的一种格式，能够用来存储py中列表和字典等数据结构
numbers=[2,3,5,7,11,13]
filename='numbers.json'
with open(filename,'w') as f:   # 写入模式，没有文件就自动创建
    json.dump(numbers,f)    # dump方法接受两个参数，要存储的数据，及可用于存储数据的文件对象，dump方法将数字列表写入到文件中

with open(filename) as f:
    numbers=json.load(f)    # load方法将文件列表内容读取出来，并将其赋值给numbers
print(numbers)

# 重构(代码能够正确运行，但是一段代码中还能具体化分出一系列工作的函数，这样细化的过程叫做重构)
import json
def get_stored_username():  # 获取
    filename = 'username.json'
    try:
        with open(filename) as f:   # 只读的方式读取文件内容
            username=json.load(f)
    except FileNotFoundError:
        return False
    else:
        return username

def get_new_username():     # 写入
    username=input("What is your name?")
    filename='username.json'
    with open(filename,'w') as f:
        json.dump(username,f)   # 写入json文件
    return username

def greet_user():   # 输出
    username=get_stored_username()
    if username:    # 如果跑过一遍，文件username已将存在了，这里的if会时获取到get_stored_username()返回的内容，不用再输入了
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}! ")

greet_user()

"""原未重构代码
import json
filename='username.json'
try:
    with open(filename) as f:
        username=json.load(f)
except FileNotFoundError:
    username=input("What is your name?")
    with open(filename,'w') as f:
        json.dump(username,f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
"""



























