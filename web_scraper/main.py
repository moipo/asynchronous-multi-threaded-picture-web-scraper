from parsing.mtpws import start




def validate(img_qua:str):
    if isinstance(img_qua, str) and 1 <= int(img_qua) <= 100000000: pass
    else: raise TypeError("The amount of images must be a positive integer and not higher than 10000000")

inp = input("Input the amount of pictures you'd like to download: ")
validate(inp)
start(int(inp))
