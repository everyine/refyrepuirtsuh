import requests
from telebot import TeleBot, types
import wikipedia
wikipedia.set_lang('ru')

TOKEN = "7529164218:AAGPAVebPgTfzQWS_NQ0A-BJlBjU7nOb1jU"
bot = TeleBot(TOKEN)

@bot.message_handler(commands=['wiki'])
def wiki(message):
    text = ' '.join(message.text.split(' ')[1:])
    results = wikipedia.search(text)
    markup = types.InlineKeyboardMarkup()
    for res in results:
        markup.add(types.InlineKeyboardButton(res, callback_data=res))
    bot.send_message(
        message.chat.id, text='Смотри что я нашёл!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data)
def answer(call):
    page = wikipedia.page(call.data)
    bot.send_message(call.message.id, text=page.title)
    bot.send_message(call.message.id, text=page.summary)
    bot.send_message(call.message.id, text=page.url)

def random_duck():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url'] 

@bot.message_handler(commands=['duck'])
def divide(message):
    url = random_duck()
    bot.send_message(message.chat.id, url)

def random_fox():
    url = 'https://randomfox.ca/floof'
    res = requests.get(url)
    data = res.json()
    return data['image'] 

@bot.message_handler(commands=['fox'])
def divide(message):
    url = random_fox()
    bot.send_message(message.chat.id, url)

bot.polling(none_stop=True)