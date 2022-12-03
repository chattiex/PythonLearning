# -*- coding: utf-8 -*-
# @Time: 8:05 下午
# @Author: 顾安
# @File: 8. 关于await的使用
# Software: PyCharm


import asyncio


async def main():
    # 获取当前正在运行的事件循环
    loop = asyncio.get_running_loop()  # 官方文档
    # 创建任务 future对象 当前对象没有绑定任何任务
    fut = loop.create_future()
    # 等待任务结果 因为当前future对象没有绑定任何任务 也就没有返回值
    await fut


asyncio.run(main())



