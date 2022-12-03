# -*- coding: utf-8 -*-
# @Time: 8:31 下午
# @Author: 顾安
# @File: 10.process_pool
# Software: PyCharm


import time
from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor


def func(value):
    time.sleep(1)
    print(value)


# 创建线程池运行函数
# thread_pool = ThreadPoolExecutor(max_workers=5)
# for i in range(10):
#     fut = thread_pool.submit(func, i)
#     print(fut)


# 进程池运行函数
process_pool = ProcessPoolExecutor(max_workers=5)

if __name__ == "__main__":
    for i in range(10):
        fut = process_pool.submit(func, i)
        print(fut)


'''
因为之后大家去使用asyncio去进行并发编程的时候
    当前这个库不支持协程
'''