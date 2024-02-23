import requests, bs4, telebot, time


# Configurando o bot do Telegram
TOKEN = '5354237813:AAG5C7CglIyaGddlNfjmIbJOCs2Zr2gE48M'
bot = telebot.TeleBot(TOKEN)


##Obtendo os elementos de link da página, que contenham o link do post
##Exemplo do GE


def obter_noticias(qtdNoticias):
    url = "https://www.otakupt.com/"
    requisicao = requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    listaNoticias = pagina.find_all("a", class_="td-image-wrap") ##Buscando a tag <a>, que contenham a tag "feed-post-link"

    noticias = []

    for noticia in listaNoticias[:qtdNoticias]:
        titulo = noticia.get("title")
        link = noticia.get("href")
        noticias.append((titulo, link))

    return noticias

def enviar_noticias():
    noticias = obter_noticias(3)

    for titulo, link in noticias:
            mensagem = f"{titulo}\n{link}"
            print(mensagem)
            bot.send_message('643003849', mensagem)  # Substitua 'seu_id_telegram' pelo seu ID do Telegram
            time.sleep(1) 


enviar_noticias()