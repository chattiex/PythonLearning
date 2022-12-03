# -*- coding: utf-8 -*-
# @Time: 8:40 下午
# @Author: 顾安
# @File: 11. 交叉编程
# Software: PyCharm


import time
import asyncio
import concurrent.futures


def func_1():
    time.sleep(2)
    return '测试'


async def main():
    loop = asyncio.get_running_loop()
    # 在协程函数中运行普通函数 在执行函数时，协程内部会自动创建一个线程池来运行任务
    # run_in_executor()方法第一个参数为None时则默认创建一个线程池
    fut = loop.run_in_executor(None, func_1)
    # await 可以运行由事件循环创建的线程池
    result = await fut
    print('当前方式会自动创建一个线程池去执行普通函数: ', result)

    # 在协程函数中运行基于线程池的任务, 效果与以上代码一致
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func_1)  # 如果在协程函数中运行线程池 必须使用run_in_executor
        print('在线程池中得到的执行结果: ', result)

    # 在协程函数中运行基于进程池的任务
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func_1)
        print('在进程池中得到的执行结果: ', result)


if __name__ == "__main__":
    asyncio.run(main())


"""
1. 在协程函数中可以运行一个线程池，但是这个协程池必须由事件循环处理
    run_in_executor:如果不是一个协程对象通过该方法进行调用
    run_in_executor默认会创建一个线程池
    如果自己手动创建也必须使用run_in_executor去执行自己手动创建的线程池

2. 如果在协程函数中自己手动的创建了一个线程池
    则必须使用run_in_executor进行调用

3. 手动创建进程池
    run_in_executor运行进程池对象
    
    
对之前对老项目进行重构
    线程去完成的
"""