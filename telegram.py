import time, os
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import telebot
from bs4 import BeautifulSoup
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")

# Configurando o bot do Telegram

bot = telebot.TeleBot(TOKEN)



# Configurando o Selenium
chrome_options = Options()
chrome_options.add_argument('--headless')  # Rodar em segundo plano
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Edge(options=chrome_options)

# Função para obter notícias do site
def obter_noticias():
    url = "https://www.otakupt.com/"
    driver.get(url)
    time.sleep(5)  # Espera para garantir que a página seja totalmente carregada
    pagina = BeautifulSoup(driver.page_source, 'html.parser')
    lista_noticias = pagina.find_all("a", class_="td-image-wrap")

    noticias = []
    for noticia in lista_noticias[1:10]:
        titulo = noticia.get("title")
        link = noticia.get("href")
        noticias.append((titulo, link))

    return noticias

# Função para enviar as notícias pelo Telegram
def enviar_noticias():
    noticias = obter_noticias()
    for titulo, link in noticias:
        mensagem = f"{titulo}\n{link}"
        print(mensagem)
        bot.send_message(USERID, mensagem)  # Substitua 'seu_id_telegram' pelo seu ID do Telegram
        time.sleep(1)  # Espera para não sobrecarregar o envio de mensagens

# # Agendamento para enviar notícias duas vezes ao dia
# while True:
#     # Defina a hora que deseja enviar as notícias
#     # Aqui, definimos para enviar às 9h e 18h (horário do Brasil)
#     hora_envio = ['09:00', '18:00']
#     hora_atual = time.strftime('%H:%M')
#     if hora_atual in hora_envio:
#         enviar_noticias()
#         time.sleep(60)  # Aguarda 60 segundos para evitar reenviar no mesmo minuto
#     time.sleep(60)  # Verifica a hora a cada minuto

enviar_noticias()