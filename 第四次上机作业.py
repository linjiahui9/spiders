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
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name.title()

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


class ExaggeratingKid(SchoolKid):
    def __init__(self, name, age):
        super().__init__(name, age)

    def getAge(self):
        super().setAge(self.age + 2)
        return self.age


if __name__ == "__main__":
    skid = ExaggeratingKid('xiaoming', 18)
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


class Flower:
    def __init__(self, priceTable):
        self.priceTable = priceTable
        self.count = 0
        self.name = ''
        self.total = 0

    def buyFlower(self, name, count):
        if name in self.priceTable:
            self.count = count
            self.name = name
            self.total = self.priceTable[self.name] * self.count + self.total
        else:
            self.total = 0

    def total(self):
        return self.total


if __name__ == "__main__":
    priceTable = {"petunia": 50, "pansy": 15, "rose": 75, "violet": 20, "carnation": 80}
    print(priceTable)
    flower = Flower(priceTable)
    while True:
        name = input("输入花名，按q退出：")
        if name == "q":
            break
        else:
            count = int(input("输入购买的数量:"))
            flower.buyFlower(name, count)
            print(f"You should pay:{flower.total}")

