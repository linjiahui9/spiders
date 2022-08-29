# -*- codeing = utf-8 -*-
# @Time : 2022/1/21 12:20
# @Author : wujinying
# @File : car.py
# @Software PyCharm

# 在一个模块存储多个类

# 使用类和实例(Car类给属性指定默认值)
class Car:
    def __init__(self,make,model,year):
        # 初始化描述汽车的属性
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0     # py创建新属性，并且把初始值设置为0

    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odpmeter(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:  # 新指定的值大于或等于原来的值
            self.odometer_reading=mileage   # 把新属性中的值设置为指定值
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        self.odometer_reading+=miles    # 写普通的类内方法修改属性

    def fill_ges_tank(self):        # 与子类同名方法
        print(f"This car need a gas tank!")

# 将实例用作属性
class Battery:      # 类也能作为类内的属性
    def __init__(self,battery_size=75):
        self.battery_size=battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):    # 根据电量写续航
        if self.battery_size==75:
            range=260
        elif self.battery_size==100:
            range=315
        print(f"This car can go about {range} miles on a full charge.")

# 子类(创建子类时，父类必须包含在当前文件中，且位置在子类前面)
class ElectricCar(Car):     # 继承填入父类名
    # 子类能有独特于父类的属性和方法
    def __init__(self,make,model,year):     # 不懂回看上面
        super().__init__(make,model,year)   # super是一个特殊的函数,能都调用超类(父类)的方法,这里调用父类的init方法(类似c++一样,派生类要初始化父类的成员,能够调用父类的构造函数)
        self.battery_size=75        # 子类能在继承超类的属性同时，也能创建只属于子类新属性，超类不能访问

        self.battery = Battery(100)  # 在类内创建Battery的实例，并且赋值给ElectricCar的battery属性(该属性类型时类)

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_ges_tank(self):    # 方法名与父类相同，重写父类的方法。子类的实例调用时，默认先调用子类重写的，覆盖掉父类的同名方法(C++的函数重载)
        print("This car doesn't need a gas tank!")