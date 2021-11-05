from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(context: CallbackContext, update : Update):
    greetin_text = 'Вызван /start'
    logging.info(greetin_text)
    context.message.reply_text(greetin_text)


def talk_to_me(context: CallbackContext, update : Update):
    user_text = "Привет {}! Ты написал: {}".format(context.message.chat.first_name, context.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", context.message.chat.username, context.message.chat.id, context.message.text )
    context.message.reply_text(user_text)


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user ))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me ))

    mybot.start_polling()
    mybot.idle()


main()
