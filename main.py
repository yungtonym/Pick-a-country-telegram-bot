import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6292095375:AAGQ9S9FtYEomvSbX6XNjgjuakBY9XM9j_s')


@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    search_button = types.KeyboardButton('Search')
    flag_info_button = types.KeyboardButton('What\'s that flag on bot\'s avatar?')
    help_button = types.KeyboardButton('Help')
    random_country_button = types.KeyboardButton('Random country')
    markup.row(search_button)
    markup.row(help_button, flag_info_button, random_country_button)
    bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}!', reply_markup=markup)
    # bot.register_next_step_handler(message, on_click)


@bot.message_handler(content_types=['text'])
def on_click(message):
    if message.text == 'What\'s that flag on bot\'s avatar?':
        webbrowser.open('https://www.flagofplanetearth.com/')
    elif message.text == 'Help':
        bot.send_message(message.chat.id, '<b>Help information</b>', parse_mode='html')
    elif message.text == 'Search':
        bot.send_message(message.chat.id, '<b>Enter the name of a country</b>', parse_mode='html')
        look_for_country(message)
    elif message.text == 'Random country':
        bot.send_message(message.chat.id, '<b>Random country</b>', parse_mode='html')


def look_for_country(message):
    name = message.text.strip().lower()


@bot.message_handler(commands=['your_flag'])
def flag_info(message):
    webbrowser.open('https://www.flagofplanetearth.com/')


@bot.message_handler(commands=['help'])
def help_command(message):
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
