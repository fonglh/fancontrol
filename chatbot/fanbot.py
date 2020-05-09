#!/usr/bin/python3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import fancodes
from dotenv import dotenv_values

def get_id(update, context):
    update.message.reply_text('Hello {0}, your id is {1}'.format(update.message.from_user.first_name, update.message.from_user.id))

def fan(update, context):
    count = 1
    msg_text = update.message.text
    msg_text = msg_text.replace('fan', '')
    words = msg_text.split()
    command_word = words[-1].strip()
    if command_word.startswith('lx') and len(command_word) > 2:
        count = int(command_word[-1])
        command_word = command_word[:-1]
    fan = ''.join(words[:-1]).lower()
    if fan == 'all':
        fancodes.transmit_all(command_word)
    fancodes.transmit_command(fan, command_word, count)
    context.bot.send_message(chat_id=update.effective_chat.id, text=fan + ' ' + command_word)

env_values = dotenv_values()
TELEGRAM_TOKEN = env_values['TELEGRAM_TOKEN']
ALLOWED_USER_IDS = list(map(int, env_values['ALLOWED_USER_IDS'].split(",")))

updater = Updater(TELEGRAM_TOKEN, use_context=True)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

updater.dispatcher.add_handler(CommandHandler('getid', get_id))
updater.dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command) & Filters.user(ALLOWED_USER_IDS), fan))

updater.start_polling()
updater.idle()
