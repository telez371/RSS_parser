import telebot
import time

from sending_messages.sticker_list import sticker_file_id
from random import choice


def send_telegram_message(telegram_settings, message):
    bot = telebot.TeleBot(telegram_settings.api_key)
    bot.send_message(telegram_settings.chat_id, message)
    bot.send_sticker(telegram_settings.chat_id, choice(sticker_file_id))
    time.sleep(1)
