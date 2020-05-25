import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


class ImageParser():
    def __init__(self):
        path = r'C:\Users\User\Google Диск\SEO Work\Repositories\python\seo_win\web_drivers\chromedriver.exe'
        self.driver = webdriver.Chrome(path)

    def google(self):
        self.driver.get('https://www.google.com/')

        keyword = 'Poland'
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.send_keys(keyword)

        sleep(1)

        search_btn = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
        search_btn.send_keys(u'\ue007')

        images_mark = self.driver.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[2]/a')
        images_mark.click()

        first_image = self.driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]')
        first_image.click()

        sleep(2)

    def next_picture(self):
        next_btn = self.driver.find_element_by_xpath(
            '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div[1]/div[1]/div/div[1]/a[2]/div')
        next_btn.click()

    def img_link(self):
        print(self.driver.current_url)
        page = self.driver.current_url
        html_page = urllib.request.urlopen(page)
        soup = BeautifulSoup(html_page, features='html.parser')
        image = soup.find('img', {'class': 'n3VNCb'})
        for link in image.find('src'):
            src = link.get('href')
            print(src)


launch = ImageParser()
launch.google()