#target: https://nicefon.ru/

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm



class Parser2:
    def __init__(self):
        self.cnt = 1

    def parse_one_page(self, link):
        response = requests.get(link)
        soup = BeautifulSoup(response.text,"html.parser")
        soup = soup.find('div', id = "images-listview").findAll("img")
        for i in soup:
            image_link = i.get("src")
            img_response = requests.get(image_link)
            with open("pictures/nicefon_img_{num}.jpg".format(num = self.cnt), "wb") as img:
                img.write(img_response.content)
            self.cnt += 1


    def parse_pages_in_range(self, start_page, last_page ):
        if start_page <= 0: start_page = 1
        for i in tqdm(range(start_page,last_page)):
            self.parse_one_page(f"https://nicefon.ru/nav/page-{i}.html")




