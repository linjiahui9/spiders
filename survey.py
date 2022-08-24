# -*- codeing = utf-8 -*-
# @Time : 2022/1/22 15:58
# @Author : wujinying
# @File : survey.py
# @Software PyCharm

# 这个类可以进行简单的调查，但想让每个用户都可以输入多个答案时，要编写多一个方法，可能用户在输入多个答案时修改处理单个答案的方式，所以要测试(这段代码没这问题)

class AnonymousSurvey:
    # 收集匿名调查问卷的答案
    def __init__(self,question):
        # 存储一个问题，并为存储答案做准备
        self.question=question
        self.responses=[]

    def show_Question(self):
        # 显示调查问卷
        print(self.question)

    def store_response(self,new_response):
        # 存储单份调查答卷
        self.responses.append(new_response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")



