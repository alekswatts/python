import os

path = r'full path'

with open('results.csv', 'w', encoding='utf-8') as f:
    f.write(f'icon\n')

for i in os.listdir(path):
    sep = ' : '
    i = i + sep
    line = i.replace('.png : ', '')
    line = line.replace('-', ' ')
    line = line.replace('game icon ', '')
    result = f'{i + line.title()}\n'
    print(result)
    with open('results.csv', 'a', encoding='utf-8') as f:
        f.write(result)





