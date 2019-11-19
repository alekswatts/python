from requests_html import HTMLSession
from time import time

domain = 'https://netflix.com'
t1 = time()
count = 0

with open('netflix_keys.txt', 'r', encoding='utf-8') as f:
    with open('results.csv', 'w', encoding='utf-8') as f2:
        f2.write(f'Keyword\tDomain\tPosition\n')
        for line in f:
            line = line.strip()
            session = HTMLSession()
            resp = session.get(f'https://www.google.com/search?q={line}&num=100&hl=en')
            links = resp.html.xpath('//div[@class="r"]/a[1]/@href')

            for position, url in enumerate(links, start=1):
                if domain in url:
                    result = f'{line.strip()}\t{url}\t{position}\n'
                    f2.write(result)

t2 = time()
print(f'All done!')
print('Working time is: ', round(t2-t1, 4), ' seconds')