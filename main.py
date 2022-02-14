from transliterate import to_latin
from transliterate import to_cyrillic
from telebot import types
import telebot



TOKEN = "5103265847:AAFEYRHQShWPaWeqhtVQydLrP_edZ_eBHzo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
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


bot.polling()









