# -*- coding: utf-8 -*-
# @Time: 9:20 下午
# @Author: 顾安
# @File: uvloop_test
# Software: PyCharm


import asyncio
import uvloop

# 设置事件循环为uvloop

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def test():
    await asyncio.sleep(2)
    return '123'


async def main():
    task = await test()
    print(task)


asyncio.run(main())

