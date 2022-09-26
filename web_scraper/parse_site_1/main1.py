from tqdm import tqdm
from web_scraper.parse_site_1.page_parser_1 import Parser1


p = Parser1()
for page_link in tqdm(p.generate_7fon_links_in_range(2,10)):
    p.parse_7fon_page(page_link)
