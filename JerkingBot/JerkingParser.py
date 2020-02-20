from time import time
from requests_html import HTMLSession
import sys
from pathlib import Path
from urllib.parse import urljoin

def jerking_parser():
    domain = 'stardevine.com'
    home_url = f'http://{domain}/'

    filename = domain.replace('.', '_') + '.csv'

    result_file = open(filename, 'w', encoding='utf-8')
    result_file.write('URL\tIMG\n')

    parsed_urls, queue_urls = set(), dict()

    queue_urls[home_url] = 1

    while len(queue_urls) > 0:

        min_level = min(queue_urls.values())

        for key, value in queue_urls.items():
            if value == min_level:
                url = key
                level = queue_urls.pop(url)
                break

        print('Scan: ', url)

        parsed_urls.add(url)

        with HTMLSession() as session:
            t1 = time()
            response = session.get(url)
            t2 = time()
        try:
            parsed_body = html.fromstring(response.text)
            img = parsed_body.xpath('//img/@src')[0].text
        except Exception as e:
            img = 'Not found'

        response_time = round(t2 - t1, 2)

        result = f'{url}\t{img}\n'

        result_file.write(result)

        for link in response.html.absolute_links:
            if '#' in link:
                link = link.split('#')[0]
                continue

            if link.endswith('.xml'):
                continue

            if domain not in link:
                continue

            if link in parsed_urls:
                continue
            if link not in queue_urls:
                queue_urls[link] = level + 1

    print('Website is parsed!')


jerking_parser()
