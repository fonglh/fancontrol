#!/usr/bin/python3

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.ext import ContextTypes
import logging
import fancodes
from dotenv import dotenv_values

async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello {0}, your id is {1}'.format(update.message.from_user.first_name, update.message.from_user.id))

async def fan(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
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
    await context.bot.send_message(chat_id=update.effective_chat.id, text=fan + ' ' + command_word)

def main() -> None:
    env_values = dotenv_values()
    TELEGRAM_TOKEN = env_values['TELEGRAM_TOKEN']
    ALLOWED_USER_IDS = list(map(int, env_values['ALLOWED_USER_IDS'].split(",")))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler('getid', get_id))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND & filters.User(user_id=ALLOWED_USER_IDS), fan))

    application.run_polling()

if __name__ == '__main__':
    main()
