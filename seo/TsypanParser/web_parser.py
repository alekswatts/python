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
    print(parsed_urls)
    return parsed_urls


parsed_links = parser(domain)


