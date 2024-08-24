import re

import requests
from bs4 import BeautifulSoup
url = 'https://rosstat.gov.ru'
rosstat = requests.get(url)

def get_page(site, page_name: str):
    link = site.find("a", string=page_name).get('href')
    page = requests.get(link)
    return BeautifulSoup(page.text,"html.parser")


page_names = ['Статистика', 'Официальная статистика', 'Население']

soup = BeautifulSoup(rosstat.text, "html.parser")

for name in page_names:
    soup = get_page(soup, name)

# print(soup)
class_to_search =['document-list__item-title','document-list__item-info','btn btn-icon btn-white btn-br btn-sm']
population_cnt = 'Численность населения по полу и возрасту'

list_files = soup.find_all(["div","a"], class_=class_to_search)

print(list_files)


# page_link_statistics = get_page("Статистика")
#
# official_statistics_page = (
#     BeautifulSoup(
#         requests.get(page_link_statistics)
#         .text, "html.parser")
#     .find("a", string="Официальная статистика")
#     .get('href')
# )
