import telebot

bot = telebot.TeleBot("924035289:AAEkYpPemBXmmzKf13JdbAKaDdLr7gjvM90")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	#bot.reply_to(message, message.text)
	bot.send_message(message.chat.id, message.text)
bot.polling(none_stop = True)