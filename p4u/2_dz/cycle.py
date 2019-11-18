keywords ="""
netflix ukraine
netflix сериалы
netflix українською
netflix это
netflix фильмы
netflix ru
netflix на русском
netflix movies
""".strip().split("\n")

print(keywords)

word = "netflix"


for keyword in enumerate(keywords):
    print("Word: ", keyword, i)
    if word in keyword:
        print("Word in: ", keyword)

print("All done")