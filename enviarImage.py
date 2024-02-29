import os
import telebot
import pyautogui

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")

# Configurando o bot do Telegram
bot = telebot.TeleBot(TOKEN)



# Envia a foto junto com a mensagem para o usuário
@bot.message_handler(commands=['print'])
def send_image(message):
    screenshot = pyautogui.screenshot()
    screenshot.save("arquivo.png")
    with open("arquivo.png", 'rb') as photo:
        bot.send_photo(USERID, photo, caption="Print da tela")
    os.remove("arquivo.png")

# Inicie o bot
bot.polling()
