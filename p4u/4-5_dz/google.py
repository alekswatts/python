from requests_html import HTMLSession
from time import time

domain = 'netflix.com'
t1 = time()

# took all keywords from file
with open('netflix_keys.txt', 'r', encoding='utf-8') as f:

    with open('results.csv', 'w', encoding='utf-8') as f2:
        f2.write(f'Keyword\tDomain\tPosition\n')
        for key in f:
            key = key.strip()
            print(f'Send request for key: [{key}]')

            with HTMLSession() as session:
                try:
                    resp = session.get(
                        f'https://www.google.com/search?q={key}&num=100&hl=en')
                    if resp.status_code != 200:
                        raise ValueError('Status code is not 200')

                    links = resp.html.xpath('//div[@class="r"]/a[1]/@href')
                except Exception as e:
                    print(type(e), e)
                    links = []
                    found = 'ban_google'

            for position, url in enumerate(links, start=1):
                if domain in url:
                    result = f'{key.strip()}\t{url}\t{position}\n'
                    with open('results.csv', 'a', encoding='utf-8') as f2:
                        f2.write(result)

t2 = time()
print(f'All done!')
print('Working time is: ', round(t2 - t1, 4), ' seconds')
