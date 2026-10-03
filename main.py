import os
import logging
import telebot
from telebot import types

# Loglarni sozlash (Xatoliklarni ko'rib turish uchun)
logging.basicConfig(level=logging.INFO)

# Telegram Bot Tokeningizni shu yerga yozing
BOT_TOKEN = "BOT_TOKENINGIZNI_SHU_YERGA_YOZING"

bot = telebot.TeleBot(BOT_TOKEN)

# /start buyrug'i uchun buyruq
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    user_name = message.from_user.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💐 Gullar katalogi")
    item2 = types.KeyboardButton("📞 Biz bilan bog'lanish")
    markup.add(item1, item2)
    
    bot.reply_to(
        message, 
        f"Assalomu alaykum, {user_name}! 🌸\nFlowerbot xizmatiga xush kelibsiz!", 
        reply_markup=markup
    )

# Tugmalar yoki matnli xabarlar uchun ishlov beruvchi
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "💐 Gullar katalogi":
        bot.send_message(message.chat.id, "Bizdagi mavjud gullar ro'yxati tez orada yuklanadi...")
    elif message.text == "📞 Biz bilan bog'lanish":
        bot.send_message(message.chat.id, "Adminga murojaat: @admin_username")
    else:
        bot.reply_to(message, f"Siz yubordingiz: {message.text}")

# Serverda 24/7 uzluksiz va xatosiz ishlashi uchun qayta ulanish kodi
if __name__ == "__main__":
    print("Bot muvaffaqiyatli ishga tushdi va ishlamoqda...")
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

