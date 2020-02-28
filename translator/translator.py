from google.cloud import translate

filename = input('Enter filename: ')

with open('filename.doc', 'w', encoding='utf-8') as f:
    with open('filename.csv', 'w', encoding='utf-8') as f2: