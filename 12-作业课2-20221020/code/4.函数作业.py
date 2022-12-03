# def run():
#     print('dahai')
#
#
# # print(run)
# # 函数对象/函数内存地址
# # run()
# # # 1.变量引用数据:   数据类型   引用另一个变量   引用一个函数对象（函数内存地址）
# func=run
#
# func()

# 2.当作参数传给一个函数
# x='hello'
# def func():
#     print('from func')
#
# def foo(m):
#     print(m)
#     # m就是func的内存地址
#     m()
#
# #
# print(func)
# foo(func)

# 3.可以当作函数的返回值
# x='hello'
# def func():
#     print('from func')
# def foo(x):
#     print(x)
#     return x
# #
# res=foo(func)
# print(res)
# res()


# 4.可以当作容器类型的元素
# x='hello'
# def func():
#     print('from func')
# # l=[x,]
# # print(l)
# l=[func,]
# print(l)
# print(l[0])
# l[0]()

# 5.函数内存地址加括号（括号里面放不放参数根据定义的函数参数决定）调用函数


# 第二题
# def func(a,b=[]):
# 	print(id(b))
# 	b.append(a)
# 	print(b)
# func(1)
# func(1)
# func(1)
# func(1)


# def func(a,b={}):
#     b[a] = 'v'
#     print(b)
# func(1)
# func(2)

# a = 1
# def fun(a):
# 	a=2
# 	return a
# a=fun(a)
# print(a)


# *args
# def run(*args):
# 	print(args)
# run(1,2,3,4,5)

# **kwargs
# def run(**kwargs):
# 	print(kwargs)
# run(x=1,y=2,w=3,a=4,b=5)

# def factory(a,b): # 制造一个工厂
#     print('a是%s'%a)
#     print('b是%s'%b)
# 正确
# factory(1,2)
# 错误
# factory(a=1,2)
# 正确
# factory(1,b=2)

# 第9题
#
# 输入三个数字，写一个函数将三个数字从小到大输出

# def my_sorted(a,b,c):
#
#     list1= []
#     list1.extend([a,b,c])
#     list1.sort()
#     # print(list1)
#     return list1
# a = int(input('输入第一个数字'))
# b = int(input('输入第二个数字'))
# c = int(input('输入第三个数字'))
# list1=my_sorted(a,b,c)
# print(list1)


# 第10题
#
# 定义一个函数，计算1到990的和，用for循环完成

# n = 990
#
# def for1(n):
#     sum = 0
#     for i in range(1,n+1):
#         # print(i)
#         sum += i
#     # print(sum)
#     return sum
# s=for1(n)
# print(s)


# 笔记在手 天下我有
# 学会了 上学
# 学习心态    一台好电脑
# 找对象      把自己打扮好点   找一个特别丑朋友


'''
1.数据类型*****
2.控制流程*****
3.函数基础*****
4.函数高级***
5.面向对象****
6.网络编程***
7.并发编程****
8.模块使用*****
9.mysql数据库使用***
10.redis数据库使用***
11.MongoDB数据库使用***
13.python操作mysql数据库*****
14.python操作redis数据库*****
15.python操作MongoDB数据库*****
'''

# 双赢
# 爬虫课

# 插班生  每一次的这个作业解答课  看录播学习  不懂直接下课问老师









