# -*- codeing = utf-8 -*-
# @Time : 2022/1/18 13:29
# @Author : wujinying
# @File : 列表操作.py
# @Software PyCharm

# py是根据缩进来判断代码行与前一个代码行的关系
magicians=['alice','david','carolina']
for magician in magicians:      # 使用单复数形式命名，可以帮助判断处理的是单个列表还是整个列表，还有注意冒号，c/c++循环没有冒号
    print(f"{magician.title()},that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")    #如果忘了缩进就会利用循环结束后的终值carolina，看似合法，其实逻辑会不符合

# 创建数值列表(这样只是将一列数打印出来)
for value in range(1,11):    # range能生成一些列数，如果参数只有一个则是从0到该数值减一
    print(value)    # 打印一系列数输出1到4，左开右闭

# 使用range创建数字列表(把上面的那组数转换为列表)
numbers=list(range(1,11,2))    # 用函数list将range的结果直接转换成列表，把range作为list的参数，输出将是一个数字列表，
print(numbers)                 # 第三个参数指定步进值

squates=[]      # 创建空列表
for value in range(1,11):
    # squate=value**2   两种方法
    # squates.append(squate)
    squates.append(value**2)    # py中两个**号表示乘方(平方)，把1到10的每个数的平方追加到列表squates中
print(squates)
print(min(squates))    # 求数列最小值
print(max(squates))    # 求数列最大值
print(sum(squates))    # 求数列和

# 列表解析
Squates=[value**2 for value in range(1,11)]     # 列表解析将for循环和创建新元素的代码合并为一行，并自动附加新元素
print(Squates)              # 这里在括号里面先定义一个表达式用来生成要存储到列表中的值，接下来在接上一个for循环用于给表达式提供值，注意：这个for循环末尾没有冒号

# 切片(左开右闭,输出会带中括号)
players=['charles','martina','michael','florence','eli']
print(players[:3])      # 输出的也是列表，没有默认卡头索引，默认是从0开始
print(players[2:])      # 没有填写结尾索引，默认截取到结尾(0,1,2)
print(players[-3:])     # 截取倒数第三个元素开始到结尾(-3.-2,-1没有-0)

# 遍历切片(循环每个元素会有换行)
print("Here are the first three players oon my team:")
for player in players[:3]:
    print(player.title())

# 复制列表
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]    # 都不填默认从起始到结尾索引，逗号为切片的方法复制能把切片的副本复制给另一个列表，类似形参和实参
print(friend_foods)
# friend_foods=my_foods       # 直接赋值有点像引用让两个变量名指向同一个列表，后面那个变量名修改列表都会有影响

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)     # 不用关联回原列表























































