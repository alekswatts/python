import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

username = 'seoteamlime@gmail.com'
password = 'DDamntasty3337777'


class OutReachEmail():
    def __init__(self):
        path = r'C:\Users\User\Google Диск\SEO Work\Repositories\python\seo_win\web_drivers\chromedriver.exe'
        self.driver = webdriver.Chrome(path)

    def login(self):
        self.driver.get('https://ninjaoutreach.com')

        button = self.driver.find_element_by_xpath('//*[@id="primary_manu_influencers"]/div/div/div[3]/a[2]')
        button.click()

        email_in = self.driver.find_element_by_xpath('//*[@id="Email"]')
        email_in.send_keys(username)

        pw_in = self.driver.find_element_by_xpath('//*[@id="Password"]')
        pw_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="loginButton"]')
        login_btn.click()

        self.driver.get('https://app.ninjaoutreach.com/YourProspecting')

        my_list = self.driver.find_element_by_xpath('//*[@id="dropdownMenu1"]')
        my_list.click()

        sleep(1)

        final_page = self.driver.find_element_by_xpath('//*[@id="njo-body"]/div[2]/div[1]/div[1]/div[1]/ul/li[2]/a/span')
        final_page.click()

        self.driver.implicitly_wait(10)

        doc = self.driver.page_source
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

        for email in emails:
            print(email)


launch = OutReachEmail()
launch.login()