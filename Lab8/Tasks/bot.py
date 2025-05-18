import telebot
from safe import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start']) #/start 
def start_message(message):
    bot.send_message(message.chat.id, 
"""📞 Привіт! Я *Телефончик* — твій бот-помічник.  
Введи /help, щоб дізнатись, що я вмію.  
👂 Я слухаю тебе уважно...""", parse_mode='Markdown')
    
@bot.message_handler(commands=['help']) #/help
def help_message(message):
    bot.send_message(message.chat.id, 
"""/time — Показати поточний час
/echo _текст_ — Повторити те, що ти написав
/sticker — Відправити стікер
/github — Показати посилання на GitHub
/clear — Очистити чат
/stop — Зупинити бота""", parse_mode='Markdown')

@bot.message_handler(commands=['time']) #/time
def time_message(message):
    import datetime as dt
    now = dt.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    bot.send_message(message.chat.id, f"🕒 Поточний час: {current_time}")

@bot.message_handler(commands=['echo']) #/echo text
def echo_message(message):
    text = message.text.split(' ', 1)
    if len(text) > 1: bot.send_message(message.chat.id, f"🔊 {text[1]}")
    else: bot.send_message(message.chat.id, "🔈 ")

@bot.message_handler(commands=['sticker']) #/sticker
def sticker_message(message):
    import random as r
    stickers = [
        'CAACAgIAAxkBAAEOg8BoKd3zPnkLFGj5f-tIpQ7avEXFeAACDicAAh5v0EmbtU7CYB0N-zYE',
        'CAACAgIAAxkBAAEOg8RoKd4lgJQ7IF5yo715JpdaoIzdGAACjxIAAiXVsEi_4Q-PyoPsCjYE',
        'CAACAgIAAxkBAAEOg8toKd5bXOeEqWiWrMTeBEDnWm-5wAACSBQAAmoz4UlQCUG0FKMZiTYE',
        'CAACAgIAAxkBAAEOg81oKd6Y6zFIjj6mMfbhaRIWAAEWBlkAAioAA9cyTx5rOenqNdJhsDYE',
        'CAACAgIAAxkBAAEOg89oKd7ZuseKOdYcsDCOW5gKb2Y1vwACfEYAAsw0yUrTDUa1JsYxFjYE',
        'CAACAgIAAxkBAAEOg9NoKd-QsJoGDHhUg5hdAAFq2vY-ndUAAoYVAALIfNBLwdWIqWyiYM42BA',
        'CAACAgIAAxkBAAEOg9VoKeBIKsQMaOQMNI9agn0HreFUgAAC8iAAAmUl2EonKSfn8aLdXDYE',
        'CAACAgIAAxkBAAEOg9loKeC8IfpIJ0WvL-HQtzIodiaEYgACpBcAAmSD0EvrOstI8mPpVDYE'
    ]
    sticker_id = r.choice(stickers)
    bot.send_sticker(message.chat.id, sticker_id)

@bot.message_handler(commands=['github']) #/github
def github_message(message): bot.send_message(message.chat.id, "🔗 *Мій GitHub:* [movavok](https://github.com/movavok)", parse_mode='Markdown')

@bot.message_handler(commands=['stop']) #/stop
def stop_message(message):
    bot.send_message(message.chat.id, "👋 Бувай! Якщо захочеш повернутись — ввімкни мене знову.")
    bot.stop_polling()

@bot.message_handler(commands=['clear']) #/clear
def clear_message(message):
    try:
        for i in range(message.message_id, 0, -1):
            try: bot.delete_message(message.chat.id, i)
            except: continue
        bot.send_message(message.chat.id, "🧹 Чат очищено! Тепер тут чисто.")
    except: bot.send_message(message.chat.id, "❌ На жаль, я не можу видалити всі повідомлення. Можливо, у мене немає прав адміністратора.")

def unknown_message(message): bot.send_message(message.chat.id, "🤔 Я не знаю, що з цим робити. Введи /help, щоб дізнатись, що я вмію.")

@bot.message_handler(content_types=['text']) #розпізнавання тексту
def handle_specific_text(message):
    text = message.text.lower()
    if text in ["привіт", "доброго ранку", "доброго дня", "доброго вечора", "привіт!"]: bot.send_message(message.chat.id, "👋 Вітаю! /help, щоб дізнатись, що я вмію.")
    elif text in ["дякую", "дякую!"]: bot.send_message(message.chat.id, "🤗 Завжди радий допомогти!")
    elif text == "як справи?": bot.send_message(message.chat.id, "🙃 У мене все добре, дякую!")
    elif text == "котра година?": time_message(message)
    elif text == "стікер": sticker_message(message)
    elif text == "оцінка": bot.send_message(message.chat.id, "⭐️ 5/5")
    elif text == "погода": bot.send_message(message.chat.id, "🌤️ Погода завжди гарна, коли ти поруч!")
    else:unknown_message(message)

bot.polling(none_stop=True)