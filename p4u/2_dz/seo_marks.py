from pprint import pprint
from requests_html import HTMLSession
from collections import Counter
import collections
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


#
# url = input("Enter url: ")
# keyword = input("Enter keyword: ")
def validate(url):
    govno = False
    while not govno:
        val = URLValidator()
        try:
            govno = val(url)
            return url
        except Exception as e:
            govno = False
            url = input("Re-Enter url: ")


url = validate(input("Enter url: "))
keyword = input("Enter keyword: ")

with HTMLSession() as session:
    resp = session.get(url)

title = resp.html.xpath('//title')[0].text
description = resp.html.xpath('//meta [@name="description"]/@content')
h1 = resp.html.xpath('//h1/text()')
h2 = resp.html.xpath('//h2/text()')

print('*' * 20, 'title', '*' * 20)
pprint(title)
print('*' * 20, 'description', '*' * 20)
pprint(description)
print('*' * 20, 'H1', '*' * 20)
pprint(h1)
print('*' * 50)

title_words = len(title.split())
title_symbols = len(title)

desc_list = ''.join(description)
desc_symbols = len(desc_list)

h1_number = len(h1)
h1_list = ''.join(h1)
h1_symbols = len(h1_list)

title_value = 60
title_mark = 30
key_title_mark = 5
title_grade = title_symbols * title_mark / title_value

if keyword in title:
    final_title_grade = key_title_mark + title_grade
    print("Title grade: " + str(round(final_title_grade)))
elif str(title_grade):
    print("Title grade: " + str(round(title_grade)))

desc_value = 160
desc_mark = 30
key_desc_mark = 5
desc_grade = desc_symbols * desc_mark / desc_value

if keyword in desc_list:
    final_desc_grade = key_desc_mark + desc_grade
    print("Description grade: " + str(round(final_desc_grade)))
elif str(desc_grade):
    print("Description grade: " + str(round(desc_grade)))

h1_value = 70
h1_mark = 30
key_h1_mark = 5
first_h1 = h1[0]
first_len_h1 = len(first_h1)
h1_grade = first_len_h1 * h1_mark / h1_value

for i in range(h1_number):
    if i == 0:
        print("Too much headlines. Printed the first one! Total count: " + str(h1_number))
for i in range(h1_number):
    if i > 0:
        first_h1 = h1[0]
        continue
    elif keyword in h1_list:
        final_h1_grade = key_h1_mark + h1_grade
        print("H1 grade: " + str(round(final_h1_grade)))
    elif str(h1_grade):
        print("H1 grade: " + str(round(h1_grade)))
