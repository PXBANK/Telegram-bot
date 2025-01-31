import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен из переменных окружения
bot = telebot.TeleBot(TOKEN)

# Список фильмов (можно заменить на базу данных)
films = {
    "Фильм 1": "https://link_to_video1.mp4",
    "Фильм 2": "https://link_to_video2.mp4"
}

@bot.message_handler(commands=["start"])
def send_welcome(message):
    text = "Привет! Выберите фильм:\n" + "\n".join(films.keys())
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda msg: msg.text in films)
def send_film(message):
    bot.send_message(message.chat.id, f"Вот ваш фильм: {films[message.text]}")

bot.polling()
