#
# Copyright (c)
# 2018 V.Shishkin
#

# -*- coding: utf-8 -*-

#import config
import telebot
import time
import random
import json

token =  '771932376:AAFavfwj6C-ldY0CUHihyTkJT5zchTktyUQ'
bot = telebot.TeleBot(token)

helping_msg = ''
starting_msg = "Добрый невечер. Я Галея, управляющий, бармен и вообще душа этого места. Вы нашли путь в мое заведение, так что не забудьте расписаться в гостевой книге."
chat_already_msg = "Вы уже открыли дверь однажды"
alredy_msg = "Ты уже в моем журнале, дорогуша"
you_are_in_the_book_msg = "Добро пожаловать, теперь ты в книге важных гостей, "
whait_some_time_msg = "Я уже выбирала сегодня, не спеши. У нас впереди может быть еще вечность..."
#---------------------------
#------Command list --------

#--------------Starting--------------------------
#@bot.message_handler(commands=['start'])
def start_bot_in_chat(message):
    with open('stat.json') as json_file:
        start_dat = json.load(json_file)
        if message.chat.id in start_dat['chat']:
            bot.send_message(message.chat.id, chat_already_msg)
        else:
            bot.send_message(message.chat.id, starting_msg)
            start_dat['chat'].append(message.chat.id)
            json_file.close()
    with open('stat.json','w') as outfile:
        json.dump(start_dat,outfile)

@bot.message_handler(commands=['help'])
def send_help_msg(message):
    bot.send_message(message.chat.id, helping_msg)

#-------------------Registration------------------
@bot.message_handler(commands=['reg'])
def register_newcomer(message):
    with open('stat.json') as json_file:
        start_dat = json.load(json_file)
        if message.chat.id not in start_dat['chat']:
            start_bot_in_chat(message)

    json_file.close()
    with open('data' + str(message.chat.id) + '.json') as json_file:
        data = json.load(json_file)
        newcomer = {
            "user" : message.from_user.username,
            "stats" : [0,0,0,0,0]
        }

        reg_status=0
        for pos in range(0,len(data['people'])):
            if message.from_user.username in data['people'][pos]['user']:
                bot.send_message(message.chat.id, alredy_msg)
                reg_status = 1
        if(reg_status == 0):
            bot.send_message(message.chat.id, you_are_in_the_book_msg + str(message.from_user.first_name))
            data['people'].append(newcomer)
            json_file.close()
    with open('data' + str(message.chat.id) + '.json', 'w') as outfile:
        json.dump(data, outfile)

#---------------------User of the day------------------------
break_time = 0
@bot.message_handler(commands=['run'])
def user_of_the_day(message):
    global break_time
    if(time.time()-break_time > 30): #57700
        chat_id = message.chat.id
        with open('data' + str(chat_id) + '.json') as json_file:
            data = json.load(json_file)
            winner = random.choice(data['people'])
            bot.send_message(message.chat.id, 'Наш победитель сегодня это.... '+'@'+ winner['user']+'!')

        break_time = time.time()
        for pos in range(0,len(data['people'])):
                if  (winner ==  data['people'][pos]):
                    data['people'][pos]['stats'][0] += 1

        break_time = time.time()
        json_file.close()
        with open('data' + str(message.chat.id) + '.json', 'w') as outfile:
            json.dump(data, outfile)
    else:
        bot.send_message(message.chat.id, whait_some_time_msg)

#---------------------Pidor of the day------------------------
p_break_time = 0
@bot.message_handler(commands=['pidor'])
def user_of_the_day(message):
    global p_break_time
    if(time.time()-p_break_time > 30): #57700
        chat_id = message.chat.id
        with open('data' + str(chat_id) + '.json') as json_file:
            data = json.load(json_file)
            winner = random.choice(data['people'])
            bot.send_message(message.chat.id, 'Пип,пип,пип... Пидор найден! '+'@'+winner['user']+'!')
            for pos in range(0,len(data['people'])):
                if  (winner ==  data['people'][pos]):
                    print("OK!")
                    data['people'][pos]['stats'][1] += 1

        p_break_time = time.time()
        json_file.close()
        with open('data' + str(message.chat.id) + '.json', 'w') as outfile:
            json.dump(data, outfile)

    else:
        bot.send_message(message.chat.id, whait_some_time_msg)

if __name__ == '__main__':
    bot.polling(none_stop=True)
