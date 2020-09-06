import telebot
from telebot import types
import time
from datetime import datetime

API_TOKEN = '1039703621:AAGNQ-r3cQxd2hEdbj8KHnBgT-ruyUUhq84'

bot = telebot.TeleBot(API_TOKEN)
tb = telebot.AsyncTeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, 'Я - будильник... А ты лох ))))))) ')
    bot.send_message(message.chat.id, 'Узнать правила: /help \nУстановить напоминание: /settime')

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, так и знал, что нажмешь ХЕЛП. \nПока нет ничё, бро')

# It is useless right now... But I will think it over and try to come up with something )))
@bot.message_handler(commands=['activate'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, "Nikita, have you washed your face?")
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('Yes', 'No', 'In 5 min')
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




@bot.message_handler(commands=['settime'])
def send_notification(message):
    msg = bot.send_message(message.chat.id, "What time would you prefer?")
    bot.register_next_step_handler(msg, process_time_step)


def process_time_step(message):
    try:
        chat_id = message.chat.id
        answer = message.text
        while 1:
            # bot.send_message(chat_id, str(datetime.now().strftime("%H:%M:%S")))
            time.sleep(5)
            if str(datetime.now().strftime("%H:%M")) == answer:
                bot.send_message(chat_id, "Notification!!!!!")
                break
    except Exception as e:
        bot.reply_to(message, 'oooops')



bot.polling()


