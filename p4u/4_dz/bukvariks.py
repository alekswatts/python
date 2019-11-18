from time import time

keys = input('Enter keyword or comma separated keywords: ')
t1 = time()
count = 0
# з залальної бази букварікса викачав слова "keywords" - скоріше обробляє
with open('keyword.txt', 'r', encoding='utf-8') as f:
    with open('results.csv', 'w', encoding='utf-8') as f2:

        f2.write(f'Keyword\tWords Count\tSymbols\n')
        for line in f:
            line = line.strip()
            temp_list = line.split()

            flags = list()
            for kw in keys.split(', '):
                if kw in temp_list:
                    flags.append(True)
                else:
                    flags.append(False)

            if any(flags):

                words_count = len(line.split())
                symbols_count = len(line)
                raw = f'{line}\t{words_count}\t{symbols_count}\n'
                count +=1
                f2.write(raw)

                del words_count, symbols_count, raw

                del temp_list
t2 = time()

print(f'All done! Found {count} keywords')
print('Working time is: ', round(t2-t1, 4), ' seconds')

