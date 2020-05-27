import json
import telebot
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types

with open("param_tel_bot.txt", "r") as param_tele_bot_file:
    param_tele_bot = json.load(param_tele_bot_file)

bot = telebot.TeleBot(param_tele_bot["token"])

# Метод, который получает сообщения и обрабатывает их
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, Bro")
        # Готовим кнопки
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_testimony = types.InlineKeyboardButton(text='Передать показания', callback_data='testimony')
        # И добавляем кнопку на экран
        keyboard.add(key_testimony)
        bot.send_message(message.from_user.id, text='Чё будем делать?', reply_markup=keyboard)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    if call.data == "testimony":

        msg = 'Напиши показания холодной воды'

        bot.send_message(call.message.chat.id, msg)

# Запускаем постоянный опрос бота в Телеграме
bot.polling(none_stop=True, interval=0)