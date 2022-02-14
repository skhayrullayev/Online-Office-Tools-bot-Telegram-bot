from transliterate import to_latin
from transliterate import to_cyrillic
import telebot

TOKEN = "5103265847:AAFEYRHQShWPaWeqhtVQydLrP_edZ_eBHzo"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Assalamu alaykum!\nMen ushbu chatdagi barcha siz yuborgan xabarlarni Lotindan Kirilga yoki Kirildan Lotinga o'gira olaman. " +
                                    "Men sizga kundalik vazifalarni bajarishda yordam beraman. Agar sizda xabar yoki takliflar bo'lsa @khayrus_dev ga murojat qiling" .format(message.from_user))


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        words = to_cyrillic(msg)
    else:
        words = to_latin(msg)
    bot.reply_to(message, words)


bot.polling()
