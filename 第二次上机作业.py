# -*- codeing = utf-8 -*-
# @Time : 2022/9/14 15:05
# @AUTHOR : wujinying
# @File : 第二次上机作业.py
# @Software : PyCharm


# 可能的最小利克瑞尔数--196
'''
a = input("请输入一个数：")
while True:
    b = a[::-1]
    s = int(a)+int(b)
    print(f"{a}+{b}={s}")
    if str(s) == str(s)[::-1] or len(str(s)) > 100:
        break
    a = str(s)

'''

# 有一百个瓶子，分别编号为1-100。现在有人拿枪从第一个射击，每枪击破一个跳过一个，直到一轮结束。
# 接着在剩下的瓶子里面再次击破第一个，间隔一个在击破一个，最后剩下完整的瓶子时这一百个瓶子里面的第几个？

'''
s = list(range(1,101))
while len(s) > 1:
    s = s[1::2]
    print(s,end=",")    # end=","
print(s[0])

'''

# 水仙花数
'''
for i in range(100,1000):
    print(type(i))
    ii = str(i)
    if i == int(ii[0]**3) + int(ii[1])**3 + int(ii[2])**3:
        print(i)

'''


# 1.统计该文本中单词的出现次数。比如：How are you. How are you.统计结果是：{“how”:2, “are”:2,”you”:2}
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
        for word in words:
            word = word.lower()
            if word in dic.keys():
                dic[word] = dic.get(word) + 1
            else:
                dic[word] = 1
        num_words = len(words)
        print(dic)

dic = {}
count_words('第二次上机作业文本.txt', dic)

print('\n')

# '''

'''
2.已知：字符串a = "aAsmr3idd4bgs7Dlsf9eAF"，
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
    if n.isdigit():
        dic.append(n)
print(''.join(dic))

for n in a:
    if n in dic:
        continue
    elif n in dics.keys():
        dics[n] = dics.get(n) + 1
    else:
        dics[n] = 1
print(dics)

nn = ''
for n in a:
    if not n in nn:
        nn += n
print(nn)

print('\n')

'''3. 在单词表中查找包含所有元音字母aeiou的单词，并打印出来。
# 推荐一个单词表：
# https://github.com/qiwsir/StarterLearningPython/blob/master/newcodes/answers/dictionary.txt，
# 或者到http://www.math.sjsu.edu/~foster/dictionary.txt下载。
'''
import operator
def test_words(filename, lst):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()    # 空格或回车分割返回列表
        for word in words:
            lsts = []
            for char in word:
                if char.lower() in lst:     # 遍历拿到单词每一个字母判断是否在内，判断最后是否和传入的列表完整匹配
                    lsts.append(char)
            if operator.eq(lst,lsts):   # eq是==，判断两个对象是否相同，可以是自定义类对象
                # https://blog.csdn.net/weixin_36670529/article/details/116465808
                yield word

lst = ['a', 'e', 'i', 'o', 'u']
words = test_words("第二次上机作业文本2.txt", lst)
print(type(words))  # <class 'generator'>
for word in words:
    print(word)
print('\n')

# 或
def clean_word(word):
    return word.strip().lower()

def get_vowels_in_word(word):
    vowel_str = "aeiou"
    vowels_in_word = ""
    for char in word:
        if char in vowel_str:
            vowels_in_word += char
    return vowels_in_word

if __name__ == "__main__":
    data_file = open("dictionary.txt", "r")
    print("Find words containing vowels 'aeiou' in that order:")
    for word in data_file:
        word = clean_word(word)
        if len(word) <= 6:
            continue
        vowel_str = get_vowels_in_word(word)
        if vowel_str == "aeiou":
            print(word)


# 4. 编写斐波那契数列函数。
a, b, lsts = 0, 1, []
for i in range(10):
    a, b = b, a + b
    lsts.append(a)
print(lsts)

print('\n')

# 5. 定义一个由整数组成的列表，其中包含10个元素，分别赋值为1~10， 然后将列表中的元素依次向前移一个位置，即，原来是[1,2,3,4,5,6,7,8,9,10]，变成：[2,3,4,5,6,7,8,9,10,1]，然后输出这个数组
lst = [value for value in range(1, 11)]
lst.append(lst.pop(0))
print(lst)
