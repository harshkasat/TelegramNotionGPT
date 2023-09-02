import os
from dotenv import load_dotenv
import telebot
from chatbot import get_message
load_dotenv()
# Getting value form .env
BOT_TOKEN = os.getenv('BOT_TOKEN')


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def usermessages(message):
    message = get_message(message)
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['Notion'])
def notion(message):
    pass


bot.infinity_polling()
