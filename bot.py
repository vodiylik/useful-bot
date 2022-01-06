import os
import telebot
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salom, sizni eshityapman?")


@bot.message_handler(content_types=['new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo'])
def handle_docs_audio(message):
    bot.delete_message(message.chat.id, message.message_id)


bot.infinity_polling()
