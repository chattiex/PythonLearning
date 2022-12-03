# class Teacher:
#     yyy = 111
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
# dahai = Teacher('大海', 18, '男')
# # D选项正确
# # 给对象添加了一个独有的属性
# dahai.yyy = 222
# # print(Teacher.yyy)
# # 对象有独有的属性会优先用自己的
# print(dahai.yyy)
#
#
# # B选项错误
# # 对象独有的属性不会给类用
# # print(Teacher.name)
# # 打印结果是 dahai
# # C选项错误
# print(Teacher.yyy)

'''
第六题

定义一个Student类，有姓名、年龄，性别实例/对象属性，定义一个自我介绍的方法，可以打印出自己的姓名，

学号和年龄的信息。

'''

# class Student:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def self_introduction(self):
#         # print('大家好，我是%s,我今年%s岁，性别%s'%('小明',18,'男'))
#         print('大家好，我是%s,我今年%s岁，性别%s'%(self.name,self.age,self.sex))
#
#
#
#
# xiaoming = Student('小明',18,'男')
# # print(xiaoming.__dict__)
# xiaoming.self_introduction()


'''
第七题

声明一个电脑类：

属性：品牌、颜色、内存大小

方法：打游戏、写代码、看视频

对品牌属性修改，删除颜色属性

调用方法：打游戏、写代码、看视频

# '''
# class Computer:
#     def __init__(self,brand,color,ram):
#         self.brand = brand
#         self.color = color
#         self.ram = ram
#     def play(self):
#         print('打游戏')
#     def video(self):
#         print('看电视')
#     def code(self):
#         print('看视频')
#
# p=Computer('联想','黑色','16G')
# p.brand = '华硕'
# print(p.__dict__)
# del  p.color
# print(p.__dict__)
# p.play()
# p.code()
# p.video()


'''
第八题

创建一个Person类，添加一个类属性用来统计Perosn类的对象的个数

'''
# class Person:
#     numbers = 0
#     def __init__(self,name):
#         # print('对象生成都会经过__init__方法')
#         Person.numbers += 1
#         self.name = name
# a=Person('大海')
# a1=Person('夏洛')
# a2=Person('顾安')
# a3=Person('柏川')
# print(Person.numbers)


'''
第九题

声明一个矩形类

属性：长、宽 方法：计算周长和面积

创建不同的矩形，并且打印其周长和面积

'''

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
#
#     def per(self):
#         print('周长是%s'%((self.length+self.width)*2))
#
#     def area(self):
#         print('面积是%s'%(self.length*self.width))
#
# c = Rectangle(5,6)
# c.per()
# c.area()


'''
第十题

设计一个立方体类（Box），定义三个属性，分别是长、宽、高。定义两个方法，分别计算并输出立方体的体积和表面积

'''
# class Box:
#     def __init__(self,l,x,h):
#         self.l = l
#         self.x = x
#         self.h = h
#     def tiji(self):
#         tiji = self.l*self.x*self.h
#         return tiji
#     def biaomianji(self):
#         biaomianji = (self.l*self.x+self.l*self.h+self.x*self.h)*2
#         return biaomianji
#
# box = Box(1,2,3)
# print(box.tiji())
# print(box.biaomianji())




