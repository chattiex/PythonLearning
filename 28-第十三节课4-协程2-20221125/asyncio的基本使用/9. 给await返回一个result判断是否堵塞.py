# -*- coding: utf-8 -*-
# @Time: 8:18 下午
# @Author: 顾安
# @File: 9. 给await返回一个result判断是否堵塞
# Software: PyCharm


import asyncio


async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('这是自己设置的结果')


async def main():
    # 获取系统层面的事件循环
    loop = asyncio.get_running_loop()

    # 创建一个future对象
    fut = loop.create_future()

    # 手动设置future任务的最终结果
    await loop.create_task(set_after(fut))

    # 获取future对象中的结果
    data = await fut
    print(data)


asyncio.run(main())


'''
通过当前案例 我们发现可以对future对象手动的返回一个结果
    用于解堵塞
'''




