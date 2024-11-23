from telebot import TeleBot
from random import randint, choice
game_choice = ["камень","ножницы", "бумага"]
user_points = 0
comp_points = 0

TOKEN = "7529164218:AAGPAVebPgTfzQWS_NQ0A-BJlBjU7nOb1jU"
bot = TeleBot(TOKEN)


# @bot.message_handler(func=lambda x: x.text.lower() in game_choice)
# def start(message):
#     user_choice = message.text.lower()
#     bot_choice = choice(game_choice)
#     bot.send_message(message.chat.id, bot_choice)

@bot.message_handler(func=lambda x: x.text.lower() in game_choice)
def game(message):
    global user_points
    global comp_points
    user_choice = message.text.lower()
    bot_choice = choice(game_choice)
    bot.send_message(message.chat.id, bot_choice) 
    if user_choice == "камень" and bot_choice == "ножницы":
        msg = "Победа"
        user_points += 1
    elif user_choice == "бумага" and bot_choice == "камень":
        msg = "Победа"
        user_points += 1
    elif user_choice == "ножницы" and bot_choice == "бумага":
        msg = "Победа"
        user_points += 1
    else:
        msg = "Ты проиграл"
        comp_points += 1 
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=['reset'])
def reset(message):
    user_points = 0
    comp_points = 0
    bot.send_message(message.chat.id, "Ну  блина я не зачитал сколько очков, это рофл просто очки обнулены, ")

@bot.message_handler(commands=['points'])
def points(message):
    bot.send_message(message.chat.id, f"бот: {comp_points}  игрок: {user_points}")

bot.polling(none_stop=True)