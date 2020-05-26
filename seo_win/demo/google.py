import os
import sys
# import pdb
import random
from lxml import html
from time import sleep
from urllib.parse import quote
from selenium import webdriver
from python3_anticaptcha import NoCaptchaTaskProxyless
from yarl import URL


def get_results(code):
    sites = html.fromstring(code).xpath('//h3[@class="r"]/a/@href')
    if len(sites) == 0:
        raise ValueError('no websites in result page')
    return sites


def understand_captcha(url, browser, proxy, UA):
    # Captcha Solving
    print('Captcha solving....')
    api_key = '5d7715dba5393cc85562e9177751bd4e'
    site_key = browser.find_element_by_id('recaptcha').get_attribute('data-sitekey')
    _result = NoCaptchaTaskProxyless(anticaptcha_key=api_key).captcha_handler(websiteURL=url, websiteKey=site_key)
    print(_result)
    captcha_result = _result.get('solution').get('gRecaptchaResponse')
    browser.execute_script("document.getElementById('g-recaptcha-response').style.display = '';")
    browser.execute_script(f"document.getElementById('g-recaptcha-response').value = '{captcha_result}'; ")
    browser.execute_script("document.getElementsByName('submit')[0].click();")
    return browser


def crawler(country='US'):
    '''
    AU,Australia,Sydney,103.4.17.44:80
    AU,Australia,,103.18.40.30:80
    AU,Australia,Brisbane,103.4.19.254:80
    US,United States,Smarr,192.184.95.44:80
    US,United States,Las Vegas,67.203.0.119:80
    !US,United States,New York,104.254.57.24:80
    US,United States,Las Vegas,67.203.1.202:80
    US,United States,Saint Louis,66.165.113.226:3128
    US,United States,Chicago,50.31.9.155:3128
    GB,United Kingdom,Thornton Heath,31.132.1.186:3128
    GB,United Kingdom,,77.75.126.205:3128
    GB,United Kingdom,,77.75.126.215:3128
    '''

    keys = []

    proxy = {'US': 'http://104.254.57.24:80',
             'UK': 'http://77.75.126.205:3128',
             'AU': 'http://103.4.17.44:80',
             'CA': 'http://192.184.95.44:80'}

    google = {'US': 'google.com', 'UK': 'google.co.uk', 'AU': 'google.com.au', 'CA': 'google.ca'}

    result_file = f'data/google_sites_result_{country}.txt'
    input_file = f'data/google_input_keys_{country}.txt'
    parsed_file = f'data/google_parsed_keys_{country}.txt'

    with open(parsed_file, 'r', encoding='utf-8') as f1:
        result = f1.read()

    with open(input_file, 'r', encoding='utf-8') as f2:
        for line in f2:
            key = line.strip()
            if key not in result:
                keys.append(key)

    print(len(keys), 'Keys in Queue')

    UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
    _options = webdriver.chrome.options.Options()
    # _options.add_argument('--headless')
    # _options.add_argument('--no-sandbox')
    _options.add_argument('--disable-notifications')
    _options.add_argument(f'--proxy-server={proxy[country]}')
    _driver = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
    browser = webdriver.Chrome(chrome_options=_options, executable_path=_driver)

    for k in keys:
        try:
            print('[SEND]', k)
            url = f'https://www.{google[country]}/search?q={quote(k)}&num=100'
            browser.get(url)
            sleep(random.randint(3, 7))
            code = browser.page_source
            if 'recaptcha' in code:
                browser = understand_captcha(url, browser, proxy, UA)
                code = browser.page_source
            sites = get_results(code)
            with open(result_file, 'a', encoding='utf-8') as result:
                for s in sites:
                    # result.write('{}\t{}\n'.format(k, s))
                    result.write(f'{URL(s).host}\n')
            with open(parsed_file, 'a', encoding='utf-8') as parsed:
                parsed.write(f'{k}\n')
            print('[OK]', k)
            sleep(random.randint(2, 8))
        except Exception as e:
            print(type(e), e, 'line: ', sys.exc_info()[-1].tb_lineno)
            browser.quit()
            browser = webdriver.Chrome(chrome_options=_options, executable_path=_driver)
    browser.quit()


def main():
    countries = ['US', 'UK', 'AU', 'CA']
    for c in countries:
        crawler(c)


if __name__ == '__main__':
    main()
