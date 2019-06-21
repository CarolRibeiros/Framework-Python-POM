from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os
from Resources.Functions import Reader
from datetime import datetime


class Evidencia():

    def __init__(self, driver):
        self.driver = driver


    def screenshot(self, img_name):
        self.driver.save_screenshot(Reader.getProperty("screenshot_path") + "/" + datetime.now().strftime("%H-%M-%S.")
                                    + img_name + ".png")


    def gerar_evidencia(self, test_name, env, status, start_time, end_time, error_msg):
        doc = SimpleDocTemplate(Reader.getProperty("save_report_path") + "/" + datetime.now().strftime("%d-%m-%Y %H.%M.%S.")
                                + test_name  + ".pdf",
                                pagesize=A4,
                                rightMargin=40, leftMargin=40,
                                topMargin=20, bottomMargin=10)
        Story = []
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))

        # imgs logo
        logo_sempre = Reader.getProperty("logo_sempre_path")
        logo_alfa = Reader.getProperty("logo_alfa_path")

        im_sempre = Image(logo_sempre, 2.5 * inch, 1 * inch, hAlign='LEFT')
        Story.append(im_sempre)
        Story.append(Spacer(1, 70))

        im_alfa = Image(logo_alfa)
        Story.append(im_alfa)
        Story.append(Spacer(1, 80))

        # Nome CT
        ptext = '<font size=16><b>Caso de Teste: %s</b></font>' % test_name
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 340))

        # Ambiente
        ptext = '<font size=14>Ambiente: %s</font>' % env
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 10))

        # Status
        ptext = '<font size=14>Status: %s</font>' % status
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 10))

        # data inicio
        ptext = '<font size=14>Data ínicio: %s</font>' % start_time
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 10))

        # data fim
        ptext = '<font size=14>Data fim: %s</font>' % end_time
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 10))

        #Duração
        duration = (datetime.strptime(end_time, '%d/%m/%Y %H:%M:%S') - \
                         datetime.strptime(start_time, '%d/%m/%Y %H:%M:%S')).total_seconds()
        ptext = '<font size=14>Duração: %s</font>' % duration
        Story.append(Paragraph(ptext, styles["Normal"]))
        Story.append(Spacer(1, 30))

        # Adiciona screenshots
        diretorio = os.listdir(Reader.getProperty("screenshot_path"))
        for img in diretorio:
            texto = img.split('.')
            ptext = '<font size=14>%s</font>' % texto[1]
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 10))

            screenshot = Image(Reader.getProperty("screenshot_path") + "/" +img, 7.25 * inch, 4.5 * inch, hAlign='LEFT')
            Story.append(screenshot)
            Story.append(Spacer(1, 40))

        # Falha
        if error_msg != None:
            ptext = '<font size=14>Falha: %s</font>' %error_msg
            Story.append(Paragraph(ptext, styles["Normal"]))
            Story.append(Spacer(1, 10))
        else:
            pass

        doc.build(Story)


    def limpar_screenshot(self):
        for img in os.listdir(Reader.getProperty("screenshot_path")):
            os.remove(Reader.getProperty("screenshot_path") + "/" + img)
