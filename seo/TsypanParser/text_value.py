from pprint import pprint
from seo.TsypanParser.web_parser import *


def text_value(parsed_links):

    for link in parsed_links:
        link = link.strip()
        print(f'Send request for key: [{link}]')
        with HTMLSession() as session:
            try:
                response = session.get(link)
                if response.status_code != 200:
                    raise ValueError('Blocked! Website is protected by Firewall!')
            except Exception as e:
                print(type(e), e)

        h1 = response.html.xpath('//h1/text()')
        h2 = response.html.xpath('//h2/text()')
        h3 = response.html.xpath('//h3/text()')
        h4 = response.html.xpath('//h4/text()')
        h5 = response.html.xpath('//h5/text()')
        heading = h1+h2+h3+h4+h5
        paragraph = response.html.xpath('//p/text()')
        print(heading)
        pprint(paragraph)


text_value(parsed_links)