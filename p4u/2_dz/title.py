from pprint import pprint
from requests_html import HTMLSession
from collections import Counter
import collections

# не зрозумів логіки як визначити заспамленість та щільність тексту


url = input("Enter url: ")

with HTMLSession() as session:
    resp = session.get(url)

title = resp.html.xpath('//title')[0].text
description = resp.html.xpath('//meta[@name="description"]/@content')
keyword = "Netflix"


print('*'*20, 'title', '*'*20)
pprint(title)
print('*'*20, 'description', '*'*20)
pprint(description)
print('*'*50)

title_words = len(title.split())
title_symbols = len(title)

title_unique = title.replace("-", " ")\
    .replace("?", " ")\
    .replace("!", " ")\
    .replace(",", " ")\
    .replace(".", " ")\
    .replace(".", " ")

unique = set(title_unique.split())
uniqueWordCount = len(unique)
spam = Counter(title_unique.split())



dictionary = {"Words": title_words,
              "Symbols": title_symbols,
              "Unique Words": uniqueWordCount,
              "Spam Words": spam}

result = collections.OrderedDict(dictionary)

pprint(result)


