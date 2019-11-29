from requests_html import HTMLSession

url = 'https://netflix.com'


class Website:
    def __init__(self):
        self.url = url
        self.domain = url.split('/')[2]

class Title:
    def __init__(self, urls):
        with HTMLSession as session:
            self.resp = session.get(urls)
            self.title = self.resp.html.xpath('//title')[0].text

class Description:
    def __init__(self, urls):
        with HTMLSession as session:
            self.resp = session.get(urls)
            self.description = self.resp.html.xpath('//description')[0].text


result_url = Website(url)

print(result_url)

