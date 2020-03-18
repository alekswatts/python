from seo.TsypanParser.web_parser import *


def google_index_status(parsed_links):

    for link in parsed_links:
        link = link.strip()
        time.sleep(3)
        print(f'Send request for: [{link}]')

        with HTMLSession() as session:
            try:
                response = session.get(
                    f'https://www.google.com/search?q={link}&num=100&hl=en')
                print(response)
                if response.status_code != 200:
                    raise ValueError('Status code is not 200')
            except Exception as e:
                print(type(e), e)
                links = []
                found = 'Banned by Google'


google_index_status(parsed_links)