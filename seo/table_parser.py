import urllib.request
from bs4 import BeautifulSoup


page = 'https://kasynohex.com/kasyna-online/'


def casino_names(page):
    html_page = urllib.request.urlopen(page)
    soup = BeautifulSoup(html_page, "lxml")
    table = soup.find_all('td', {'class' : 'col col-4'})
    for casino in table:
        print(casino.text)


casino_names(page)