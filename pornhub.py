import urllib.request
from time import time

import requests
from requests_html import HTMLSession

domain = 'pornhub.com'
key = 'Asian'

t1 = time()


def user_ag():
    url = f'https://{domain}/'
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    headers = {'User-Agent': user_agent}
    response = requests.get(url, headers=headers)

    with HTMLSession() as session:
        resp = session.get(url)
        title = resp.html.xpath('//title')[0].text
    print(title)

user_ag()


def crawler():
    with HTMLSession() as session:
        try:
            resp = session.get(
                f'https://www.google.com/search?q={key}&num=100&hl=en')
            if resp.status_code != 200:
                raise ValueError('Jerking is declined')

            links = resp.html.xpath("//div[@class=\"r\"]/a[1]/@href")
            print(links)
            print(key)

        except Exception as e:
            print(type(e), e)



