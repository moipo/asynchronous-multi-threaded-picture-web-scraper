import requests
import asyncio
import aiohttp
from time import time

def write_image(data):
    filename = f'pictures/loremflicker-{int(time()*1000)}.jpeg'
    with open(filename, 'wb') as f:
        f.write(data)

async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_image(data)

async def async_parsing(quantity):
    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        while quantity["thread_1"] > 0:
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
            quantity["thread_1"]-=1

        await asyncio.gather(*tasks)
