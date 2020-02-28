from pprint import pprint
import urllib.request

from bs4 import BeautifulSoup

filename = open('stardevine_com.csv', 'r', encoding='utf-8')
file = filename.read()
file = file.split()
file.pop(0)
file.pop(0)


def image_collect(page):
    html_page = urllib.request.urlopen(page)
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        href = link.get('href')
        if not href.endswith('jpg'):
            continue
        if href.endswith('.com/'):
            continue
        final_result = list()
        final_result.append(href)
        print(final_result)


final_result = list()
for page in file:
    final_result.append(image_collect(page))








