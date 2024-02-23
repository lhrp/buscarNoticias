import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak
from reportlab.lib.styles import getSampleStyleSheet

def criar_pdf(listaNoticias, autor):
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
        story.append(Paragraph(cNoticia, style_body))
        story.append(Paragraph(cLinkNoticia, style_body))
        story.append(Paragraph("\n", style_body))
        # Adiciona uma quebra de página para separar cada notícia
        story.append(PageBreak())

    doc.build(story)
    return pdf_filename

listaNoticias = [
    {"nCdNoticia":1,"dExtracaoNoticias":"2024-02-23T14:16:09.397","cTituloNoticia":"Noticia 1","cLinkNoticia":"Link da Noticia 1","cNoticia":"Corpo do Texto da Noticia 1"},
    {"nCdNoticia":2,"dExtracaoNoticias":"2024-02-23T14:16:09.397","cTituloNoticia":"Noticia 2","cLinkNoticia":"Link da Noticia 2","cNoticia":"Corpo do Texto da Noticia 2"},
    {"nCdNoticia":3,"dExtracaoNoticias":"2024-02-23T14:16:09.397","cTituloNoticia":"Noticia 3","cLinkNoticia":"Link da Noticia 3","cNoticia":"Corpo do Texto da Noticia 3"},
    {"nCdNoticia":4,"dExtracaoNoticias":"2024-02-23T14:16:09.397","cTituloNoticia":"Noticia 4","cLinkNoticia":"Link da Noticia 4","cNoticia":"Corpo do Texto da Noticia 4"},
    {"nCdNoticia":5,"dExtracaoNoticias":"2024-02-23T14:16:09.397","cTituloNoticia":"Noticia 5","cLinkNoticia":"Link da Noticia 5","cNoticia":"Corpo do Texto da Noticia 5"}
]

autor = "LHRP"  # Defina o autor aqui

pdf_filename = criar_pdf(listaNoticias, autor)
