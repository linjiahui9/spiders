# 生成一个由100以内能够被5整除的数组成的列表，然后将其从大到小排序
# '''
values = []
for value in range(5,101,5):
    values.append(str(value))
values.reverse()
print(values)
# '''

# '''
lst = [value for value in range(5,101,5)]
print(lst)
lsts = []
for value in lst:
    lsts.append(str(value))
lsts.reverse()
print(lsts)
# '''

# '''
lst = list(range(5,101,5))
print(lst)
lsts = []
for value in lst:
    lsts.append(str(value))
lsts.reverse()
print(lsts)
# '''

# 定义一个列表，要求列表元素包含字符串、整数、浮点数然后把列表中不是字符串的元素全部删除
# '''
lists = ['xxx',100,100.1,100.2,'yyy',101,101.1,'aaa',101.2,'zzz',]
print(lists)
for list in lists[:]:
    if isinstance(list,str):
        pass
    else:
        lists.remove(list)
print(lists)
# '''

# 输入英文姓名，按照字母顺序将所有姓名排序，输入完毕，将结果打印
# '''
name_lst = []
while True:
    name = input("Please input an English name(input 'q' then exit)")
    if name == 'q':
        break
    else:
        name_lst.append(name)
name_lst.sort()
print(name_lst)
# '''

# 寻找这样的两位数，使得将它进行平方后，将产生1个三位数，而这个三位数最右边的两个数字与原来的2位数字相同
#Squates = [value**2 for value in range(10,101)]
#for s in Squates:
#    if str(s).length() == 3:
#        s = str(s)
#        if s[0:2] 
#    else:
#        continue
def find_num(n):
    x = n**2
    if x>99 and x<1000:
        last_two = x%100
        if last_two == n:
            return True
        else:
            return False
    else:
        return False

for i in range(10,100):
    if find_num(i):
        print(i)
    

# 回文（palindrome）是正读或者反读都相同的单词或短语，忽略空格和字母大小写。例如，下面的示例都是回文：warts n straw、radar、xyzczyx编写一个程序，判断输入的字符串是否是回文
while True:
    word = input("input a word:('q':exit)")
    if word in ('q','Q'):
        break
    else:
        word = ''.join(word.split())    # 按空格分隔,再连接
        word = word.lower()
        if word == word[::-1]:
            print(f"{word}是回文...")
        else:
            print(f"{word}不是回文...")


# 在一个list中删掉奇数，只保留偶数
[k+2 for k in [1,2,3,4] if k % 2 == 0]
list(map(lambda x:x+2, filter(lambda k:k % 2 == 0, [1,2,3,4])))

# 3. 在单词表中查找包含所有元音字母aeiou的单词，并打印出来。
# 推荐一个单词表：
# https://github.com/qiwsir/StarterLearningPython/blob/master/newcodes/answers/dictionary.txt，
# 或者到http://www.math.sjsu.edu/~foster/dictionary.txt下载。
def count_words(filename,lst):
    try:
        with open(filename,encoding='utf-8') as f:
            contents=f.read()
    except FileNotFoundError:
        pass
    else:
        words=contents.split()
        for word in words:
            if word.lower()[0:1] in lst:
              print(word)  
                
lst = ['a','e','i','o','u']
count_words("dictionary.txt",lst)

# 4. 编写斐波那契数列函数。


# 5. 定义一个由整数组成的列表，其中包含10个元素，分别赋值为1~10， 然后将列表中的元素依次向前移一个位置，即，原来是[1,2,3,4,5,6,7,8,9,10]，变成：[2,3,4,5,6,7,8,9,10,1]，然后输出这个数组
lst = [value for value in range(1,11)]
lst.append(lst.pop(0))   
print(lst) 
