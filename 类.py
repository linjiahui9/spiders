# -*- codeing = utf-8 -*-
# @Time : 2022/1/20 22:08
# @Author : wujinying
# @File : 类.py
# @Software PyCharm

# 创建和使用类(创建Dog类)
class Dog:      # 创建类名，和c++类似
    def __init__(self,name,age):    # 方法__init__()。类中的函数被叫做方法，__init__()方法每当这个类创建新实例时，便会自动执行(这里和c++的构造函数类似)
        # 初始化属性name和age,这里的形参self在py调用这个方法时会自动传入实参self(在c++中类似this指针作用)
        # self是一个指向实例本身的引用,让实例能访问类中的属性和方法(类似C++拷贝构造函数传入的对象)
        self.name=name      # 获取形参name相关的值，让值赋给该变量，然后该变量被关联到当前创建的实例
        self.age=age        # 通过实例访问的在c++中叫成员变量，在py中叫属性

    def sit(self):
        # 函数模拟小狗接到命令时蹲下
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        # 模拟小狗接到命令时打滚
        print(f"{self.name} rolled over!")

my_dog=Dog('Willie',6)      # 实例创建(类似C++隐式创建对象)
print(f"My dog's name is {my_dog.name}.")       # 调用类中的属性
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()        # 调用类中的方法
my_dog.roll_over()

# 导入单个类
from car import Car

my_new_car=Car('audi','as4',2022)       # 创建实例
print(f"\n{my_new_car.get_descriptive_name()}")     # 调用类中方法，取得返回值
my_new_car.read_odpmeter()

# 修改属性的值
my_new_car.odometer_reading=23      # 直接修改属性值
my_new_car.read_odpmeter()

# 通过方法来修改属性值
my_new_car.update_odometer(28)
my_new_car.read_odpmeter()

# 通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odpmeter()

# 从一个模块中导入多个类
from car import ElectricCar,Battery

my_tesla=ElectricCar('tesla','model s',2003)    # 创建子类实例
print(my_tesla.get_descriptive_name())          # 子类的实例能够访问超类的方法
my_tesla.describe_battery()
my_tesla.fill_ges_tank()                # 调用子类的方法
my_tesla.battery.describe_battery()     # 与c++操作调用成员类相似，先调用ElectricCar的实例，在调用类内Battery创建的实例，最后调用Battery类内的describe_battery方法
my_tesla.battery.get_range()

# 导入整个模块
import car
my_beetle=car.Car('volkswagen','beetle',2002)
print(f"\nmy_beetle.get_descriptive_name()")

# 导入模块所有类(from module_name import *)(也可以给模块中的类起别名，as)

# 在一个模块导入另一个模块



# randint()标准库，把两个整数作为参数，并随机返回这两个数之间的整数
from random import randint
print(randint(1,6))

# choice()是random模块中用于把一个列表或元组作为参数，并随机返回其中一个元素
from random import choice
players=['charles','martina','michael','florence','eli']    # 注意：集合是没有下标可言的{，，，}
first_up=choice(players)
print(first_up)














