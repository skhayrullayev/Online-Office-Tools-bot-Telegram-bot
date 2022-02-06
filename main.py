from transliterate import to_latin
from transliterate import to_cyrillic
from telebot import types
import telebot
from random import random


TOKEN = "5103265847:AAFEYRHQShWPaWeqhtVQydLrP_edZ_eBHzo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # item1 = types.KeyboardButton('Random')
    # item2 = types.KeyboardButton('Кирил-Latin')
    # item3 = types.KeyboardButton('Date and Time')

    # markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Assalamu alaykum!\n Men ushbu chatdagi barcha xabarlarni Lotindan Kirilga yoki Kirildan Lotinga o'gira olaman, ushbu botdan kundalik ishlaringizda foydalanishingiz mumkin. " +
                                     "Tez kunda mazkur botga yangi funksiyalar qo'shiladi. Umid qilamizki, " +
                                    "mazkur bot sizga kundalik vazifalarni bajarishda yordam beradi. Siz xabar yoki takliflar bo'lsa @skhayrullayev ga murojat qiling" .format(message.from_user))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        words = to_cyrillic(msg)
    else:
        words = to_latin(msg)
    bot.reply_to(message, words)


# @bot.message_handler(content_types=['text', 'location'])
# def bot_message(message):
#     if message.chat.type == 'private':
#
#         if message.text == 'Random':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             message = message
#             back = types.KeyboardButton('back')
#             markup.add(back)
#             bot.send_message(message.chat.id, 'the random number: ' + str(random.randint(0, message)))
#
#         elif message.text == 'Кирил-Latin-Кирил':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#
#             back = types.KeyboardButton('back')
#             markup.add(back)
#             bot.send_message(message.chat.id, 'Кирил-Latin', reply_markup=markup)
#
#         elif message.text == 'Date and Time':
#              markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#              item1 = types.KeyboardButton('Date')
#              item2 = types.KeyboardButton('Time')
#              item3 = types.KeyboardButton("Ramazon")
#              back = types.KeyboardButton('back')
#              markup.add(item1, item2, item3, back)
#              bot.send_message(message.chat.id, 'Date and Time', reply_markup=markup)
#
#         elif message.text == 'back':
#             markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#             item1 = types.KeyboardButton('Random')
#             item2 = types.KeyboardButton('Кирил-Latin')
#             item3 = types.KeyboardButton('Date and Time')
#
#             markup.add(item1, item2, item3)
#
#             bot.send_message(message.chat.id, 'main menu'.format(message.from_user), reply_markup=markup)
# #
# #         elif message.text == 'Date':
# #             tday = datetime.date.today()
# #             bot.send_message(message.chat.id, 'today is ' + str(tday))
# #
# #         elif message.text == 'Ramazon':
# #             tday = datetime.date.today()
# #             ramazon2022 = datetime.date(2022, 3, 4)
# #             till_ramazon2022 = ramazon2022-tday
# #             bot.send_message(message.chat.id, str(till_ramazon2022.days) + ' days left to Ramazon')\
# #
# #         elif message.text == 'location':
# #             bot.send_location(message.chat_id)
# # #            bot.send_chat_action(message.chat_id, action_string)


bot.polling()









