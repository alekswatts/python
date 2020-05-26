import os
import gc
import pdb
import sys
import socket
from time import sleep
from selenium import webdriver
from db import sa, dsn, domain
from concurrent.futures import ThreadPoolExecutor


executor = ThreadPoolExecutor(max_workers=4)


engine = sa.create_engine(dsn)
conn = engine.connect()


def save_to_db(data):
    print (data)
    conn.execute(domain.insert().values(**data))
    #conn.execute(domain.update().values(**data).where(domain.c.domain == data['domain']))


def main():
    domainsindb = set([d[0] for d in conn.execute('select domain from domains;')])
    #domainsindb = set([d[0] for d in conn.execute('select domain from domains where title is null;')])
    with open('data/domains.txt', 'r', encoding='utf-8') as f:
        domains = set([line.strip() for line in f])
    domains_queue = domains - domainsindb
    #domains_queue = domainsindb
    #pdb.set_trace()
    print (domains_queue)
    print(len(domains_queue), 'Domains in Queue')

    _options = webdriver.chrome.options.Options()
    _options.add_argument('--headless')
    _options.add_argument('--no-sandbox')
    _options.add_argument('--disable-notifications')
    _options.add_argument('--proxy-server=http://50.31.109.248:3128')
    _driver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
    browser = webdriver.Chrome(chrome_options=_options, executable_path=_driver)
    browser.set_page_load_timeout(10)

    for dom in domains_queue:
        # pdb.set_trace()
        try:
            url = 'http://' + dom + '/'
            browser.get(url)
            sleep(0.2)
            data = dict()
            data['content'] = browser.page_source
            try:
                data['ip'] = socket.gethostbyname(dom)
            except Exception:
                data['ip'] = '0.0.0.0'
            data['domain'] = dom
            data['title'] = str(browser.title)[:250]
            executor.submit(save_to_db, data)
            print('[OK]', dom)
        except Exception as e:
            try:
                print(type(e), e, 'line: ', sys.exc_info()[-1].tb_lineno)
                browser.quit()
                sleep(3)
                del (browser)
                gc.collect()
                browser = webdriver.Chrome(chrome_options=_options, executable_path=_driver)
            except Exception:
                print('Error')
            # browser.stop_client()
            # browser.close()
            
    else:
        # browser.stop_client()
        # browser.close()
        browser.quit()
        del (browser)


def order_main():
    engine = sa.create_engine(dsn)
    conn = engine.connect()

    _options = webdriver.chrome.options.Options()
    _options.add_argument('--headless')
    _options.add_argument('--no-sandbox')
    _options.add_argument('--disable-notifications')
    _options.add_argument('--proxy-server=http://50.31.109.248:3128')
    _driver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
    browser = webdriver.Chrome(chrome_options=_options, executable_path=_driver)

    #for d in conn.execute('select id, orderlinks from domains where orderlinks is not null and ordercontent is null;'):
    for d in conn.execute('select id, orderlinks from domains where orderlinks is not null;'):
        try:
            browser.get(d.orderlinks)
            sleep(0.5)
            conn.execute(domain.update().values(ordercontent=browser.page_source).where(domain.c.id == d.id))
            print(d.id)
        except Exception as e:
            print(type(e), e)


if __name__ == '__main__':
    #main()
    order_main()
