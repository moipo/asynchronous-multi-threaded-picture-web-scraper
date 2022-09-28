from .parser_1 import Parser1
from .parser_2 import Parser2
from threading import *
import os
import pathlib

def start(img_qua):

    pictures_path = os.path.join(pathlib.Path(__file__).parent.parent.resolve(), "pictures")
    # os.rmdir(pictures_path)
    # os.mkdir(pictures_path)
    os.startfile(pictures_path)

    #
    # p1 = Parser1()
    # p2 = Parser2()
    #
    # quantity = {"img_qua" : img_qua}
    #
    # t1 = Thread(target=p1.parse_pages_in_range,args = (1,1000,quantity))
    # t2 = Thread(target=p2.parse_pages_in_range,args = (1,1000,quantity))
    #
    # t1.start()
    # t2.start()
    #
    # t1.join()
    # t2.join()





