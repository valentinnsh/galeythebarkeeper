#
# Copyright (c)
# 2018 V.Shishkin
#

# -*- coding: utf-8 -*-

#import config
import telebot
import subprocess
import time

token =  '771932376:AAFavfwj6C-ldY0CUHihyTkJT5zchTktyUQ'
bot = telebot.TeleBot(config.token)

helping_msg = "Добрый невечер. Я Галея, управляющий, бармен и вообще душа этого места."
#------Command list --------
@bot.message_handler(commands=['help'])
def send_help_msg(message):
    bot.send_message(message.chat.id, helping_msg)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)
