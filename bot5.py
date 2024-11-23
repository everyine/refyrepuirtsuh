from telebot import TeleBot, type
from random import randint
import json
import os

TOKEN = "7529164218:AAGPAVebPgTfzQWS_NQ0A-BJlBjU7nOb1jU"
bot = TeleBot(TOKEN)

game = False
used_cities = []
letter = ''
points = 0
leaderboard = {}


with open('cities.txt', 'r', encoding='utf-8') as f:
    cities = []
    for line in f.readlines():
        cities.append(line.strip().lower())

def select_letter(text):
    i = 1
    while text[-1*i] in ('ъ', 'ы', 'й'):
        i += 1
    return text[-1*i]

@bot.message_handler(commands=['leaderboard'])
def leader(message):
    with open('score.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    leaders = ''
    for name, user_points in_data.items():
        leaders += name + ' ' + str(user_points) + '\n'
    @bot.send_message(message.chat.id, text = leaders ) 
    



@bot.message_handler(commands=['goroda'])
def start_game(message):
    global game
    global letter
    game = True
    city = choice(cities)
    letter = select_letter(city)
    bot.send_message(message.chat.id, text=city)


@bot.message_handler()
def game(message):
    if game:
        if message.text.lower() in used_words:
            print(letter)
            bot.send_message(message.chat.id, 'Город назывался!')
            return
        if message.text.lower()[0] != letter:
            bot.send_message(message.chat.id, 'Не та буква')
            return
        if message.text.lower() in data:
            if message.from_user.first_name in leaderboard:
                leaderboard[message.from_user.first_name] += 1
            else:
                leaderboard[message.from_user.first_name] = 1

@bot.message_handler(commands=['save'])
def save(message):   
    if os.path.exists('score.json'):
        with open('score.json', 'w', encoding='utf-8') as f:
            data = json.load(f)
        bot.send_message(message.chat.id, 'Прогресс сохранён')






bot.polling(none_stop=True)