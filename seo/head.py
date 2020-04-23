from requests_html import HTMLSession


class Head:
    def __init__(self, link):
        with HTMLSession() as session:
            response = session.get(link)

        self.title = response.html.xpath('//title')[0].text
        self.description = response.html.xpath('//meta [@name="description"]/@content')
        str_desc = ''.join(self.description)

        print('Link: ', link)
        print('Title: ', self.title)
        print('Description: ', str_desc)


link = Head('https://py4you.com')
