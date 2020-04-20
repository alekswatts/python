import urllib.request
from bs4 import BeautifulSoup
import json
import re


filename = open('xuk_life.csv', 'r', encoding='utf-8')
file = filename.read()
file = file.split()
file.pop(0)


def image_collect(page):
    html_page = urllib.request.urlopen(page)
    soup = BeautifulSoup(html_page, "lxml")
    print(soup)
    #final_result = list()
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href.endswith('.jpg'):
            continue
        if href.endswith('.com/'):
            continue
        final_result.append(href)
        print('Collecting links. Please, wait. ')

    return final_result


final_result = list()

link_list = list()
for page in file:
    link_list.append(image_collect(page))
print(link_list)
with open('results.json', 'w', encoding='utf-8') as f:
    json.dump(link_list, f)





