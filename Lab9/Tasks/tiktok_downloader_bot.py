import telebot
import requests
from safe import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привіт! Надішли мені посилання на відео з TikTok, і я його скачаю 🎬')

@bot.message_handler(func=lambda message: 'tiktok.com' in message.text)
def handle_tiktok_link(message):
    url = message.text.strip()
    bot.send_message(message.chat.id, "⏳ Завантажую відео...")

    try:
        api_url = "https://tikwm.com/api/"
        response = requests.get(api_url, params={"url": url})
        data = response.json()

        if data['code'] != 0:
            bot.send_message(message.chat.id, "❌ Не вдалося завантажити відео. Спробуй інше посилання.")
            return

        video_url = data['data']['play']  # посилання на mp4
        caption = data['data']['title']

        # Надсилання відео користувачу
        bot.send_video(message.chat.id, video=video_url, caption=caption)

    except Exception as e:
        bot.send_message(message.chat.id, f"⚠️ Сталася помилка: {e}")

@bot.message_handler(func=lambda message: True)
def fallback(message):
    bot.send_message(message.chat.id, "👋 Надішли посилання на TikTok відео, щоб я міг його завантажити.")

bot.polling(none_stop=True)