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

        paragraph = response.html.xpath('//p/text()')
        print(paragraph)
        print(len(paragraph))


text_value(parsed_links)