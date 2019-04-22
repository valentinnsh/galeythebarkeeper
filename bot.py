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

token =  ''
bot = telebot.TeleBot(token)

helping_msg = ''
starting_msg = "Добрый невечер. Я Галея, управляющий, бармен и вообще душа этого места. Вы нашли путь в мое заведение, так что не забудьте расписаться в гостевой книге."
chat_already_msg = "Вы уже открыли дверь однажды"
alredy_msg = "Ты уже в моем журнале, дорогуша"
you_are_in_the_book_msg = "Добро пожаловать, теперь ты в книге важных гостей, "
#---------------------------
#------Command list --------
@bot.message_handler(commands=['start'])
def start_bot_in_chat(message):
    with open('stat.json') as json_file:
        start_dat = json.load(json_file)
        if int(message.chat.id) in start_dat['chat']:
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

@bot.message_handler(commands=['reg'])
def register_newcomer(message):
    with open('data' + str(message.chat.id) + '.json') as json_file:
        data = json.load(json_file)
        newcomer = {
            "user" : message.from_user.username,
            "stats" : [0,0,0,0,0]
        }

        if message.from_user.username in data['people']:
            bot.send_message(message.chat.id, alredy_msg)
        else:
            data['people'].append(newcomer)
            with open('data' + str(message.chat.id) + '.json', 'w') as outfile:
                json.dump(data, outfile)
                bot.send_message(message.chat.id, you_are_in_the_book_msg + str(message.from_user.first_name))

if __name__ == '__main__':
    bot.polling(none_stop=True)
