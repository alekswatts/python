import requests,time
from bs4 import BeautifulSoup

url = "URL_HERE"
r = requests.get(url)

listy = []
main_url = "https://www.expireddomains.net"
while True:
    try:
        r = requests.get(url)
        html = BeautifulSoup(r.text,"lxml")
        url = main_url + html.find("div",class_="right").find("a")["href"]

        print(url)
        links = html.find_all(class_="field_domain")

        for x in links:
            listy.append(x.find("a")["title"])
            print(x.find("a")["title"])

        r = requests.get(url)
        print("Total Urls Found "), len(listy)
    except:
        print(html)
        if html.text.__contains__("You hit the rate limiter. Slow down!"):
            File = open("sites.txt", "w")
            for x in listy:
                File.write(x + "\n")
            File.flush()
            print("Total Urls Found "), len(listy)
            print("Sleeping...")
            time.sleep(5)


        else:
            print("Breaking")
            break

File = open("sites.txt","w")
for x in listy:
    File.write(x + "\n")
File.close()