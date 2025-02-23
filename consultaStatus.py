import requests
import time
from datetime import datetime
import telebot

# Substitua 'SEU_TOKEN' pelo token do seu bot no Telegram
TELEGRAM_TOKEN = ''
CHAT_ID = ''  # Substitua pelo ID do chat onde deseja receber as mensagens
WEBSITE_URL = ''  # Substitua pelo URL do site que deseja verificar


def enviaTelagram(mensagem):
    try:
        telegramToken = ""
        telegramChatID = ""
        
        bot = telebot.TeleBot(telegramToken)
        bot.send_message(telegramChatID, mensagem, timeout=5)
    except:
        pass

while True:
    try:
        response = requests.get(WEBSITE_URL)
        retorno = response.status_code == 200
    except requests.ConnectionError:
        print(requests.ConnectionError)
        retorno = False
    finally:
        response.close()
        print(retorno)
        if retorno == True:
            #print("Site está no ar")
            enviaTelagram(f"O site {WEBSITE_URL} está online! \nConsulta realizada em {datetime.now()}")
        else:
            # print("Site está fora do ar")
            enviaTelagram(f"O site {WEBSITE_URL} está offline! \nConsulta realizada em {datetime.now()}")
    time.sleep(600)  # Verifica a cada 10 minutos (3600 segundos) se o site está no ar
