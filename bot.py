from random import randint, choice
from telebot import TeleBot

TOKEN = "7493646951:AAE_PU5ewJsthzZnxNEHqBq9FfJQ4X9kVhk"
bot = TeleBot(TOKEN)


jokes = [
    'Решили дед и бабка не повторять прошлых ошибок и вместо колобка испекли кубик.',
    "При встрече с медведем постарайся не совершать резких движений, не есть из его миски"
    "- Вовочка, приведи пример одноклеточных. \n- Два хомяка в одной клетке."
]



@bot.message_handler(commands=["sum"])
def start(message):
    vals = message.text.split(' ')
    number = int(vals[1]) + int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=["sub"])
def start(message):
    vals = message.text.split(' ')
    number = int(vals[1]) - int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=["share"])
def start(message):
    vals = message.text.split(' ')
    number = int(vals[1]) / int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler(commands=["multiply"])
def start(message):
    vals = message.text.split(' ')
    number = int(vals[1]) * int(vals[2])
    bot.send_message(message.chat.id, number)

@bot.message_handler()
def start(message):
    if message.text == "как дела?":
        bot.send_message(message.chat.id, "Хорошо а у тебя?")
        return
    if message.text == "Что делаешь?":
        bot.send_message(message.chat.id, "Бип бип...")
        return
    if message.text == "пошути":
        bot.send_message(message.chat.id, choice(jokes))
        return
    bot.send_message(message.chat.id, message.text)



if __name__ == '__main__':
    bot.polling(none_stop=True)