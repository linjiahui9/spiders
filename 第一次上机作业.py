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

'''
lst = range(0,100,5)
a = list(lst)
a.sort(reverse=True)

sorted(a,reverse=True)

a[::-1]
'''

# 定义一个列表，要求列表元素包含字符串、整数、浮点数然后把列表中不是字符串的元素全部删除
# '''
lists = ['xxx',100,100.1,100.2,'yyy',101,101.1,'aaa',101.2,'zzz']
print(lists)
for list in lists[:]:
    if isinstance(list,str):
        pass
    else:
        lists.remove(list)  # 正序pop和remove会出现跳过的情况
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


