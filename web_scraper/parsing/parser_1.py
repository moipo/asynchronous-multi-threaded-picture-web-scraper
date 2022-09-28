# target: https://7fon.org/

import requests
from bs4 import BeautifulSoup


class Parser1:

    def __init__(self):
        self.cnt = 0

    def parse_one_page(self,page_link,quantity):
        response = requests.get(page_link)
        soup = BeautifulSoup(response.text, "html.parser")
        soup = soup.findAll('div' , id = "tmbox")
        for tmbox in soup:
            if tmbox.img is not None:
                self.cnt += 1
                quantity["img_qua"] -= 1
                if quantity["img_qua"] <= 0: exit()
                download_it = "https:" + str(tmbox.img.get('src'))
                img_content = requests.get(download_it)
                with open(f"pictures/7fon_img_{self.cnt}.png", "wb" ) as picture:
                    picture.write(img_content.content)



    def __generate_links_in_range(self,start_page, last_page):
        base_link = "https://7fon.org/"
        res = []
        current_link:str
        for num in range(start_page,last_page):
            if num == 1: current_link = base_link
            else: current_link = base_link + "Обои/%s.html" % num
            res.append(current_link)
        return res


    def parse_pages_in_range(self, start_page, last_page, quantity):
        for link in self.__generate_links_in_range(start_page, last_page):
            self.parse_one_page(link,quantity)
            print("images left to download: ", quantity["img_qua"])
