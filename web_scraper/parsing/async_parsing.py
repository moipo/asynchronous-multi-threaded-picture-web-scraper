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

async def async_parsing():
    url = "https://loremflickr.com/320/240"
    tasks = []

    async with aiohttp.ClientSession() as session:
        for i in range(20):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)
