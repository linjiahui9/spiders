# -*- codeing = utf-8 -*-
# @Time : 2022/1/18 21:34
# @Author : wujinying
# @File : 字典.py
# @Software PyCharm
# '''
# 字典就是一系列的键值对用花括号

# 添加键值对
alien_0={'color':'green','points':5}
alien_0['x_position']=0     # 末尾追加键值对
alien_0['y_position']=25
print(alien_0)

# 修改字典中的值
alien_0['color']='yellow'
print(f"The alien is now {alien_0['color']}.\n")    # 这里用f格式输出字典中color键对应的值，没有括号


# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
alien_0['speed']='medium'
if alien_0['speed']=='slow':
    x_increment=1
elif alien_0['speed']=='medium':
    x_increment=2
else:
    x_increment=3
alien_0['x_position']=alien_0['x_position']+x_increment     #例如这里可以直接指出键然后加变量就好了
print(f"New x_position:{alien_0['x_position']}")

# 删除键值对
del alien_0['points']   # 删除键points及其值(永久性的不可赋值变量)

# 由类似对象组成的字典(对于较长的列表和字典，一般采用这种格式，大多数编译器也提供了以类似方式设置格式的功能)
favorite_languages={
    'jen':'python',
    'sarah':'c',
    'edward':'rubu',
    'phil':'python',
}

# 使用get()来访问值
# 字典以用get方法在指定的键不存在时返回一个默认值，能避免访问不存在的键出现报错
point_value=alien_0.get('points','No point value assigned.')    # get方法第二个参数是可选的，写了当没找到字典中的键时返回第二个参数，没写就是默认None
print(point_value)

# 遍历字典
user_0={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi'
}
for key,value in user_0.items():    # 声明两个变量，用于存储键值对中的键和值。items方法返回一个键值对列表，for循环依次将每个键值对付给指定的两个变量
    print(f"\nKey:{key}")
    print(f"Value:{value}")

# 遍历字典中所有键(在不需要值得时候会好用些)
for name in favorite_languages.keys():      # .keys()可以写或者不写，遍历时默认是遍历所有的键，显示调用可能更好理解
# for name in favorite_languages:
    print('\n'+name.title())

friends=['phil','sarah']    # 创建一个列表
for name in favorite_languages.keys():  # 遍历列表并把元素逐个赋值给name
    print(f"Hi {name.title()}.")

    if name in friends:         #
        language=favorite_languages[name].title()   # 首字母大写的方式赋值给language
        print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():     # erin不存在的键
    print("Erin, please take our poll!")

for name in sorted(favorite_languages.keys()):  # 通过sorted方法把字典的keys方法返回的键写入作为参数，能对键进行排序输出
    print(f"{name.title()}, thank you for taking the poll.")

# 遍历字典中的所有值
print("\nThe following languages have been mentioned:")
for language in favorite_languages.values():    # 通过values方法来返回一个值列表，不包含键
    print(language.title())     # 有两次py
print('\n')
for language in set(favorite_languages.values()):   # 通过调用set把字典的values方法返回值写入为参数，能提取出不重复的值
    print(language.title())

# 字典列表(嵌套，列表中每一个元素就是一个字典)
aliens=[]   # 创建一个用来存储外星人的空列表
for alien_number in range(30):      # 循环30次
    new_alien={'color':'green','points':5,'speed':'slow'}   # 创建字典
    aliens.append(new_alien)    # 把字典追加进列表

for alien in aliens[:3]:    # 遍历修改前三个
    if alien['color']=='green':
        alien['color']='yellow'
        alien['speed']='medium'
        alien['points']=10

for alien in aliens[:5]:    # 遍历输出前5个一模一样的外星人
    print(alien)
print('...')
print(f"Total number of aliens:{len(aliens)}")  # len方法显示列表长度

# 在字典中存储列表(一个键存在多个值(列表))
favorite_languages={
    'jen':['python','ruby'],
    'sarah':['c'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
}
for name,languages in favorite_languages.items():    # 54行
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:      # 有多个值(列表)，遍历输出
        print(f"\t{language.title()}")

# '''
# 在字典中存储字典
users={
    'aeinstein':{
        'frist':'albert',
        'last':'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'frist':'marie',
        'last':'curie',
        'location':'paris',
    },
}
for username, user_info in users.items():   # 54行
    print(f"\nUsername:{username}")     # 用户名
    full_name=f"{user_info['frist']} {user_info['last']}"   # 完整名字的格式
    location=user_info['location']
    work=user_info.get('work','None work!')     # 45行

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tWork:{work.title()}")









