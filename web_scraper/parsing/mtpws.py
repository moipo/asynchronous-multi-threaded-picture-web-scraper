from .parser_1 import Parser1
from .parser_2 import Parser2


def start():

    p1 = Parser1()
    p2 = Parser2()

    p2.parse_pages_in_range(2, 5)
    p1.parse_pages_in_range(2,5)
