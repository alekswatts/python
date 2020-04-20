import requests
import time
import telebot
import random
import json


# def point(event, context):
#     print(event)
#
#
# def start_request():
#     url = 'https://api.telegram.org/bot{token}/{method}'.format(
#         token='934918878:AAHU1SyU4NGrmdlzRrZDrroO3ZzKOW9aSSM',
#         method='setWebhook'
#     )
#     data = dict(
#         url='https://evg4uh3fqd.execute-api.us-east-2.amazonaws.com/v0/934918878AAHz-cYQwbRHnCd4tW3Kh_8bm_od2mLBlfU')
#     r = requests.post(url, data=data)
#     print(r.json())
#
#
# if __name__ == '__main__':
#     start_request()

bot = telebot.TeleBot('934918878:AAE5nCE6U-rLTSJQ9_HOBFDWxv8mr_MU-vU')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Начнем', 'Бабу хочу', 'Я все')


@bot.message_handler(commands=['start'])
def start_message(message):

    bot.send_message(message.chat.id, 'Ну что, пришло время вздрочнуть?', reply_markup=keyboard1)


link = "https://scontent-waw1-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640" \
       "/41702064_269509570566616_6727338982570758741_n.jpg?_nc_ht=scontent-waw1-1.cdninstagram.com&_nc_cat=104" \
       "&_nc_ohc=8bG42sfmqPoAX_u63NW&oh=6bd6e8d37dbffaf5bb74f2d9767b751d&oe=5E9D7481 "


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Начнем':
        bot.send_message(message.chat.id, 'Чего желаешь?')

    elif message.text == 'test':
        with open("56.jpg", "rb") as file1:
            data = file1.read()
        bot.send_photo(message.from_user.id, photo=data)
    elif message.text == 'Бабу хочу':
        with open('results.json', 'r', encoding='utf-8') as file:
            filecont = json.load(file)
            nubies = random.choice(filecont)
            bot.send_photo(message.chat.id, "".join(nubies))

    elif message.text == 'Надю хочу':
        bot.send_message(message.chat.id, 'Щя, будет тебе Надя!')
        time.sleep(2)
        bot.send_photo(message.chat.id, link)

    elif message.text == 'Я все':
        bot.send_message(message.chat.id, 'Прощай, надеюсь тебе понравилось!')


print('Turned on')
with open('results.json', 'r', encoding='utf-8') as file:
    file = json.load(file)
    test = random.choice(file)


bot.polling()

import random
import urllib.request
from bs4 import BeautifulSoup



