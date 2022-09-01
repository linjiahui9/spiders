# 生成一个由100以内能够被5整除的数组成的列表，然后将其从大到小排序
'''
values = []
for value in range(5,101,5):
    values.append(str(value))
    print(value)
values.reverse()
print(values)
'''



# 定义一个列表，要求列表元素包含字符串、整数、浮点数然后把列表中不是字符串的元素全部删除
'''
lists = ['xxx',100,100.1,100.2,'yyy',101,101.1,'aaa',101.2,'zzz',]
print(lists)
for list in lists[:]:
    if isinstance(list,str):
        pass
    else:
        lists.remove(list)
print(lists)
'''

# 输入英文姓名，按照字母顺序将所有姓名排序，输入完毕，将结果打印
'''
name_lst = []
while True:
    name = input("Please input an English name(input 'q' then exit)")
    if name == 'q':
        break
    else:
        name_lst.append(name)
name_lst.sort()
print(name_lst)
'''