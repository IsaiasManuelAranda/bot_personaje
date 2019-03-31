#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals  # Te perimte usar caracteres
from builtins import (ascii, bytes, chr, dict, filter, hex, input,
                      int, map, next, oct, open, pow, range, round,
                      str, super, zip)

from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler,
                          Filters, RegexHandler, ConversationHandler)
import logging
import web
import random

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'bot_shrek',
    user = 'chay',
    pw = 'chay',
    port = 3306
)

#Samm17_bot 
token = '767578580:AAEDkHYl1c2j_ewMdsRqDs3gOo6lSzXM0M8'

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    username = update.message.from_user.username
    update.message.reply_text(
        'Hola {} usa estos comandos:\n/info llave #busca_informacion\n/personaje nombre_personaje\nConsulta al personaje de la pelicula de shrek\n  \
        '.format(username))

def help(bot, update):
    username = update.message.from_user.username
    update.message.reply_text('Hola {} Usa estos comandos:\n/info '.format(username))

def search(bot, update):
    text = update.message.text.split()
    username = update.message.from_user.username
    try:
        nombre_personaje = text[1] # cast para convertir str a int
        print "Send info to {}".format(username)
        print "Key search {}".format(nombre_personaje)
        result = db.select('personaje', where='nombre_personaje=$nombre_personaje', vars=locals())[0]

        nombre_personaje = result.nombre_personaje
        descripcion_personaje = result.descripcion

        nombre = nombre_personaje.encode("utf-8")
        descripcion = descripcion_personaje.encode("utf-8")
        respuesta =  "Personaje: " + nombre + "\n" + \
                    "                           Descripcion\n" + descripcion
        #response = "Sending Info " + str(result[0]) + ", " + str(result[1]) + ", " + str(result[2])
        #print response
        update.message.reply_text('Hola {}\nEsta es el personaje que buscas:\n{}'.format(username, respuesta))


    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('La llave {} es incorreta'.format(nombre_personaje))

def personaje(bot, update):
    search(bot, update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'Personaje init token'
        
        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'Shrek Bot'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))
        dp.add_handler(CommandHandler("personaje", personaje))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors
        dp.add_error_handler(error)

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'Personaje ready'
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
