from time import time
from requests_html import HTMLSession
from reppy.robots import Robots

domain = 'xuk.life'
home_url = f'https://{domain}/erotic/teen'
robots_url = home_url + 'robots.txt'
robots = Robots.fetch(robots_url)

filename = domain.replace('.', '_') + '.json'

result_file = open(filename, 'w', encoding='utf-8')

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

    response_time = round(t2 - t1, 2)

    result = f'{url}\n'

    result_file.write(result)

    for link in response.html.absolute_links:
        if '#' in link:
            link =link.split('#')[0]
            continue

        if link.endswith('.jpg'):
            continue

        if domain not in link:
            continue

        if '/teen/' not in link:
            continue

        if link in parsed_urls:
            continue

        if not robots.allowed(link, '*'):
            continue

        if link not in queue_urls:
            queue_urls[link] = level + 1

print('Website is parsed!')



