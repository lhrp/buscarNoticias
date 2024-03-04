import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Image
from reportlab.lib.styles import getSampleStyleSheet

def criar_pdf(listaNoticias):
    autor = "LHRP"  # Defina o autor aqui
    pdf_filename = f"DailyNews_{time.strftime('%Y-%m-%d_%Hh%M')}.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter, author=autor)  # Definindo o autor aqui
    styles = getSampleStyleSheet()
    style_title = styles['Title']
    style_body = styles['Normal']
    story = []

    for item in listaNoticias:
        nCdNoticia = item['nCdNoticia']
        dExtracaoNoticias = item['dExtracaoNoticias']
        cTituloNoticia = item['cTituloNoticia']
        cLinkNoticia = item['cLinkNoticia']
        cNoticia = item['cNoticia']



        story.append(Paragraph(cTituloNoticia, style_title))
        story.append(Paragraph(cLinkNoticia, style_body))
                # Carregar a imagem a partir do dicionário de dados
        if 'cImagem' in item:
            imagem_path = item['cImagem']
            story.append(Image(imagem_path, width=300, height=200))  # Adiciona a imagem
            story.append(Paragraph("\n", style_body))  # Adiciona uma quebra de linha após a imagem
        story.append(Paragraph(cNoticia, style_body))
        story.append(Paragraph("\n", style_body))
        # Adiciona uma quebra de página para separar cada notícia
        story.append(PageBreak())

    doc.build(story)
    return pdf_filename

listaNoticias = [
    {'nCdNoticia': 1, 'dExtracaoNoticias': '2024-02-28 22:47:37.432839', 'cTituloNoticia': 'Imagem promocional do filme anime Overlord: The Sacred Kingdom', 'cLinkNoticia': 'https://www.otakupt.com/anime/imagem-promocional-do-filme-anime-overlord-the-sacred-kingdom/', 'cNoticia': 'Tempor dolor ad quis excepteur amet nisi amet officia voluptate aute non. Amet fugiat dolor laborum incididunt nisi magna exercitation minim consequat ullamco ex veniam aute. Pariatur aliqua veniam aliquip eu incididunt laborum laborum ullamco magna. In et est quis reprehenderit est officia. Ullamco labore esse reprehenderit Lorem eu. Tempor veniam qui ad labore labore exercitation excepteur aliquip dolor ad amet. Commodo exercitation officia est do est.', 'cImagem': r'C:\Users\leonardopaulino-mtz\Pictures\Original\36.png'},
    {'nCdNoticia': 2, 'dExtracaoNoticias': '2024-02-28 22:47:37.432839', 'cTituloNoticia': 'Nova imagem promocional de Re:ZERO 3', 'cLinkNoticia': 'https://www.otakupt.com/anime/nova-imagem-promocional-de-rezero-3/', 'cNoticia': 'Quis consectetur minim deserunt amet. Cupidatat pariatur ipsum aute dolore velit minim elit officia Lorem cupidatat mollit consectetur. Minim consequat elit nulla do laborum. Magna mollit laborum pariatur quis ad nostrud ea excepteur aliquip. Tempor tempor eiusmod qui occaecat consequat laboris ullamco ullamco. Sunt anim consectetur consequat aliquip fugiat fugiat adipisicing commodo commodo nostrud occaecat anim cupidatat pariatur. Aliqua deserunt ut ipsum fugiat laborum in magna magna non nostrud et enim.', 'cImagem': r'C:\Users\leonardopaulino-mtz\Pictures\Original\Uno.png'},
]

pdf_filename = criar_pdf(listaNoticias)
