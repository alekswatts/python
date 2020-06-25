from selenium import webdriver
from time import sleep

path = r'C:\Users\User\Google Диск\SEO Work\Repositories\python\seo_win\web_drivers\chromedriver.exe'


class ThematicCheck():
    def __init__(self):
        self.driver = webdriver.Chrome(path)

    def google(self):
        with open('links.csv', 'r', encoding='utf-8') as f:
            with open('result.csv', 'w', encoding='utf-8') as f2:
                f2.write(f'Domain\tThematic\n')

                for link in f:
                    link = link.strip()
                    key = 'site: ' + link + ' ' + 'casino'

                    print(f'Send request for key: [{key}]')

                    sleep(5)

        self.driver.get(f'https://www.google.com/search?q={key}&num=100&hl=en')


start = ThematicCheck()
start.google()
