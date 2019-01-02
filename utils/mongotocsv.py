# -*- coding: utf-8 -*-
# @Time : 2019/1/2 7:28 PM
# @Author : cxa
# @File : mongotocsv.py
# @Software: PyCharm
from db.mongohelper import get_data
import asyncio
import aiofiles
import pathlib


async def m2f():
    data = await get_data()
    async for item in data:
        t = item.get("content").get("message").strip()
        fs = await aiofiles.open(pathlib.Path.joinpath(pathlib.Path.cwd().parent, "msg.txt"), 'a+')
        await fs.write(t)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(m2f())
