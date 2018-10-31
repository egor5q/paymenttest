# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
import info
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
from emoji import emojize
import requests
import json
from SimpleQIWI import *

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
bearer=os.environ['bearer']
mylogin=79268508530


s=requests.Session()
s.headers['authorization']='Bearer '+bearer
parameters={'rows':'10'}
h=s.get('https://edge.qiwi.com/payment-history/v1/persons/'+str(mylogin)+'/payments', params = parameters) 
print(json.loads(h.text))

#hook=s.put("https://edge.qiwi.com/payment-notifier/v1/hooks?hookType=1&param=http%3A%2F%2Fecho.fjfalcon.ru%2F&txnType=2")
info=s.get("https://edge.qiwi.com/payment-notifier/v1/hooks/active")
print(json.loads(info.text))
tst=s.get('https://edge.qiwi.com/payment-notifier/v1/hooks/15c545e6-9547-4192-a2dc-ad2ee77f53ee')
print(json.loads(tst.text))
#s.delete('https://edge.qiwi.com/payment-notifier/v1/hooks/fa6d8174-b2fe-425f-b52d-16d035b1e4c0')

api=QApi(token=bearer,phone=mylogin)
price=1
comment='testcomment'#api.bill(price)
print(comment)
print('Переведите '+str(price)+' рублей на счёт '+str(mylogin)+' с комментарием '+comment)

@api.bind_echo()
def foo(bar):
    bot.send_message(441399484,'New payment!')
    print(bar)
    


#while True:
#      if api.check(comment):
#            print('Платеж получен!')
#            bot.send_message(441399484,'Платеж получен! Сумма: '+str(price)+' рублей.')
#            break        
#      time.sleep(1)
      
#api.stop()



#def posts():
#      getkey=s.post('')
#      print(json.loads(getkey.text))
#      t=threading.Timer(10,posts)
#      t.start()

if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

