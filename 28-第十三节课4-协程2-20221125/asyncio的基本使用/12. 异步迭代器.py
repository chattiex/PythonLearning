# -*- coding: utf-8 -*-
# @Time: 8:55 下午
# @Author: 顾安
# @File: 异步迭代器
# Software: PyCharm


import asyncio


# 自定义异步迭代器
class Reader:
    def __init__(self):
        self.count = 0

    async def readline(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    # 迭代器执行的代码一般为IO耗时操作
    # 协程函数
    async def __anext__(self):
        val = await self.readline()
        if val is None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    # 异步for循环必须在协程函数内执行，协程函数名称随意取名
    async for item in obj:
        print(item)


asyncio.run(func())
