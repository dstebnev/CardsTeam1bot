# _*_ coding: utf-8 _*_

import telebot
import time
import datetime
from multiprocessing import *
import schedule

API_TOKEN = 'hzhz'
bot = telebot.TeleBot(API_TOKEN)
 
 
def start_process():#Запуск Process
    p1 = Process(target=P_schedule.start_schedule, args=()).start()
 
    
class P_schedule(): # Class для работы с schedule
    def start_schedule(): #Запуск schedule
        ######Параметры для schedule######
        schedule.every().day.at("19:30").do(P_schedule.send_message1)
        schedule.every(1).minutes.do(P_schedule.send_message1)
        ##################################
        
        while True: #Запуск цикла
            schedule.run_pending()
            time.sleep(1)
 
    ####Функции для выполнения заданий по времени  
    def send_message1():
        chats = {}
        with open("chats.txt") as file_handler:
            for line in file_handler:
                chats[line] = line
            for chat in chats.keys():
                bot.send_message(chat, 'Ребята, заполните карточки, пожалуйста')
    ################
 
###Настройки команд telebot#########
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Оооокей, теперь буду напоминать про карточки')      
    with open("chats.txt", 'a') as file_handler:
        file_handler.write(str(message.chat.id)+"\n")
#####################
 
    
if __name__ == '__main__':
    start_process()
    try:
        bot.polling(none_stop=True)
    except:
        pass