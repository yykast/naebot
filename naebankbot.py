import telebot

bot = telebot.TeleBot("892728913:AAFOXOVtN5OQ6mi9CiCV1faxZy-HBTgDuew")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling( none_stop = True )
