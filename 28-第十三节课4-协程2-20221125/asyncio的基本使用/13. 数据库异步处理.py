# -*- coding: utf-8 -*-
# @Time: 9:04 下午
# @Author: 顾安
# @File: 13. 数据库异步处理
# Software: PyCharm


import asyncio


class AsyncContextManager:
    def __init__(self, conn=None):
        self.conn = conn

    async def do_something(self):
        # 异步操作数据库
        return 'crud'

    async def __aenter__(self):
        # 异步连接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库连接
        await asyncio.sleep(1)


async def func():
    # 上下文管理器处理也需要在协程函数中运行
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)


asyncio.run(func())
