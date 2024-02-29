import subprocess
import requests
import bs4
import telebot
import time
import os
import datetime
import pyautogui
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText  # Adicionando esta importação
from email import encoders


TOKEN = os.environ.get("TOKEN")
USERID = os.environ.get("USERID")
SENHAAPP = os.environ.get("SENHAAPP")
bot = telebot.TeleBot(TOKEN)

def converter_para_mobi(pdf_filename):
    titulo="Leonardo H R Paulino"
    mobi_filename = pdf_filename.replace(".pdf", ".epub")
    subprocess.run([r"C:\Program Files\Calibre2\ebook-convert", pdf_filename, mobi_filename, "--title", titulo])
    return mobi_filename

def enviar_email(destinatario, assunto, corpo, arquivo_anexo):
    remetente = "leoshuyaa@gmail.com"  # Insira seu endereço de e-mail aqui
    senha = SENHAAPP  # Insira sua senha de e-mail aqui

    # Configuração do servidor SMTP do Gmail
    servidor_smtp = "smtp.gmail.com"
    porta_smtp = 587

    # Criando o objeto MIMEMultipart
    msg = MIMEMultipart()

    # Configurando os parâmetros do e-mail
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Adicionando o corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Adicionando o arquivo PDF como anexo
    with open(arquivo_anexo, "rb") as anexo:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(anexo.read())
    
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename= {arquivo_anexo}")
    msg.attach(part)

    # Conectando-se ao servidor SMTP e enviando o e-mail
    servidor = smtplib.SMTP(host=servidor_smtp, port=porta_smtp)
    servidor.starttls()
    servidor.login(remetente, senha)
    texto_email = msg.as_string()
    servidor.sendmail(remetente, destinatario, texto_email)
    servidor.quit()


def criar_pdf(listaNoticias):
    autor = "LHRP"
    pdf_filename = f"DailyNews_{time.strftime('%Y-%m-%d_%Hh%M')}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, author=autor)
    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_body = styles['Normal']
    story = []

    for item in listaNoticias:
        cTituloNoticia = item['cTituloNoticia']
        cLinkNoticia = item['cLinkNoticia']
        
        # Extrair texto da notícia
        texto_noticia, _ = extrair_texto_e_imagem_noticia(cLinkNoticia)
        
        story.append(Paragraph(cTituloNoticia, style_title))
        story.append(Paragraph(cLinkNoticia, style_body))
        story.append(Paragraph(texto_noticia, style_body))
        story.append(Paragraph("\n", style_body))
        story.append(PageBreak())

    doc.build(story)
    return pdf_filename


def extrair_texto_e_imagem_noticia(url):
    requisicao = requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    texto_noticia = pagina.find("div", class_="td_block_wrap tdb_single_content tdi_51 td-pb-border-top td_block_template_1 td-post-content tagdiv-type").text.strip()
    imagem_noticia_tag = pagina.find("img", class_="alignnone size-full")
    imagem_noticia_src = None
    if imagem_noticia_tag:
        imagem_noticia_src = imagem_noticia_tag.get("src")
    return texto_noticia, imagem_noticia_src

def obter_noticias(qtdNoticias):
    url = "https://www.otakupt.com/"
    requisicao = requests.get(url)
    pagina = bs4.BeautifulSoup(requisicao.text, "html.parser")
    listaNoticias = pagina.find_all("a", class_="td-image-wrap")

    noticias = []

    for item, noticia in enumerate(listaNoticias[:qtdNoticias], start=1):
        titulo = noticia.get("title")
        link = noticia.get("href")
        #print(item)
        corpo_noticia = "Testes"
        dataAtual = datetime.datetime.now()
        dicionario_noticia = {
                "nCdNoticia": int(item),
                "dExtracaoNoticias": str(dataAtual),
                "cTituloNoticia": titulo,
                "cLinkNoticia": link,
                "cNoticia": ""  # Deixe o campo da notícia vazio por enquanto
            }
        #print(dicionario_noticia)
        noticias.append(dicionario_noticia)

    arquivoPDFGerado = criar_pdf(noticias)
    arquivoMOBIGerado = converter_para_mobi(arquivoPDFGerado)
    email_destinatario = "lleoshuya@kindle.com"  # Insira o endereço de e-mail do destinatário
    assunto = f'Notícias Diárias {datetime.datetime.now().strftime("%d/%m/%Y")}'
    corpo_email = "Segue em anexo as 10 primeiras notícias do site OtakuPT de Hoje ."
    enviar_email(email_destinatario, assunto, corpo_email, arquivoMOBIGerado)
    #os.remove(arquivoPDFGerado)
    return noticias

def enviar_noticias():
    noticias = obter_noticias(5)

    for noticia in noticias:
        mensagem = f"{noticia['cTituloNoticia']}\n{noticia['cLinkNoticia']}"#\n{noticia['cNoticia']}"
        bot.send_message(USERID, mensagem)
        time.sleep(1)

# Envia a foto junto com a mensagem para o usuário
@bot.message_handler(commands=['print'])
def enviarImagem(message):
    screenshot = pyautogui.screenshot()
    screenshot.save("arquivo.png")
    with open("arquivo.png", 'rb') as photo:
        bot.send_photo(USERID, photo, caption="Print da tela")
    os.remove("arquivo.png")

@bot.message_handler(commands=['news'])
def enviarMensagem(message):
    bot.send_message(USERID, "Processando envio das notícias.\nPor favor aguarde.")
    enviar_noticias()

# Inicie o bot
bot.polling()
