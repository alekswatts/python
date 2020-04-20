import random
import urllib.request
from bs4 import BeautifulSoup



# def download_image(url):
#     name = random.randrange(1, 100)
#     fullname = str(name) + ".jpg"
#     urllib.request.urlretrieve(url, fullname)
#
#
# download_image("https://img5.xuk.life/images/photos/00/05/13/94/51394/origin/fbe6b13767ef33c9fac405e0dbcbfa89.jpg")

page = 'https://xuk.life/'

html_page = urllib.request.urlopen(page)
soup = BeautifulSoup(html_page, "lxml")
print(soup)