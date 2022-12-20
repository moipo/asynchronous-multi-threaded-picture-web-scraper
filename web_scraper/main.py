from parsing.mtpws import start






def validate(img_qua:str):
    if isinstance(img_qua, str) and 20 <= int(img_qua) <= 1000: pass
    else: raise TypeError("The amount of images must be from 20 to 1000")


def main():
    inp = input("Input the amount of pictures you'd like to download (from 20 to 1000): ")
    validate(inp)
    start(int(inp))

if __name__ == "__main__":
    main()
