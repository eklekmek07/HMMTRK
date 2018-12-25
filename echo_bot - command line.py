from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, bus_calc

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Kilyos bota hoşgeldiniz..  Kullanılabilir komutlar:\n/rk  /hs  /mekikA  /mekikZ  /help')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Kullanılabilir komutlar:\n/rk  /hs  /mekikA  /mekikZ')

def rk(bot, update):
    update.message.reply_text(bus_calc.calc("rk"))
    print("rk")

def hs(bot, update):
    update.message.reply_text(bus_calc.calc("hs"))

def mekikA(bot, update):
    update.message.reply_text(bus_calc.calc("mekikA"))

def mekikZ(bot, update):
    update.message.reply_text(bus_calc.calc("mekikZ"))

def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def answer(bot, update):
    update.message.reply_text('Ve aleyküm esselam')

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("677471119:AAEM9cI6auBPyxgIclp8i4ywvKsJoJIXN9M")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("hs", hs))
    dp.add_handler(CommandHandler("rk", rk))
    dp.add_handler(CommandHandler("mekikA", mekikA))
    dp.add_handler(CommandHandler("mekikZ", mekikZ))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_handler(MessageHandler("selam", answer))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
