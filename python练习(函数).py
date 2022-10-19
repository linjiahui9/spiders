# -*- codeing = utf-8 -*-
# @Time : 2022/10/19 15:04
# @AUTHOR : wujinying
# @File : python练习(函数).py
# @Software : PyCharm

"""
为老师们编写一个处理全班考试成绩的程序：
要求：
（1）能够依次录入班级同学的姓名和分数；
（2）录入完毕，则打印出全班的平均分，最高分的同学姓名和分数。
"""
'''
name_list = []
source_list = []
while True:
    name = input("请输入学生姓名：")
    if name == 'q':
        break
    else:
        source = input("请输入学生成绩：")
        source = int(source)
        name_list.append(name)
        source_list.append(source)
dic = dict(zip(name_list, source_list))
source_sum = sum(dic.values())
number = len(dic)
print("平均分%s" % (source_sum / number))
source_max = max(dic.values())
max_name = list(dic.keys())[list(dic.values()).index(source_max)]
print("最高分同学为姓名为：%s，成绩为：%d" % (max_name, source_max))

'''
# 或
def average(lst):
    total = 0
    for i in lst:
        total = total + i
    ave = total / len(lst)
    return ave


def max_student(dct):
    max_name = 0
    for k, v in dct.items():
        if v > max_name:
            max_name = v
            name = k
    return name, max_name   # 可以不打括号


if __name__ == "__main__":
    d = {}
    score_lst = []
    while True:
        name = input("input name:('q'-exit)")
        if name == "q":
            break
        else:
            score = int(input("input score:"))
            d[name] = score
            score_lst.append(score)

    ave = average(score_lst)
    print("the average scroe is:{}".format(round(ave, 2)))
    name, score = max_student(d)
print("xueba is {0}, his/her score is {1}".format(name, score))


# 36、编写斐波那契数列函数
def fibs(n):
    result = [0, 1]
    for i in range(n-2):
        result.append(result[-2] + result[-1])
    return result

if __name__ == "__main__":
    lst = fibs(10)
print(lst)

# 其它方式

class Fibs:
    def __init__(self, max):
        self.max = max
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        if fib > self.max:
            raise StopIteration
        self.a, self.b = self.b, self.a + self.b
        return fib

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibs(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


# 44、编写程序，判断一个数字是否为素数
import math

def isPrime1(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def isPrime2(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

from itertools import count

def isPrime3(n):
    if n <= 1:
        return False
    for i in count(2):
        if i * i > n:
            return True
        if n % i == 0:
            return False

def isPrime4(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

if __name__ == "__main__":
    p = []
    for i in range(1, 10):
        if isPrime4(i):
            p.append(i)
    print(p)


# 48、已知：字母序列【d, g, e, c, f, b, o, a】，请实现一个函数针对输入的列表，
# 比如["bed", "dog", "dear", "eye"]，按照前面规定的字母顺序排序并打印结果应为：dear, dog, eye, bed。
def char_to_number(by_list, char):    #根据排序依据字母顺序，给另外一个字母编号
    try:
        return by_list.index(char)
    except:
        return 1000

def sort_by_list(by_list, input_list):
    result={}
    for word in input_list:
        number_list = [char_to_number(by_list,word[i]) for i in range(len(word))]
        result[word] = number_list
    return [v[0] for v in sorted(result.items(), key=lambda x:x[1])]

if __name__=="__main__":
    word = ["bed","dog","dear","eye"]
    by_string = ['d','g','e','c','f','b','o','a']
    print("the word list is:")
    print(word)
    print("\nwill sorted by:")
    print(by_string)
    print("\nthe result is:")
print(sort_by_list(by_string,word))


# 49、将一个整数，分拆为若干整数的和。例如实现： 4=3+1 ，4=2+2 ，4=2+1+1 ，4=1+1+1+1
def divided(m,r,out):
    if(r==0):
        return True
    tm=r
    while tm>0:
        if(tm<=m):
            out.append(tm)
            if(divided(tm, r-tm, out)):
                print(out)
            out.pop()
        tm = tm-1
    return False

n=6
output=[]
divided(n-1, n, output)


# 50、编写一段程序，许可用户输入三角形的三条边的长度（使用整数），判断是否能构成一个三角形，如果能，其形状是什么样的？
# 要求：输入三边长度；输入判断结果；再计算三角形面积（使用海伦公式计算）
import math
def sorted_sides(sides_lst):
    sides = sorted(sides_lst)
    x, y, z = sides[0], sides[1], sides[2]
    return float(x), float(y), float(z)

def is_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    if x >=0:
        if (x + y > z):
            return True
        else:
            return False
    else:
        return False

def side_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    if x == y or y == z:
        return "isosceles"
    elif x == z:
        return "equilateral"
    else:
        return "scalene"

def angle_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    difference = z**2 - (x**2 + y**2)
    if difference == 0:
        return "right"
    elif difference > 0:
        return "obtuse"
    else:
        return "acute"

def area_triangle(sides_lst):
    x, y, z = sorted_sides(sides_lst)
    s = (x + y + z)/2
    a = math.sqrt(s*(s-x)*(s-y)*(s-z))
    return round(a, 3)

if __name__ == "__main__":
    triangle_sides = input("please input three sides of triangle, and split them by space:")
    sides_lst = triangle_sides.split()
    if is_triangle(sides_lst):
        result_side = side_triangle(sides_lst)
        result_angle = angle_triangle(sides_lst)
        area = area_triangle(sides_lst)
        print("The triangle is {0} and {1}. Its area is {2}".format(result_side, result_angle, area))
    else:
        print("Sorry, the sides cannot be the side of triangle.")


# 51、编写程序，检验一个数是否是完全数，比如6 = 1+2+3，6就是一个完全数
# https://github.com/qiwsir/StarterLearningPython/blob/master/newcodes/answers/q40.py


# 52、编写一个程序，将列表[2,3,5]中的所有数字的排列和组合全部列出来。
#本题放在函数部分，是因为有不少朋友看到题目之后，试图自己编写函数，通过循环的方式实现。
# 但在Python中，我们不使用这种解决问题思路，而是：
import itertools
list(itertools.permutations([2, 3, 5], 2) )
# [(2, 3), (2, 5), (3, 2), (3, 5), (5, 2), (5, 3)]
list(itertools.permutations([2, 3, 5], 1))
# [(2,), (3,), (5,)]
list(itertools.permutations([2, 3, 5], 3))
# [(2, 3, 5), (2, 5, 3), (3, 2, 5), (3, 5, 2), (5, 2, 3), (5, 3, 2)]

list(itertools.combinations([2, 3, 5], 3))
# [(2, 3, 5)]
list(itertools.combinations([2, 3, 5], 2))
# [(2, 3), (2, 5), (3, 5)]
list(itertools.combinations([2, 3, 5], 1))
# [(2,), (3,), (5,)]


# 53、写一个函数，用以求解一元二次方程，并在程序中使用
# 要求：输入一元二次方程的系数，输出方程的样式和解
import math
import cmath

def solve_be(a, b, c):
    delta = b**2 - 4*a*c
    if delta == 0:
        #x = fractions.Fraction(-b, 2*a)
        x = -b / (2*a)
        return x
    elif delta > 0:
        sqrt_delata = math.sqrt(delta)
    else:
        sqrt_delata = cmath.sqrt(delta)
    #x1 = fractions.Fraction((-b + sqrt_delata), 2*a)
    #x2 = fractions.Fraction((-b - sqrt_delata), 2*a)
    x1 = (-b + sqrt_delata) / (2*a)
    x2 = (-b - sqrt_delata) / (2*a)
    return (x1, x2)

if __name__ == "__main__":
    print("The binary linear equation is x^2 + 2^x + 3 = 0")
    r = solve_be(1, 2, 3)
    if len(r) == 1:
        print("The equation only has one root. It is:")
        print(r)
    else:
        print("The equation have two root. They are:")
print(r)


# 54、编写程序，提示用户输入一个在0~99的值，然后以文字的形式显示该值。例如，如果输入21，则显示twenty-one。
# 本问题在网上可以看到不同的解法，推荐两个：
# http://www.blog.pythonlibrary.org/2010/10/21/python-converting-numbers-to-words/
# https://www.quora.com/How-do-I-convert-numbers-to-words-in-Python
# 仅供参考
# 但是，熟悉python的模块，能够让解法更简单
# sudo pip3 install num2words
from num2words import num2words
num2words(42)
# 'forty-two'
num2words(1234567890)
# 'one billion, two hundred and thirty-four million, five hundred and sixty-seven thousand, eight hundred and ninety'
# 所以，在开发中要充分使用轮子，不要重复造轮子了


# 57、回文（palindrome）是正读或者反读都相同的单词或但与，忽略空格和字母大小写。
# 例如，下面的示例都是回文：warts n straw、radar、xyzczyx。编写一个程序，判断输入的字符串是否是回文。
def palindrome(word):
    word_lst = [ i for i in word ]
    word_lst.reverse()
    new_word = "".join(word_lst)
    if word == new_word:
        return True
    else:
        return False

if __name__ == "__main__":
    while True:
        word = input("input a word:('q'-exit)")
        if word == "q":
            break
        else:
            if palindrome(word):
                print("{0} is a palindrome".format(word))
            else:
                print("The word is not palindrome")


# 59、将一个正整数分解质因数。
def split_int(a):
    for i in range(2, 100, 1):
        if a % i == 0:
            return i
    return 0

if __name__ == '__main__':
    a = int(input('input a number, please.'))
    val = split_int(a)
    while val > 1:
        print(val)
        a = a / val
val = split_int(a)

# 60、计算两个整数的最大公约数和最小公倍数。
def gcd(m, n):
    return m if n == 0 else gcd(n, m % n)

def lcm(m, n):
    return m * n // gcd(m, n)

if __name__ == "__main__":
    m = int(input("input m:"))
    n = int(input("input n:"))
    print("GCD", gcd(m, n))
print("LCM", lcm(m, n))
