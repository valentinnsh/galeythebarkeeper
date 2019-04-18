#!/usr/bin/python3
#
# Copyright (c)
# 2018 V.Shishkin
#

# -*- coding: utf-8 -*-

#import config
import telebot
import sys
import subprocess
import time

token =  '771932376:AAFavfwj6C-ldY0CUHihyTkJT5zchTktyUQ'
bot = telebot.TeleBot(config.token)

helping_msg = "Добрый невечер. Я Галея, управляющий, бармен и вообще душа этого места."
#------Command list --------
@bot.message_handler(commands=['help'])
def send_help_msg(message):
    bot.send_message(message.chat.id, helping_msg)

if __name__ == '__main__':
    bot.polling(none_stop=True)
