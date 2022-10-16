# -*- codeing = utf-8 -*-
# @Time : 2022/10/12 20:05
# @Author : wujinying
# @File : 第四次上机作业.py
# @Software PyCharm

'''
1. 创建类SchoolKid，初始化小孩的姓名、年龄。也有访问每个属性的方法和修改属性的方法。
然后创建类ExaggeratingKid，继承类SchoolKid，子类中覆盖访问年龄的方法，并将实际年龄加2。
'''
class SchoolKid:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name.title()

    def setName(self,name):
        self.name = name

    def getAge(self):
        return self.age.title()

    def setAge(self,age):
        self.age = age

class ExaggeratingKid(SchoolKid):
    def __init__(self, name, age):
        super().__init__(name, age)

    def setAge(self,*age):
        super(ExaggeratingKid, self).setAge(self.age+2)

skid = SchoolKid('xiaoming',18)
ExaggeratingKid(skid).setAge(18)
print(skid.getAge())

'''
2. 有五种鲜花，花名和价格，分别是：
（1）牵牛花（petunia）：50
（2）三色堇（pansy）：75
（3）玫瑰（rose）：15
（4）紫罗兰（violet）：50
（5）康乃馨（carnation）：80
编写一个类，并在程序中实例化该类，调用类中的方法，实现输入购买数量和花名，就能打印出总价
'''

class flower:
    def __init__(self):

        petunia = 50
        pansy = 75
        rose = 15
        violet = 50
        carnation = 80

    def count(self,**dic):
        if
        dic.keys()

    def show(self):
        print()


name_list = []
source_list = []
while True:
    name = input("请输入购买的花名：")
    if name == 'q':
        break
    else:
        source = input("请输该花购买的数量：")
        source = int(source)
        name_list.append(name)
        source_list.append(source)
dic = dict(zip(name_list, source_list))
