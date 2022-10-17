# -*- codeing = utf-8 -*-
# @Time : 2022/10/17 10:47
# @AUTHOR : wujinying
# @File : python练习
# @Software : PyCharm


# 3、已知：a = 2, b = 3
# 要求：将a和b的值调换，并打印结
a, b = 2, 3
b, a = a, b
print('a = ', a)
print('b = ', b)  # 变量和对象的引用关系
print('\n')

# 5、计算：100除以3得到的商、余数分别是多少？如果保留3为小数，结果是多少？
# 要求：输出结果应该是如下样式
# 100除以3的商是33，余数是1
# 100除以3，保留3位小数，结果是33.333
s, m = divmod(100, 3)  # 查方法
print(f'100除以3的商是{s}，余数是{m}')
print("100除以3，保留3位小数，结果是{}".format(round(100 / 3, 3)))  # 查方法
print('\n')

# 6、请解释如下现象：
print(round(2.675, 2))  # 十进制数字和浮点数之间的转换问题
print('\n')

# 7、精确计算：2除以6
# 要求：结果以分数形式（1/3）输出最终结果
import fractions

result = fractions.Fraction(2, 6)
print(f'2/6 is {result.numerator}/{result.denominator}')  # 精确进行十进制计算的模块(查)
print('\n')

# 8、要求：在print()里面将“明月几时有”和“把酒问青天”两句分两行输入，但是在输出时在一行
print("明月几时有,\
把酒问青天")  # 转义符
print('\n')

# 9、已知：字符串“c:\news”
# 要求：用print()将上述字符串在终端输出（写出两种方式）
dos = r'c:\news'
print(dos)  # py中的r ?
dos2 = 'c:\\news'
print(dos2)
print('\n')

# 10、编写程序，要求输入你的姓名和年龄，并且将年龄加10之后，与姓名一起输出
'''
name = input("what is your name?")
age = input("how old are you?")
new_age = int(age) + 10     # 要该整型先要强转不然默认String

print("{0} will be {1} yeas old in ten yeas.".format(name, new_age))
'''

# 11、将字符串“map”的字符顺序倒转为“pam”
aa = 'map'
aa = aa[::-1]  # 步进为-1倒着输出，步进为2就1、3、5输出
print(aa)
# 或
bb = list(aa)  # 强转list处理
print(bb)
bb.reverse()  # 反转这里不用赋值回去...
print(bb)
print(''.join(bb))  # 空字符连接列表...
print('\n')

# 12、让用户输入一个单词，并显示这个单词的长度
'''
word = input("please input a word:")
length_word = len(word)
print("the length of {0} is {1}\n".format(word, length_word))
'''

# 13、已知字符串："Python is a widely used high-level, general-purpose, interpreted, dynamic programming language."
# 要求：将字符串中每个单词的第一个字母都变成大写字母
a = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language."
print(f"{' '.join([word.capitalize() for word in a.split()])}\n")  # ?

# 15、生成一个由100以内能够被5整除的数组成的列表，然后将该列表的数字从大到小排序(第一次上机作业)
lst = list(range(0, 100, 5))
# 方法一
print(lst.sort(reverse=True))
# 方法二
print(sorted(a, reverse=True))
# 方法三
print(list(reversed(lst)))
# 方法四
print(lst.reverse())
# 方法五
print(lst[::-1])
print('\n')

# 自己定义一个列表，要求该列表中的元素至少要包括字符串、整数、浮点数。
# 要求：编写一段程序，列表中不是字符串的元素全部删除
lists = ['xxx', 100, 100.1, 100.2, 'yyy', 101, 101.1, 'aaa', 101.2, 'zzz']
print(lists)
for lst in lists[:]:  # 倒序遍历
    if isinstance(lst, str):  # 查方法...
        pass
    else:
        lists.remove(lst)  # 正序pop和remove会出现跳过的情况
print(f'{lists}\n')

# 输入英文姓名，按照字母顺序将所有姓名排序，输入完毕，将结果打印
'''
name_lst = []
while True:
    name = input("Please input an English name(input 'q' then exit)")
    if name == 'q':
        break
    else:
        name_lst.append(name)
name_lst.sort()     # 列表排序
print(name_lst)
'''

'''
已知：已知两个列表：citys = [“suzhou”, “shanghai”, “hangzhou”, “nanjing”]，codes = [“0512”, “021”, “0571”, “025”]
要求：创建一个字典，以citys中的元素为key，以codes中的元素为value
提示：创建字典的方法，zip()函数
根据上面所得到字典中，选出value不是三个数字的键值对组成一个新的字典。比如”shanghai”:”021”就不应该在新字典中出现。
提示：字典的update()、items()方法
'''
citys = ['suzhou', 'shanghai', 'hangzhou', 'nanjing']
codes = ['0512', '021', '0571', '025']
dic = {}
new_dct = {}
for key, value in dict(zip(citys, codes)).items():  # items看字典遍历...
    if len(value) != 3:
        dic[key] = value
        new_dct.update([(key, value), ])  # 查update方法...
print(dic)
print(f'{new_dct}\n')

# 20、在0到9之间随机选择1个整数，操作100次，统计共有几种数字，并用字典的方式输出每个数字的出现次数，键是出现的整数，值是出现的次数
import random

lst = [random.randint(0, 9) for i in range(100)]
print(lst)
only_int = set(lst)
num = [lst.count(i) for i in only_int]
dct = dict(zip(only_int, num))
print(f'{dct}\n')
