import telebot
from safe import exm_token
from pyowm import OWM
from pyowm.utils.config import get_default_config


bot = telebot.TeleBot(exm_token)
config_dict = get_default_config()
config_dict['language'] = 'ua'
owm = OWM( '0f8480e94c08f6fa663ead777cd2ee53', config_dict )

@bot.message_handler(commands=['start']) #реакція чат бота на стартову команду
def start_message(message):
    bot.send_message(message.chat.id, 'Ваше повідомлення /start')

@bot.message_handler(commands=['city']) #команда для отримання початкових даних
def cmd_city(message):
    send = bot.send_message(message.chat.id, 'Введи місто')
    bot.register_next_step_handler(send, city)

def city(message): #основна робота з декількома варіантами в залежності від результату
    try:
        bot.send_message(message.chat.id, 'Дізнаюсь погодні умови в місті {city}'.format(city=message.text))
        data = message.text
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(data)
        w = observation.weather
        t = w.temperature('celsius')['temp']
        
        answer = f"В місті {message.text} зараз {w.detailed_status} \n"
        answer += f"Приблизна температура {round(t)} ℃\n\n"
     
        if t < 0:
            answer += 'Зараз температура нижче нуля, одягайся тепліше!'
            bot.send_animation(message.chat.id, 'https://media1.tenor.com/m/Xv92ltSnupgAAAAd/gosling-sad-gosling.gif')
        elif t < 15:
            answer += 'Зараз прохолодно, варто тепліше одягтися!'
            bot.send_animation(message.chat.id, 'https://media1.tenor.com/m/tgLuPlO6kz8AAAAd/what-gosling.gif')
        else:
            answer += 'Зараз досить тепло, можна одягтися легко!'
            bot.send_animation(message.chat.id, 'https://media1.tenor.com/m/F1z461rxQdwAAAAd/gosling-barbie.gif')

        bot.send_message(message.chat.id, answer)
        
    except Exception as e:
        print(f"Помилка: {e}")
        bot.send_message(message.chat.id, "❌ Помилка! Можливо, ви ввели неправильну назву міста. Спробуйте ще раз.")

bot.polling(none_stop=True) # необхідно, щоб бот не вимкнувся одразу