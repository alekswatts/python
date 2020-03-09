from pprint import pprint
from requests_html import HTMLSession
import requests
import time

domain = 'https://py4you.com'


def parser(domain):
    parsed_urls, queue_urls = set(), dict()

    queue_urls[domain] = 1

    while len(queue_urls) > 0:

        min_level = min(queue_urls.values())

        for key, value in queue_urls.items():
            if value == min_level:
                url = key
                level = queue_urls.pop(url)
                break

        parsed_urls.add(url)

        with HTMLSession() as session:
            response = session.get(url)

        for link in response.html.absolute_links:
            if '#' in link:
                link =link.split('#')[0]
                continue

            if link.endswith('.jpg'):
                continue

            if domain not in link:
                continue

            if link in parsed_urls:
                continue
            if link not in queue_urls:
                queue_urls[link] = level + 1

    print('Website is parsed!')
    return parsed_urls


final_result = parser(domain)


def google_index_status(final_result):

    for link in final_result:
        link = link.strip()
        time.sleep(2)
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        headers = {'User-Agent': user_agent}
        response = requests.get(link, headers=headers)
        print(f'Send request for: [{link}]')

        with HTMLSession() as session:
            try:
                response = session.get(
                    f'https://www.google.com/search?q={link}&num=100&hl=en')
                if response.status_code != 200:
                    raise ValueError('Status code is not 200')
            except Exception as e:
                print(type(e), e)
                links = []
                found = 'Banned by Google'


google_index_status(final_result)