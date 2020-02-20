from requests_html import HTMLSession
from reppy.robots import Robots
import time


class Text:
    body = None

    def __init__(self, body):
        self.body = body

    def clean_text(self):
        return self.body.strip()

    def get_length(self):
        return len(self.body)


class Link(Text):
    def __init__(self, body):
        self.body = body
        robots_url = body + '/robots.txt'
        self.fetched = Robots.fetch(robots_url)

    def check_robots(self):
        if not self.fetched.allowed(self.body, '*'):
            return False
        else:
            return True


class Meta(Text):
    title = None
    h1 = None

    def __init__(self, parser):
        self.body = parser.get_response()

        try:
            title = self.body.html.xpath('//title')[0].text
        except Exception as e:
            title = 'No Title'
        try:
            h1 = self.body.html.xpath('//description')[0].text
        except Exception as e:
            h1 = 'No Description'


class Parser(Link):

    def get_response(self):
        with HTMLSession() as session:
            response = session.get(self.body)
        return response


link = Link('https://netflix.com').check_robots()
pars = Parser('https://netflix.com')

