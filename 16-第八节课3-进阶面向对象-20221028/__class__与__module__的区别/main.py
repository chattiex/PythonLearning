# -*- coding:utf-8 -*-
# @FileName: main.py
# @Time    : 2022/10/26 21:08
# @Author  : 顾安


from test import Person

obj = Person()

print(obj.__module__)  # 当前这个类所存在的文件名 所谓的模块就是一个py文件
print(obj.__class__)

