import telebot
from telebot import types, util
import time
from datetime import datetime

API_TOKEN = '1039703621:AAGNQ-r3cQxd2hEdbj8KHnBgT-ruyUUhq84'

bot = telebot.TeleBot(API_TOKEN)
tb = telebot.AsyncTeleBot(API_TOKEN)
Alex = 301146859
chat_id = Alex


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
    bot.send_message(message.chat.id, f'Меня назначили твоим менеджером!\n'
                                      f'\nВсе просто – ты хочешь, что-то сделать.'
                                      f'\nПишешь мне об этом, и указываешь срок, когда я должен проконтролировать выполнение.'
                                      f'\nКак время придет – я с тебя все спрошу.'
                                      f'\nТолько без хитростей!')
    bot.send_message(message.chat.id, 'Здесь описаны наши с тобой правила: /help')
    bot.send_message(message.chat.id, 'Как ознакомишься, дай знать. И мы начнем делать дела!')

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name}, смотри.'
                                      f'\nЧтобы завести поручение используй: /set'
                                      f'\nЧтобы узнать, какие поручения на тебе: /list')

#Set a new Task
@bot.message_handler(commands=['set'])
def send_set(message):
    msg = bot.send_message(message.chat.id, 'Что ты хочешь сделать?')
    bot.register_next_step_handler(msg, put_task_on_schedule)


def put_task_on_schedule(message):
    try:
        chat_id = message.chat.id
        answer = message.text

        #TO-DO:
        #Message handler

    except Exception as e:
        bot.reply_to(message, 'Случилась какая-то ошибка >_<')


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


#Useful code
    #markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    #markup.add('Да', 'Нет', 'Через 10 минут)
    #msg = bot.send_message(message.chat.id, "Что ты хочешь сделать?", reply_markup=markup)