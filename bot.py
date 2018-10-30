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


token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)
bearer=os.environ['bearer']
mylogin=79268508530


s=request.Session()
s.headers['authorization']='Bearer '+bearer
parameters={'rows':'10'}
h=s.get('https://edge.qiwi.com/payment-history/v1/persons/'+mylogin+'/payments', params = parameters) 
print(json.loads(h.text))



if True:
   print('7777')
   bot.polling(none_stop=True,timeout=600)

