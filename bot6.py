from time import time

from telebot import TeleBot
from telebot.types import Message


TOKEN = "8079541325:AAEfE0O-YyxqJ0O4ZchKF8aOy5iZe8ysDuI"
bot = TeleBot(TOKEN)

with open("bad_words.txt", "r", encoding="utf-8") as file:
    data = [word.strip().lower() for word in file.readlines()]

def has_bad_words(text: str) -> bool:
    words = text.split(" ")
    for word in words:
        if word in data:
            return True
    return False

@bot.message_handler(chat_types=["group", "supergroup"], func=lambda message: message.entities is not None)
def delete_link(message: Message):
    for entity in message.entities:
        if entity.type in ("url", "text_link"):
            bot.delete_message(message.chat.id, message.message_id)

@bot.message_handler(chat_types=["group", "supergroup"], func=lambda message: has_bad_words(message.text.lower()) and is_group(message))
def ban_user(message: Message):
    chat_member = bot.ban_chat_member(call.message.chat.id, call.message.from_user.id)

    if chat_member.status in ("administrator", "creator"):
        bot.send_message(message.chat.id, "Хозяин вернулся", reply_to_message_id=message.message_id)
    else:
        bot.restrict_chat_member(message.chat.id, message.from_user.id, until_darte=time()+1200)
        bot.send_message(message.chat.id, f"Тебе бан на 20 минут\n{censor_message}", reply_to_message_id=message.message_id)
        bot.delete_message(message.chat.id, message.message_id)

bot.polling(non_stop=True)
