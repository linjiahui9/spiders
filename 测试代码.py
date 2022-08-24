# -*- codeing = utf-8 -*-
# @Time : 2022/1/22 11:48
# @Author : wujinying
# @File : 测试代码.py
# @Software PyCharm

# 从name_function模块(文件)中导入get_formatted_name函数，假设要修改程序让其也能判断中间名，就要修改函数，然后进行测试，这样太繁琐了
"""
from name_function import get_formatted_name
print("Enter 'q at any time to quit.")
while True:
    first=input("\nPlease give me a first name:")
    if first=='q':
        break
    last=input("Please give me a last name:")
    if last=='q':
        break
    formatted_name=get_formatted_name(first,last)
    print(f"\tNeatly formatted name: {formatted_name}.")

"""

# 单元测试和测试用例(py标准库中的模块unittest提供代码测试根据)
# 单元测试用于核实函数的某个方面没有问题。测试用例是一组单元测试，它们一道核实函数在在各种情况下的行为都符合要求

# 先导入unittest模块，再创建一个继承unittest.TestCase的类，在派生类中编写一系列方法对函数进行不同方面测试
'''
import unittest
from name_function import get_formatted_name    # 导入要测试的函数
class NamesTestCase(unittest.TestCase):         # 创建类来继承unittest模块中的TestCase类
    # 测试name_function.py
    def test_first_last_name(self):             # 核实get_formatted_name函数的测试方法
        formatted_name=get_formatted_name('janos','joplin')     # 传入参数，获取返回值
        self.assertEqual(formatted_name,'Janos Joplin')     # assertEqual断言方法：核实得到的结果是否于期望的结果一致。
        # assertEqual方法参数将上行获取返回值的变量与字符串‘Janis Joplin'比较

    def test_first_last_middle_name(self):  # 添加新测试
        formatted_name=get_formatted_name('wolfgang','mozart','amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
if __name__ == '__main__':      # 许多测试的框架都会先导入测试文件再运行，导入文件时解析器将在导入的同时执行它。(其实就是main主函数，pycharm中直接输入main回车就行)
    # 代码块检查特殊变量__name__：这个变量时在程序执行时设置的，如果这个文件作为主要程序执行，则变量__name__将被设置为'__main__'，就会调用下行代码来运行测试用例
    unittest.main()             # 在这里，调用unittest.main()来运行测试用例，如果这个文件被测试框架导入(下面那句话)，变量__name__的值将不会是'__main__'，因此不会调用这句
                                                                        # 要确保该测试文件也不是被测试的文件...
'''

# 当get_formatted_name方法改成要能处理中间名时，对其测试只有姓和名会出错，不能正确处理
# E     # 指明测试用例中有一个单元测试导致了错误
# ======================================================================
# ERROR: test_first_last_name (__main__.NamesTestCase)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\文档\网络爬虫开发\测试代码.py", line 32, in test_first_last_name
#     formatted_name=get_formatted_name('janos','joplin')     # 传入参数，获取返回值
# TypeError: get_formatted_name() missing 1 required positional argument: 'last'    # 这里指明错误原因，missing一个位置实参
# 
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s
# 
# FAILED (errors=1)

# 测试AnonymousSurvey类
'''
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):   # 继承unittest.TestCase类。
    # 针对AnonymousSurvey开始测试
    def test_store_single_response(self):   # 一个方法测试作为一组单元测试
        # 测试单个答案会被正确存储
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)     # 创建实例
        my_survey.store_response('English')     # 实例调用方法
        self.assertIn('English',my_survey.responses)    # 字符串匹配类的属性(列表)，看survey.py文件中的类

    def test_store_three_responses(self):
        # 测试3个
        question="What language did you first learn to speak?"
        my_survey=AnonymousSurvey(question)     # 创建实例
        responses=['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_response(response)         # 看survey.py文件中的类中store_response方法
        for response in responses:
            self.assertIn(response,my_survey.responses)

if __name__ == '__main__':
    unittest.main()         # 出现两个点就是代表两个测试都通过了
 
'''

# 方法setUp()：unittest.TestCase类中包括了setUp方法，这样在写派生类中重写，派生类在测试时会优先运行setUp方法，setUp方法一般用作创建实例和设置其属性的，在其他方法中直接使用这些实例
import unittest
from unittest import TestCase
from survey import AnonymousSurvey

class TestAnonymousSurvey(TestCase):
    # 继承unittest.TestCase类。不想这样写，想只写TestCase类名，要改成from unittest import TestCase,不过最后那里还是要用到unittest模块，结果还是要写...
    # 针对AnonymousSurvey开始测试
    def setUp(self):        # setUp创建一个调查对象和答案列表，这样下面的方法测试作为一组单元测试时，可以不用重复创建(实例)对象和(列表)答案
        # 创建一个调用对象和一组答案，供使用的测试方法使用
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)  # 创建实例
        self.responses = ['English', 'Spanish', 'Mandarin']     # 创建空列表

    def test_store_single_response(self):   # 一个方法测试作为一组单元测试
        # 测试单个答案会被正确存储
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_store_three_responses(self):
        # 测试3个
        for response in self.responses:
            self.my_survey.store_response(response)         # 看survey.py文件中的类中store_response方法
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()         # 出现两个点就是代表两个测试都通过了































