import telebot
from telebot import types

API_TOKEN = "7088511350:AAGcgLZiM3hotp3iluqYVAQlA4KNoZqilME"  # O'zingizning bot tokeningizni shu yerga yozing

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Inline keyboard tugmasini yaratamiz
    inline_kb = types.InlineKeyboardMarkup()
    web_app_button = types.InlineKeyboardButton(
        text="🛒Интернет-магазин",
        web_app=types.WebAppInfo(url="https://Streetstyle5.com")  # O'z web interfeys URLingizni yozing
    )
    inline_kb.add(web_app_button)

    bot.send_message(message.chat.id, "🛍 Добро пожаловать в наш онлайн-магазин! 🛍 \n 🛒 Для покупок нажмите на кнопку ниже! ⬇️:", reply_markup=inline_kb)


bot.polling()
