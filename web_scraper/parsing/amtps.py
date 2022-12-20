import asyncio
from threading import *
import pathlib
import shutil
import os
import subprocess, sys

from .parsing import Parser
from .async_parsing import async_parsing

def start(total_img_amount):

    pictures_path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "pictures")

    if os.path.isdir(pictures_path):
        shutil.rmtree(pictures_path)
    os.mkdir(pictures_path)

    try:
        os.startfile(pictures_path)
    except:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, pictures_path])

    thread_1_img_amount = (total_img_amount*3)//4
    thread_2_img_amount = total_img_amount - thread_1_img_amount

    quantity = {
    "thread_1" : thread_1_img_amount,
    "thread_2" : thread_2_img_amount,
    }

    prsr = Parser()

    t1 = Thread(target=asyncio.run,args = (async_parsing(quantity),))
    t2 = Thread(target=prsr.parse_pages_in_range,args = (1,1000,quantity))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
