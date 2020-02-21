from pprint import pprint
import urllib.request

from bs4 import BeautifulSoup

filename = open('stardevine_com.csv', 'r', encoding='utf-8')

file = filename.read()

print(file)


def image_collect():
    html_page = urllib.request.urlopen("http://stardevine.com/580-sheri-vi.html")
    soup = BeautifulSoup(html_page, "lxml")
    for link in soup.findAll('a'):
        href = link.get('href')
        if not href.endswith('jpg'):
            continue
        if href.endswith('.com/'):
            continue
        print(href)


image_collect()
