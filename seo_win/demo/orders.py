import pdb
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import db


engine = db.sa.create_engine(db.dsn)
conn = engine.connect()

hwords = ['purchase', 'order', 'quote', 'account']
awords = ['purchase', 'cart', 'order', 'place', ' now']


def get_order_links():
    count = conn.execute('select count(id) from domains;')
    count = [x[0] for x in count][0]
    n = count // 100 + 1

    for i in range(101):
        print(i*n)
        for d in conn.execute(f'select * from domains limit {n} offset {i*n};'):
            if d.orderlinks:
                print('orderlinks exists', d.domain, d.id)
                continue
            content = str(d.content)
            domain = 'http://' + str(d.domain) + '/'
            dom = BeautifulSoup(content, 'lxml')
            orders = set()
            for tag in dom.find_all('a'):
                if any([hw in str(tag.get('href')).lower() for hw in hwords]) \
                        or any([aw in str(tag.text).lower() for aw in hwords]):
                    link = urljoin(domain, tag.get('href'))
                    orders.add(link)
            
            if len(orders) > 0:
                orderlinks = '\n'.join(list(orders))
                conn.execute(db.domain.update().values(orderlinks=orderlinks).where(db.domain.c.id == d.id))
            
            print('OK', len(orders), d.domain, d.id)


def set_order_links():
    data = []
    i = 0
    with open('orderforms.txt', 'r', encoding='utf-8') as f:
        for line in f:
            i+=1
            print(i)
            x = line.split('\t')
            data.append({'id': x[0].strip(), 'domain': x[1].strip(), 'orderlinks': x[2].strip()})
    for d in data:
        print(d)
        try:
            conn.execute(db.domain.update().values(**d).where(db.domain.c.id == d['id']))
        except Exception as e:
            print(type(e), e)
    print('All done')


if __name__ == '__main__':
    #get_order_links()
	set_order_links()
