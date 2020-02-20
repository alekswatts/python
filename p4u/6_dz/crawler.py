
domain = 'casinofreewin.com'

filename = domain.replace('.', '_') + '.csv'

result_file = open(filename, 'w', encoding='utf-8')

parsed_urls = set()

queue_urls = set()

home_url = f'https{domain}/'

queue_urls.add(home_url)