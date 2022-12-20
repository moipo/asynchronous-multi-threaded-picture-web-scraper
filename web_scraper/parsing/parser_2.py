#target: https://nicefon.ru/

import requests

def parse2( quantity):
    cnt = 0
    while quantity["img_qua"] != 0:
        img_response = requests.get("https://loremflickr.com/320/240")
        with open("pictures/loremflickr{num}.jpeg".format(num = cnt), "wb") as img:
            img.write(img_response.content)
            cnt+=1
            print(type(quantity))
            quantity["img_qua"] -= 1
