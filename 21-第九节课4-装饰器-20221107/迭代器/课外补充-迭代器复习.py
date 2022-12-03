# -*- coding:utf-8 -*-
# @FileName: 课外补充-迭代器复习.py
# @Time    : 2022/11/2 21:18
# @Author  : 顾安


# 什么是迭代器
'''
1. 在python中，可以被for循环执行的对象都被称之为可迭代对象
2. 可迭代对象不一定是一个迭代器，迭代器一定是一个可以迭代的对象
    在一个对象中，如果只是实现了一个__iter__方法 我们称当前的这个对象为一个可以迭代的对象
    在一个对象中，创建了__iter__以及__next__方法 则当前的对象才是一个迭代器
'''


# 1. 实现一个可以迭代的对象
class MyRange:
    def __init__(self):
        self.index = 0
        self.my_list = []

    def add(self, item):
        self.my_list.append(item)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.my_list):
            result = self.my_list[self.index]
            self.index += 2
            return result
        raise StopIteration

# 上面的这个类是一个可以迭代的对象
# 我要知道你当前的迭代的流程

'''
没有形成一个整体的知识架构
    生成器
        -> 函数
        -> class
        -> 控制流程
        -> 容器类型
        -> 赋值操作
        -> 变量
        -> 循环
        
多任务
    
    sqlallchemy orm框架
    
    xpath
    http
    requests
    scrapy
    javascript
   
    js逆向
    
    看懂
        打断点
        api的网络数据
        
        java
'''


'''
如果现在有四个类 四个类分别在四个py文件中

    这四个类中的迭代的方式是一模一样的

    你愿意写四遍
        原因导入引用？
        
在项目开发中 不只有单继承
    多继承
        
        继承的执行速度比对象关联慢
'''


# 1. 创建一个实例对象
my_range = MyRange()
# 2. 添加元素
my_range.add(1)
my_range.add(2)
my_range.add(3)
my_range.add(4)
my_range.add(5)

# 1. 检测当前in后面的对象是否包含__iter__方法
for i in my_range:
    print(i)
