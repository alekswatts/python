from selenium import webdriver
from bs4 import BeautifulSoup
import json

chromedriver = 'C:/bin/chromedriver.exe'
options = webdriver.ChromeOptions()
#options.add_argument('headless')  # для открытия headless-браузера
browser = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)

startUrl = 'https://www.askgamblers.com/online-casinos/reviews'
resultLinks = []
resultData = []

def ScrapeLinks(url):
    browser.get(url)
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html5lib')
    links = soup.find_all("span", {"class": "do-open-info"})
    nextPage = soup.find('a', {"class": "site-pagination__next"})
    for link in links:
        href = link.findNext('a').get('href')
        resultLinks.append('https://www.askgamblers.com' + href)
    if nextPage:
        ScrapeLinks(nextPage.get('href'))

def ScrapeCasino(url):
    result = {}
    browser.get(url)
    requiredHtml = browser.page_source
    soup = BeautifulSoup(requiredHtml, 'html5lib')
    result['ts_casino_name'] = soup.find('h2', {"class": "review-main-title-pros"}).get_text().replace(" Review", "")
    result['ts_software'] = []
    providersdef = soup.find("p", text='Software')
    if providersdef:
        providers = providersdef.findNext('div').findChildren("a" , recursive=False)
        for provider in providers:
            result['ts_software'].append({'name' : provider.get_text().strip()})
    result['ts_deposit_methods'] = []
    depmetsdef = soup.find("p", text='Deposit Methods')
    if depmetsdef:
        depmets = depmetsdef.findNext('div').findChildren("a" , recursive=False)
        for dep in depmets:
            result['ts_deposit_methods'].append({'name' : dep.get_text().strip(), 'is_supported' : True})
    result['ts_withdraw_methods'] = []
    witmetsdef = soup.find("p", text='Withdrawal Methods')
    if witmetsdef:
        witmets = witmetsdef.findNext('div').findChildren("a" , recursive=False)
        for wit in witmets:
            result['ts_withdraw_methods'].append({'name' : wit.get_text().strip(), 'is_supported' : True})
    wldef = soup.find("p", text='Withdrawal Limit')
    if wldef:
        result['ts_withdraw_limit'] = wldef.findNext('div').find("a").text.strip()
    else:
        result['ts_withdraw_limit'] = ''
    result['ts_restricted_countries'] = []
    resconsdef = soup.find("p", text='Restricted Countries')
    if resconsdef:
        resconslist = resconsdef.findNext('div').find('ul', {"class": "column-list"})
        if resconslist:
            rescons = resconslist.findChildren("li" , recursive=False)
            for resc in rescons:
                result['ts_restricted_countries'].append({'name' : resc.get_text().strip().split('\n', 1)[0]})
    result['ts_currencies'] = []
    currdef = soup.find("p", text='Currencies')
    if currdef:
        currencies = currdef.findNext('div').findChildren("a" , recursive=False)
        for currency in currencies:
            result['ts_currencies'].append({'name' : currency.get_text().strip()})
    result['ts_languages'] = []
    langsdef = soup.find("p", text='Languages')
    if langsdef:
        langs = langsdef.findNext('div').findChildren("a" , recursive=False)
        for lang in langs:
            result['ts_languages'].append({'name' : lang.get_text().strip()})
    licdef = soup.find("p", text='Licences')
    if licdef:
        result['ts_licences'] = licdef.findNext('div').find("a").get_text().strip()
    else:
        result['ts_licences'] = ''
    owndef = soup.find("p", text='Owner')
    if owndef:
        result['ts_owner'] = owndef.findNext('div').find("a").get_text().strip()
    else:
        result['ts_owner'] = ''
    estdef = soup.find("p", text='Established')
    if estdef:
        result['ts_estabilished'] = estdef.findNext('div').find("a").get_text().strip()
    else:
        result['ts_estabilished'] = ''
    livdef = soup.find("p", text='Live Chat')
    if livdef:
        result['ts_livechat'] = True if livdef.findNext('div').find("a").get_text().strip() == 'Yes' else False
    else:
        result['ts_livechat'] = False
    result['ts_link_out'] = '/play/' + result['ts_casino_name'].replace(" ", "-").lower()
    return result

test = ScrapeLinks(startUrl)
i = 1
total = len(resultLinks)
for oneLink in resultLinks:
    resultData.append(ScrapeCasino(oneLink))
    print('completed ' + str(i) + ' out of ' + str(total))
    i += 1

#json_str = json.dumps(resultData)
with open('data.txt', 'w') as outfile:
    json.dump(resultData, outfile)
#print(json_str)
