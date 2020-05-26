from requests_html import HTMLSession
from time import time, sleep

with open('links.csv', 'r', encoding='utf-8') as f:
    with open('result.csv', 'w', encoding='utf-8') as f2:
        f2.write(f'Domain\tThematic\n')

        for link in f:
            link = link.strip()
            key = 'site:' + link + ' ' + 'casino'

            print(f'Send request for key: [{key}]')

            sleep(5)

            with HTMLSession() as session:
                try:
                    response = session.get(
                        f'https://www.google.com/search?q={key}&num=100&hl=en')
                    if response.status_code != 200:
                        raise ValueError('Status code is not 200')

                    status = 'No'
                    thematic = response.html.xpath('//div[@class="r"]/a[1]/@href')
                    for status in thematic:
                        if status:
                            status = 'Yes'

                            result = f'{link}\t{status}\n'
                            with open('result.csv', 'a', encoding='utf-8') as f2:
                                f2.write(result)

                except Exception as e:
                    print(type(e), e)

                    found = 'Banned by Google'

