import telebot
import webbrowser

bot = telebot.TeleBot('8348034578:AAHA_pOxQHtfDV5ozoQV7XOzTki9akjdHEI')

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://www.twitch.tv')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>info</u></em>', parse_mode='html')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.infinity_polling()