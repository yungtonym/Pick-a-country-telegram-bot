import telebot

bot = telebot.TeleBot('6292095375:AAGQ9S9FtYEomvSbX6XNjgjuakBY9XM9j_s')


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Hello!')


bot.polling(none_stop=True)
