import os
import telebot

bot = telebot.TeleBot('1053298773:AAH-hnRFYsE4NNzQ0LUGkiu3V6IRXKismlk')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Начнем', 'Я все')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Ну что, пришло время вздрочнуть?', reply_markup=keyboard1)


link = 'https://image.winudf.com/v2/image/Y29tLmludGVuc2UucHViMS5ob3Rhc2dfc2NyZWVuXzFfaHZjaGlud3M/screen-1.jpg?fakeurl=1&type=.jpg'


@bot.message_handler(content_types=['text'])
def send_text(message, *args):
    if message.text == 'Начнем':
        bot.send_message(message.chat.id, 'Чего желаешь?')
    elif message.text == 'Надю хочу':
        bot.send_message(message.chat.id, 'Щя, будет тебе Надя!')
        bot.send_photo(message.chat.id, link)
    elif message.text == 'Я все':
        bot.send_message(message.chat.id, 'Прощай, надеюсь тебе понравилось!')

print('Turned on')
bot.polling()
