from .parser_1 import Parser1
from .parser_2 import parse2
import asyncio
from .async_parsing import async_parsing
from threading import *

import pathlib
import shutil

import os
import subprocess, sys

def start(img_qua):

    pictures_path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "pictures")

    if os.path.isdir(pictures_path):
        shutil.rmtree(pictures_path)
        os.mkdir(pictures_path)
    else: os.mkdir(pictures_path)


    try:
        os.startfile(pictures_path)
    except:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, pictures_path])


    asyncio.run(async_parsing())
    img_qua-=20

    p1 = Parser1()

    quantity = {"img_qua" : img_qua}

    t1 = Thread(target=p1.parse_pages_in_range,args = (1,1000,quantity))
    t2 = Thread(target=parse2,args = (dict(quantity),))


    t1.start()
    t2.start()

    t1.join()
    t2.join()
