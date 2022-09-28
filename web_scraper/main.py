from parsing.mtpws import start


#validationerror

img_qua = int(input("Input the amount of pictures you'd like to download:"))
if type(img_qua) == int: start(img_qua)
