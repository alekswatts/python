from pprint import pprint
import collections

url = "https://www.netflix.com/"
title = "Netflix Ukraine - Watch TV Shows Online, Watch Movies Online"
description = "Watch Netflix movies & TV shows online or stream right to" \
              " your smart TV, game console, PC, Mac, mobile, tablet and more."
h1 = "All of Netflix"
keyword = "Netflix"


title_percentage = title.count(keyword) / len(title.split()) * 100
description_percentage = description.count(keyword) / len(description.split()) * 100
h1_percentage = h1.count(keyword) / len(h1.split()) * 100

url_result = {"URL": url}

title_result = {"Words": len(title.split()),
                "Symbols": len(title),
                "Keywords": title.count((keyword)),
                "Percentage": int(title_percentage)}

description_result = {"Words": len(description.split()),
                      "Symbols": len(description),
                      "Keywords": description.count((keyword)),
                      "Percentage": int(description_percentage)}

h1_result = {"Words": len(h1.split()),
             "Symbols": len(h1),
             "Keywords": h1.count((keyword)),
             "Percentage": int(h1_percentage)}


d = {"URL": url,
     "Tittle": [title, title_result],
     "Description": [description, description_result],
     "H1": [h1, h1_result]}

sorted_dic = collections.OrderedDict(d)

pprint(sorted_dic)


