import resp
from requests_html import HTMLSession

domain = 'https://py4you.com'

with open('results.csv', 'w', encoding='utf-8') as f:
    f.write(f'URL\tTitle\tH1\n')


def crawl():
    with HTMLSession() as session:
        try:
            url = session.get(domain)
            if url.status_code != 200:
                raise ValueError("Can't crawl this url")
            urls = url.html.absolute_links
        except Exception as e:
            print(type(e), e)
            print('Something goes wrong!')
    return urls


crawl()


for urls in crawl():
    if domain not in urls:
        continue
    with HTMLSession() as session:
        resp = session.get(urls)
        title = resp.html.xpath('//title')[0].text
        h1 = resp.html.xpath('//h1/text()')
        for headline in h1:
            headline = headline.strip()
            result = f'{urls}\t{title}\t{headline.strip()}\n'
            with open('results.csv', 'a', encoding='utf-8') as f:
                f.write(result)