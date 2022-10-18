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
s, m = divmod(100, 3)  # 把除数和余数运算结果结合返回结果为元组(a//b , a%b)。例如：divmod(1+2j, 1+0.5j) >>> ((1+0j), 1.5j)
print(f'100除以3的商是{s}，余数是{m}')
print("100除以3，保留3位小数，结果是{}".format(round(100 / 3, 3)))  # 第一个参数数值表达式，第二个参数是保留的小数位
print('\n')

# 6、请解释如下现象：
print(round(2.675, 2))  # 十进制数字和浮点数之间的转换问题(但并非四舍五入，具体要查...)
print('\n')

# 7、精确计算：2除以6
# 要求：结果以分数形式（1/3）输出最终结果
import fractions

# 精确进行十进制计算的模块，分子（numerator）和分母（denominator）给构造函数用于实例化Fraction类，
# 但两者必须同时是int类型或者numbers.Rational类型，否则会抛出类型错误
result = fractions.Fraction(2, 6)
print(f'2/6 is {result.numerator}/{result.denominator}')
print(f'2/6 is {result}')  # 可以直接拿到结果
# 可以提供字符串给构造函数用于实例化Fraction类
a = fractions.Fraction('1/3')
b = fractions.Fraction('0.25')  # 可以from fractions import Fraction
print(a)  # 1/3
print(b)  # 1/4
# 可以提供整数和浮点数给构造函数用于实例化Fraction类
a = fractions.Fraction('0.3')
b = fractions.Fraction(0.3)
c = fractions.Fraction(30)
print(a)  # 3/10
print(b)  # 5404319552844595/18014398509481984
print(c)  # 30
#
print('\n')

# 8、要求：在print()里面将“明月几时有”和“把酒问青天”两句分两行输入，但是在输出时在一行
print("明月几时有,\
把酒问青天")  # 转义符
print('\n')

# 9、已知：字符串“c:\news”
# 要求：用print()将上述字符串在终端输出（写出两种方式）
dos = r'c:\news'
print(dos)  # 由r开头引起的字符串就是声明了后面引号里的东西是原始字符串，在里面放任何字符都表示该字符的原始含义(处理网址好用...)
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
aa = aa[::-1]  # 步进为-1倒着输出，步进为2就1、3、5输出0起步...
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
# (capitalize()函数：将字符串的第一个字母变成大写，其余字母变为小写。字符串最前面带空格则该字符串不会首字母大写)
a = "Python is a widely used high-level, general-purpose, interpreted, dynamic programming language."
print(a.title())  # 效果同下...修改上面字符串大小写用lower后再title试试
print(f"{' '.join([word.capitalize() for word in a.split()])}\n")  # ?

# 15、生成一个由100以内能够被5整除的数组成的列表，然后将该列表的数字从大到小排序(第一次上机作业)
lst = list(range(0, 100, 5))
# 方法一
print(lst.sort(reverse=True))  # sort方法传入reverse=True参数这样就可以按照逆序的方式排序
# 方法二
print(sorted(a, reverse=True))  # 用sorted方法只是临时修改列表的顺序，不影响原来列表中的顺序，同样想逆序就传入reverse=True参数
# 方法三(使用 reversed() 函数进行逆序操作，并不会修改原来序列中元素的顺序)
print(list(reversed(lst)))  # 除了使用列表推导式的方式，还可以使用 list() 函数，将 reversed() 函数逆序返回的迭代器，直接转换成列表
# 方法四
print(lst.reverse())  # 反转列表元素，注意是反转列表当前顺序，并没有进行哪种排序(再次调用就可以恢复原顺序)
# 方法五
print(lst[::-1])
# 将列表进行逆序(列表推导式的方式)
print([x for x in reversed([1, 2, 3, 4, 5])])
# 将元组进行逆序
print([x for x in reversed((1, 2, 3, 4, 5))])
# 将字符串进行逆序
print([x for x in reversed("abcdefg")])
# 将 range() 生成的区间列表进行逆序
print([x for x in reversed(range(10))])
print('\n')

# 自己定义一个列表，要求该列表中的元素至少要包括字符串、整数、浮点数。
# 要求：编写一段程序，列表中不是字符串的元素全部删除
lists = ['xxx', 100, 100.1, 100.2, 'yyy', 101, 101.1, 'aaa', 101.2, 'zzz']
print(lists)
for lst in lists[:]:  # 倒序遍历
    # isinstance() 与 type() 区别：
    # type() 不会认为子类是一种父类类型，不考虑继承关系。
    # isinstance() 会认为子类是一种父类类型，考虑继承关系。
    # 如果要判断两个类型是否相同推荐使用 isinstance()
    if isinstance(lst, str):
        # 用于判断一个对象是否是一个已知的类型，类似type()，第二个参数可以是直接或间接类名、基本类型或者由它们组成的元组
        # a = 2
        # isinstance (a,(str,int,list))     >>>     True
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
name_lst.sort()     # 列表排序，按照元素字母顺序来进行排序，并且是无法恢复原来的顺序的
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
        new_dct.update([(key, value), ])  # update方法没啥用，不如上面直接追加键值对...
print(dic)
print(f'{new_dct}\n')

# 20、在0到9之间随机选择1个整数，操作100次，统计共有几种数字，并用字典的方式输出每个数字的出现次数，键是出现的整数，值是出现的次数
import random

lst = [random.randint(0, 9) for i in range(100)]  # 列表解析
print(lst)
only_int = set(lst)  # 强转set元组去重
num = [lst.count(i) for i in only_int]  # count方法统计某个元素在列表中出现的次数(列表解析)
dct = dict(zip(only_int, num))
print(f'{dct}\n')
'''
l1 = [1, 2, 3, 4, 5]
l4 = [i**2 for i in l1 if i>=3] # 加入额外判断
print(l4)
>>>
[9, 16, 25]
'''

# 21、写一个程序，将公元1900年到2022年之间所有的闰年年份挑选出来
import calendar

years = range(1840, 2022)
print(type(years))  # <class 'range'>
laep_years = [year for year in years if calendar.isleap(year)]  # 列表解析，解析成列表不用append...
print(laep_years)
# 或
for year in years:
    if calendar.isleap(year):  # calendar方法?
        laep_years.append(year)
print(f'{laep_years}\n')

# 22、将整数2022的每个数字分离数来，依次打印输出
a = list(str(2022))  # 能直接拿常量强转...
print(f'{a}\n')
# for i in b:print(i) 遍历字符串和list都行...

# 25、已知：字典：{“name”: “python”, “book”: “python”, “lang”:”english”}
# 要求：将该字典的键和值对换。（注意，字典中有键的值是重复的）
from collections import defaultdict
# defaultdict是Python内建dict类的一个子类，第一个参数为default_factory属性提供初始值，默认为None。它覆盖一个方法并添加一个可写实例变量。它的其他功能与dict相同，但会为一个不存在的键提供默认值，从而避免KeyError异常
a = {"name": "python", "book": "python", "lang": "english"}
dd = defaultdict(list)      # 案例看defaultdict方法.png
for k, v in a.items():
    dd[v].append(k)
print(dict(dd))
# 如果你使用类似下面的方法，得到的结果跟上面有所不同，主要是没有考虑到值的重复。
b = {v: k for k, v in a.items()}
print(f'{b}\n')
# {'english': 'lang', 'python': 'book'}

# 统计该文本中单词的出现次数。比如：How are you. How are you.统计结果是：{“how”:2, “are”:2,”you”:2}
# '''
def count_words(filename, dic):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        # 返回分割后的字符串列表。默认以空格为分隔符，包含\n，可以在第一个参数指定分隔符，第二个参数指定列表返回的的元素个数
        print(type(words))  # list类型
        for word in words:
            word = word.lower()
            if word in dic.keys():
                dic[word] = dic.get(word) + 1
            else:
                dic[word] = 1
        num_words = len(words)
        print(f'{dic}\n')


dic = {}
count_words('第二次上机作业文本.txt', dic)

'''
已知：字符串a = "aAsmr3idd4bgs7Dlsf9eAF"，
要求：编写程序，完成如下任务：
请将字符串中的数字取出，并输出成一个新的字符串。
请统计字符串出现的每个字符的出现次数（忽略大小写，a与A是同一个字母），并输出成一个字典。 例 {'a':3,'b':1}
请去除字符串多次出现的字母，不区分大小写。例 'aAsmr3idd4bgs7Dlsf9eAF'，经过去除后，输出 'asmr3id4bg7lf9e‘
提示：
判断是否数字/字母： isdigit() /  isalpha()
若要保持原顺序，c.sort(key=a.index)
'''
a = "aAsmr3idd4bgs7Dlsf9eAF"
a = a.lower()
dic = []
dics = {}
for n in a:
    if n.isdigit():  # 判断单个字符是否为数字、判断字符串中是否仅含有数字
        dic.append(n)
print(''.join(dic))
# 或
print([i for i in a if i.isdigit()])

for n in a:
    # if n in dic:      # 要不要数字...
    #     continue
    # elif n in dics.keys():
    if n in dics.keys():
        dics[n] = dics.get(n) + 1
    else:
        dics[n] = 1
print(dics)

c = set([i for i in a])
print(''.join(list(c)))  # join列表
# 或
nn = ''
for n in a:
    if not n in nn:  # 拿空串拿没有的字符...
        nn += n
print(f'{nn}\n')


# 31、有一百个人，分别从1一直到100。现在有人拿枪从第一个开始枪毙，每枪毙一个跳过一个，
# 一直到一轮完成。接着在活着的人里面再次枪毙第一个，间隔一个再枪毙一个，请问最后活着的是这一百个人里的第几个人？
people_list = [x for x in range(1, 101)]
while len(people_list) != 1:
    people_list = people_list[1::2]     # 从第一个步进二取新列表，妙啊
print(people_list[0])
# 或
s = range(100)      # <class 'range'>
while len(s) > 1:
    s = [x for i, x in enumerate(s) if i % 2 == 1]
print(s.pop() + 1)
