import telebot
from telebot import types, util
from fractions import Fraction
import time
from datetime import datetime

API_TOKEN = '1039703621:AAGNQ-r3cQxd2hEdbj8KHnBgT-ruyUUhq84'

bot = telebot.TeleBot(API_TOKEN)
tb = telebot.AsyncTeleBot(API_TOKEN)
# Viki = 1000947005
# Kate = 1090010019
Alex = 301146859
# Ekaterina = 800104629
# Konstantin = 126776816
chat_id = Alex

#bot.send_message(Alex, "Привет)))))))")
#bot.send_message(Ekaterina, "Теперь я могу тебе писать, Ekaterina!")


# bot.send_message(Konstantin, "Доброе утро, лох!")

# @bot.message_handler(content_types=['text'])
# def lalala(message):
    # bot.send_message(Alex, f"{message.text}\n\nFrom: {message.from_user.first_name} \nId: {message.from_user.id}")
    # bot.send_message(chat_id, 'Hi bro!')
    # bot.send_message(chat_id, time)
    # time.sleep(5)
    # bot.send_message(chat_id, 'Hi bro AGAIN')
    # bot.send_message(chat_id, datetime.now().strftime("%H:%M"))



@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Пока ты можешь только складывать простые дроби и находить проценты')
    bot.send_message(message.chat.id, 'Узнать правила: /help \nНачать пользоваться: /count')
    #bot.send_message(Alex, message.text)

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, так и знал, что нажмешь ХЕЛП.'
                                      f'\nКороче:'
                                      f'\nСначала ставим палочку: /'
                                      f'\nВыбираем /count и пишем по порядку по ОДНОМУ числу'
                                      f'\nДроби указываем в формате: 5/6'
                                      f'\nПроценты: сначала что, потом от чего!')

# Handle '/start' and '/help'
@bot.message_handler(commands=['activate'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Nikita, have you washed your face?")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'No', 'In 5 minutes')
    bot.register_next_step_handler(msg, process_sex_step)


def process_sex_step(message):
    try:
        chat_id = message.chat.id
        answer = message.text
        if (answer == u'Yes'):
            x = 'Very good!!!'
            bot.send_message(chat_id, x)
        elif (answer == u'No'):
            x = 'WHY ???'
            bot.send_message(chat_id, x)
        elif (answer == u'In 5 minutes'):
            x = 'Ok, I am waiting ...'
            bot.send_message(chat_id, x)
            time.sleep(3)
            bot.send_message(chat_id, 'What about now?')
            #Here we need next_step_handler to ask again (or loop)
        else:
            bot.send_message(chat_id, 'Are you durak?!')
    except Exception as e:
        bot.reply_to(message, 'oooops')


@util.async_dec()
def send_message(message):
    x = 10
    while x < 11:
        chat_id = message.chat.id
        tb.send_message(chat_id, 'Hey?')
        time.sleep(3)

# def process_life_step(message):
#     try:
#         chat_id = message.chat.id
#         time.sleep(3)
#         bot.send_message(chat_id, 'What about now?')
#     except Exception as e:
#         bot.reply_to(message, 'oooops')


bot.polling()


