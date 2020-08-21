import config
import telebot


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "hi" 
    + message.from_user.first_name + ' ' +message.from_user.last_name
    + "lol")

if __name__ == '__main__':
    bot.polling(none_stop=True)
