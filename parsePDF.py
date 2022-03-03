import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib.utils import ImageReader

class pdfExport:
    def exportarPDF(self,fil,col,pasos,instrucciones):
        w,h = A3
        c = canvas.Canvas("Instrucciones.pdf", pagesize=A3)
        c.drawString(50,h - 50,"Instrucciones")
        altura = 20
        i = 0
        while i <= pasos:
            izquierda = w / 2
            if i % 2 == 0:
                izquierda = 0
            if i < pasos:
                c.drawString(50 + izquierda,h - altura - 50,instrucciones.getInst(i + 1).replace("\n",""))
                c.drawString(55 + izquierda,h - altura - 70,instrucciones.getDetalles(i + 1).replace("\n",""))
            else:
                c.drawString(50 + izquierda,h - altura - 60,'Patrón Final')
            img = ImageReader('Patrones/mosaico' + str(i) + '.png')
            c.drawImage(img,65 + izquierda, h - altura - fil*15 - 85,width = col*20,height = fil*15)
            if i % 2 != 0:
                altura += 60 + fil*15
            if (h - altura - 90) <= 50:
                c.showPage()
                altura = 0
            i += 1
        c.save()
        webbrowser.open("Instrucciones.pdf")