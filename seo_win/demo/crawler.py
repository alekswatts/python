import os
import gc
import pdb
import sys
import socket
from time import sleep
from selenium import webdriver
from db import sa, dsn, domain
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import or_


executor = ThreadPoolExecutor(max_workers=4)


engine = sa.create_engine(dsn)
conn = engine.connect()
fprint = {'Essayexperts': 
('var essay_pricelist = [{"types": ["Essay"], "urgencies":', 'var chat = new live_chat([{"id":', '<form method="post" id="formID"'), 
'Custom-writing.org': 
('mmy2r8b8', '1043927c1b', 'blJTN0BXXUBZUE1eDVcYZBFbGVpdXFZBGRJRRw'),
'Speedypaper':
('YlQDYBdWXhBZVRVbDVseIFcRXl8NF2o2WxhPbSBEDHRcCl1YFXoHWUEERhZrcSBwdQ5cFkdeDVgARXAFSlkPRgdbVT5GAEdf',),
'Netfix': 
('la_x2s6df8d', '<input name="authenticity_token"'),
'New company 3': 
('article11-cls-1', 'btn btn-orange btn-block', 'M2249.7 280.1c-1 6.3-5.8 6.3-10.4 6.3h-2.6l1.9-11.7c.1-.7.7-1.2 1.4-1.2h1.2c3.2 0 6', '2VP53W6KLz5VFMNHluSW6RTHHFFZN4m0', 'order#before-checkout'),
'Boosta': 
('37edb83.js', '2aNK8BsvxtNwghN0d6joK2L7A9XVux9U', '/js2/fast-signup/fs.min.js', 'clientpanel.onlin'),
'Ultius':
('bea81213dc2cb17dd4052fdf2bc9ad85',),
'Trionika':
('/public/js/data_count_price.js', '164668289224369965', 'type_of_paper = client_id +', '?empty=1%pid=', 'iframe%empty=1%sub_id'),
'Govitall':
('xwzASiZfXmIZvbjoYBIdDdw55lTdDa09', '4Kr5tM4V9WuxYQloStkq3nVIKnEu7sRe', 'of-special-offer-popup'),
'Uvocorp':
('popup__discount__modal-body-main-text', '2e001083-1ade-4856-a434-309f6b6efa55', 'phTvFPEsiJdeFlMywk7RrXUcmCbV4Ygp', '<div class="old-browser-banner">You are using an <strong>outdated</strong> browser', 'data-finder="page.dalog.link.forgotpass">Forgot your password?</a>', 'id="current_auth_container"', 'order-form.php?academicLevel', 'id_esauth_myaccount_login_link'),
'Customessaymeister':
('vjnc7kia',),
'ivoryresearch':
('F9538F24-0413-436D-81C4-CAAA20BE7074',),
'Ukessays':
('4VMOYiSgxVvvYHqDuojZl9cAehGUmDcB',),
'Devellar':
('js-error-log.js',),
'Ukdissertation.co.uk':
('VpeWMuMKq5MXumarlV5yVnbKHrcebHjD',),
'ThePaperExperts':
('secureonlineorder.net',),
'SwiftPapers':
('value="Doesn`t matter"',),
'Professay':
('UA-9836363', '/java/order-processing.js'),
'Perfectessay':
('<div class="flc_txt">LiveChat</div>', '3YdpQ9yNhMMPsYabQ5TmpI4Q6KE2laD6', '2G3GiywvsRx59STqHkyaSCwmEQGD4QuN', '56f5c67d479b17744b2a780d', 'site_id=129587'),
'Papermoz':
('/webpages/client/ordermanagement/', 'id=1457296661220722'),
'Oxbridgeessays':
('GTM-5WTCXJ',),
'New company 1':
('26IWglpakrUKbfdRc0v0uaTafy28mGLG',),
'Livingstone':
('2sd0on2NLwFMOEzhtahKfm1QUIF2Z5E9',),
'New company 2':
('window.__lc.license = 3371042;', 'licence/3371042'),
'EssayWritingServices':
('shinyessays.com', '1wG96FtnktgEx0oMQnwa4UEMKmkwcX4a')


}

def save_to_db(data):
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
            for key, value in fprint.items():
                for footprint in value:
                    if footprint in data['content']:
                       data['company'] = key
                       print ('Footprint checked, company: ', key)
                       break
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


def set_company():
    engine = sa.create_engine(dsn)
    conn = engine.connect()

    for key, value in fprint.items():
        i=1
        print (key)
        try:
            for footprint in value:
                print (i, 'footprint: ', footprint)
                #conn.execute(domain.update().values(company=key).where(or_(domain.c.content.like('%'+footprint+'%'),domain.c.ordercontent.like('%'+footprint+'%'))))
                i+=1
        except Exception as e:
            print(type(e), e)

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

    for d in conn.execute('select id, orderlinks from domains where orderlinks is not null and ordercontent is null;'):
    #for d in conn.execute('select id, orderlinks from domains where orderlinks is not null;'):
        try:
            print (d)
            browser.get(d.orderlinks)
            comp = None
            for key, value in fprint.items():
                for footprint in value:
                    if footprint in browser.page_source:
                       comp = key
                       print ('Footprint checked, company: ', key)
                       break
            sleep(0.5)
            conn.execute(domain.update().values(ordercontent=browser.page_source, company=comp).where(domain.c.id == d.id))
            print(d.id)
        except Exception as e:
            print(type(e), e)

if __name__ == '__main__':
    #main()
    order_main()
    #set_company()
