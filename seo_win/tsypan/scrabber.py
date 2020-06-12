import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep


class AskGamblers():
    def __init__(self):
        path = r'C:\Users\User\Google Диск\SEO Work\Repositories\python\seo_win\web_drivers\chromedriver.exe'
        self.driver = webdriver.Chrome(path)

    def data(self):
        self.driver.get('https://www.askgamblers.com/online-casinos/crazy-fox-casino-review/')

        casino_name = self.driver.find_element_by_xpath('//*[@id="casino-review__new"]/div[3]/div[2]/div[1]/div['
                                                        '1]/div/h1').text
        print(casino_name)

        software = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[1]/li[2]/div').text
        print(software)

        deposit_methods = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[1]/li[3]/div').text
        print(deposit_methods)

        withdrawal_methods = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[1]/li[4]/div').text
        print(withdrawal_methods)

        withdrawal_time = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[1]/li[5]/div').text
        print(withdrawal_time)

        withdrawal_limit = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[1]/li[6]/div').text
        print(withdrawal_limit)

        more_button = self.driver.find_element_by_xpath('//*[@id="casinoDetails"]/div/div[2]/span[2]')
        self.driver.execute_script("arguments[0].click();", more_button)

        rest_counties = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[1]/div').text
        print(rest_counties)

        currencies = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[5]/div').text
        print(currencies)

        languages = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[6]/div').text
        print(languages)

        licences = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[7]/div').text
        print(licences)

        owner = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[8]/div').text
        print(owner)

        established = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[9]/div').text
        print(established)

        live_chat = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[10]/div').text
        print(live_chat)

        contact = self.driver.find_element_by_xpath(
            '//*[@id="casinoDetails"]/ul[2]/li[11]/div').text
        print(contact)

        first_bonus = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[1]/div/div[1]/a/div[3]/h3').text
        first_bonus_type = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[1]/div/div[1]/a/div[3]/p').text
        print(first_bonus)
        print(first_bonus_type)

        second_bonus = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[2]/div/div[1]/a/div[3]/h3').text
        second_bonus_type = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[2]/div/div[1]/a/div[3]/p').text
        print(second_bonus)
        print(second_bonus_type)

        third_bonus = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[3]/div/div[1]/a/div[3]/h3').text
        third_bonus_type = self.driver.find_element_by_xpath(
            '//*[@id="casinoBonuses"]/ul/li[3]/div/div[1]/a/div[3]/p').text
        print(third_bonus)
        print(third_bonus_type)


launch = AskGamblers()
launch.data()
