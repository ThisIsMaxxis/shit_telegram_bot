# -*- coding: utf8 -*-
from typing import Text
import telebot
import config
import random
import time
from telebot import types
from telebot.types import LabeledPrice, ShippingOption

prices2h_velnoel = [LabeledPrice(label='Велосипед', amount=43000)]
prices3h_velnoel = [LabeledPrice(label='Велосипед', amount=60000)]
pricesdh_velnoel = [LabeledPrice(label='Велосипед', amount=120000)]
prices10min_velel = [LabeledPrice(label='Велосипед Электрический', amount=10000)]
prices1h_velel = [LabeledPrice(label='Велосипед Электрический', amount=60000)]
prices10min_giro = [LabeledPrice(label='Гироскутер', amount=15000)]
prices20min_giro = [LabeledPrice(label='Гироскутер', amount=30000)]
prices30min_giro = [LabeledPrice(label='Гироскутер', amount=40000)]
prices1h_giro = [LabeledPrice(label='Гироскутер', amount=60000)]
prices10min_samokat = [LabeledPrice(label='Электросамокат', amount=20000)]
prices20min_samokat = [LabeledPrice(label='Электросамокат', amount=40000)]
prices30min_samokat = [LabeledPrice(label='Электросамокат', amount=60000)]
prices1h_samokat = [LabeledPrice(label='Электросамокат', amount=100000)]
prices30min_skate = [LabeledPrice(label='Скейтбоард', amount=10000)]
prices1h_skate = [LabeledPrice(label='Скейтбоард', amount=20000)]

bot = telebot.TeleBot('')
provider_token = ''

@bot.message_handler(commands=["start","help"])
def welcome(message):
    hello = bot.send_message(message.chat.id,"Приветствую вас меня зовут Бот!")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mrk = types.KeyboardButton("Да")
    mrk1 = types.KeyboardButton("Нет")
    markup.add(mrk,mrk1)
    bot.send_message(message.chat.id, "Хочешь взять что-то в прокат?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def start_decision(message):
    if message.text == "Да":
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar_dec = types.KeyboardButton("Велосипед(Не Электрический)")
        mar2_dec = types.KeyboardButton("Велосипед(Электрический)")
        mar3_dec = types.KeyboardButton("Гироскутер")
        mar4_dec = types.KeyboardButton("Электросамокат")
        mar5_dec = types.KeyboardButton("Детский Электромобиль")
        mar6_dec = types.KeyboardButton("Скейтбоард")
        markup1.add(mar_dec,mar2_dec,mar3_dec,mar4_dec,mar5_dec,mar6_dec)
        bot.send_message(message.chat.id,"Выбирай что себе возьмёшь",reply_markup=markup1)
    if message.text == "Велосипед(Не Электрический)":
        markup3_velnoel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_velnoel = types.KeyboardButton("2 часа велосипеда")
        mar2_velnoel = types.KeyboardButton("3 часа велосипеда")
        mar3_velnoel = types.KeyboardButton("Сутки на велике")
        mar4_velnoel = types.KeyboardButton("Назад в меню")
        markup3_velnoel.add(mar1_velnoel,mar2_velnoel,mar3_velnoel,mar4_velnoel)
        bot.send_message(message.chat.id,"Выбирай время", reply_markup=markup3_velnoel)
    if message.text == "Велосипед(Электрический)":
        markup4_velel = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_velel = types.KeyboardButton("10 минут эликтрического")
        mar2_velel = types.KeyboardButton("1 час эликтрического")
        mar3_velel = types.KeyboardButton("Назад в меню")
        markup4_velel.add(mar1_velel,mar2_velel,mar3_velel)
        bot.send_message(message.chat.id,"Выбирай время",reply_markup=markup4_velel)
    if message.text == "Гироскутер":
        markup5_giro = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_giro = types.KeyboardButton("10 минут на гироскутере")
        mar2_giro = types.KeyboardButton("20 минут на гироскутере")
        mar3_giro = types.KeyboardButton("30 минут на гироскутере")
        mar4_giro = types.KeyboardButton("1 час на гироскутере")
        mar5_giro = types.KeyboardButton("Назад в меню")
        markup5_giro.add(mar1_giro,mar2_giro,mar3_giro,mar4_giro,mar5_giro)
        bot.send_message(message.chat.id,"Выбирай время",reply_markup=markup5_giro)    
    if message.text == "Электросамокат":
        markup6_elsam = types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_elsam = types.KeyboardButton("10 минут на электросамокате")
        mar2_elsam = types.KeyboardButton("20 минут на электросамокате")
        mar3_elsam = types.KeyboardButton("30 минут на электросамокате")
        mar4_elsam = types.KeyboardButton("1 час на электросамокате")
        mar5_elsam = types.KeyboardButton("Назад в меню")
        markup6_elsam.add(mar1_elsam,mar2_elsam,mar3_elsam,mar4_elsam,mar5_elsam)
        bot.send_message(message.chat.id,"Выбирай время",reply_markup=markup6_elsam)  
    if message.text == "Детский Электромобиль":
        markup7_kidauto= types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_kidauto = types.KeyboardButton("10 минут дет.электромобиль")
        mar2_kidauto = types.KeyboardButton("20 минут дет.электромобиль")
        mar3_kidauto = types.KeyboardButton("30 минут дет.электромобиль")
        mar4_kidauto = types.KeyboardButton("1 час дет.электромобиль")
        mar5_kidauto = types.KeyboardButton("Назад в меню")
        markup7_kidauto.add(mar1_kidauto,mar2_kidauto,mar3_kidauto,mar4_kidauto,mar5_kidauto)
        bot.send_message(message.chat.id,"Выбирай время",reply_markup=markup7_kidauto) 
    if message.text == "Скейтбоард":
        markup8_skate= types.ReplyKeyboardMarkup(resize_keyboard=True)
        mar1_skate = types.KeyboardButton("30 минут скейтбоард")
        mar2_skate = types.KeyboardButton("1 час скейтбоард")
        mar3_skate = types.KeyboardButton("Назад в меню")
        markup8_skate.add(mar1_skate,mar2_skate,mar3_skate)
        bot.send_message(message.chat.id,"Выбирай время",reply_markup=markup8_skate)  
    if message.text == "2 часа велосипеда":
        bot.send_invoice(message.chat.id,
        title='Велосипед(Не Электрический)',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices2h_velnoel,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "3 часа велосипеда":
        bot.send_invoice(message.chat.id,
        title='Велосипед(Не Электрический)',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices3h_velnoel,
        start_parameter='3h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "Сутки на велике":
        bot.send_invoice(message.chat.id,
        title='Велосипед(Не Электрический)',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=pricesdh_velnoel,
        start_parameter='dh_velnoel',
        invoice_payload='удачного катания')
    if message.text == "10 минут электрического":
        bot.send_invoice(message.chat.id,
        title='Велосипед(Не Электрический)',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices10min_velel,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "1 час электрического":
        bot.send_invoice(message.chat.id,
        title='Велосипед(Не Электрический)',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices1h_velel,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "10 минут на гироскутере":
        bot.send_invoice(message.chat.id,
        title='Гироскутер 10 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices10min_giro,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "20 минут на гироскутере":
        bot.send_invoice(message.chat.id,
        title='Гироскутер 20 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices20min_giro,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "30 минут на гироскутере":
        bot.send_invoice(message.chat.id,
        title='Гироскутер 30 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices30min_giro,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "1 час на гироскутере":
        bot.send_invoice(message.chat.id,
        title='Гироскутер 1 час',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices1h_giro,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "10 минут на электросамокате":
        bot.send_invoice(message.chat.id,
        title='Электросамокат 10 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices10min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "20 минут на электросамокате":
        bot.send_invoice(message.chat.id,
        title='Электросамокат 20 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices20min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "30 минут на электросамокате":
        bot.send_invoice(message.chat.id,
        title='Электросамокат 30 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices30min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "1 час на электросамокате":
        bot.send_invoice(message.chat.id,
        title='Электросамокат 1 час',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices1h_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "10 минут дет.электромобиль":
        bot.send_invoice(message.chat.id,
        title='дет.электромобиль 10 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices10min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "20 минут дет.электромобиль":
        bot.send_invoice(message.chat.id,
        title='дет.электромобиль 20 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices20min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "30 минут дет.электромобиль":
        bot.send_invoice(message.chat.id,
        title='дет.электромобиль 30 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices30min_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "1 час дет.электромобиль":
        bot.send_invoice(message.chat.id,
        title='дет.электромобиль 1 час',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices1h_samokat,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "30 минут скейтбоард":
        bot.send_invoice(message.chat.id,
        title='Скейтбоард 30 минут',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices30min_skate,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "1 час скейтбоард":
        bot.send_invoice(message.chat.id,
        title='Скейтбоард 1 час',
        description="Отличный выбор",
        provider_token=provider_token,
        currency='rub',
        prices=prices1h_skate,
        start_parameter='2h_velnoel',
        invoice_payload='удачного катания')
    if message.text == "Назад в меню":
        welcome(message)        

@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True,
                                  error_message="Упс кажись платёж не прошёл((("
                                                "попробуйте ещё раз через несколько минут")     

@bot.message_handler(content_types=['successful_payment'])
def got_payment(message):
    bot.send_message(message.chat.id,
                     'Ура , платёж прошёл на сумму `{} {}` '
                     'Можете показать это сообщение человеку ответственному на аренде и кататься!'.format(
                         message.successful_payment.total_amount / 100, message.successful_payment.currency),
                     parse_mode='Markdown')  

bot.polling (none_stop=True , interval=0)