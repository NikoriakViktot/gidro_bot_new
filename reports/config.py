import os
import telebot
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TELEGRAMKEY')

bot = telebot.TeleBot(token)


