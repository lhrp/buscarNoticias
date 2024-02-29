import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
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
        story.append(Paragraph(cNoticia, style_body))
        story.append(Paragraph("\n", style_body))
        # Adiciona uma quebra de página para separar cada notícia
        story.append(PageBreak())

    doc.build(story)
    return pdf_filename

listaNoticias = [
    {'nCdNoticia': 1, 'dExtracaoNoticias': '2024-02-28 22:47:37.432839', 'cTituloNoticia': 'Imagem promocional do filme anime Overlord: The Sacred Kingdom', 'cLinkNoticia': 'https://www.otakupt.com/anime/imagem-promocional-do-filme-anime-overlord-the-sacred-kingdom/', 'cNoticia': 'Testes'},
    {'nCdNoticia': 2, 'dExtracaoNoticias': '2024-02-28 22:47:37.432839', 'cTituloNoticia': 'Nova imagem promocional de Re:ZERO 3', 'cLinkNoticia': 'https://www.otakupt.com/anime/nova-imagem-promocional-de-rezero-3/', 'cNoticia': 'Testes'},
]


pdf_filename = criar_pdf(listaNoticias)
