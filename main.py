import telebot
import webbrowser

bot = telebot.TeleBot('6292095375:AAGQ9S9FtYEomvSbX6XNjgjuakBY9XM9j_s')


@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')


@bot.message_handler(commands=['your-flag'])
def flag_info(message):
    webbrowser.open('https://www.flagofplanetearth.com/')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help information</b>', parse_mode='html')


@bot.message_handler(commands=['dev'])
def dev(message):
    bot.send_message(message.chat.id, message)


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
    elif message.text.lower() == 'hello':
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!')
    elif message.text.lower() == 'where am i':
        bot.reply_to(message, f'I don\'t know :)')


bot.polling(none_stop=True)
