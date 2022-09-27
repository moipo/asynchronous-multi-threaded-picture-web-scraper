from .parser_1 import Parser1
from .parser_2 import Parser2
from threading import *


def start():

    p1 = Parser1()
    p2 = Parser2()

    t1 = Thread(target=p1.parse_pages_in_range,args = (2,5))
    t2 = Thread(target=p2.parse_pages_in_range,args = (2,5))

    t1.start()
    t2.start()

    t1.join()
    t2.join()





