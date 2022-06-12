import telebot
bot=telebot.TeleBot('2140618719:AAGiQdTeWpmKJMSb2J2hgy9CfqgklXOLlyE')
@bot.message_handler(commands=['start'])
def start(message):
 bot.reply_to(message,f'Welcom')
bot.polling()