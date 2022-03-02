import os
import webbrowser
class graficar:
    def dibujar(self,f,c,mosaico):
        mosaicodot = ''
        mosaicodot += """
    Foo[
        label=<
            <table border="0" cellborder="1" cellspacing="0" cellpadding="4">"""
        i = 0
        while i < f:
            mosaicodot += """
                <tr>"""
            j = 0
            while j < c:
                if mosaico.get(i,j) == 'B':
                    mosaicodot += """
                    <td bgcolor = "black" height = "60" width = "80"></td>"""
                else:
                    mosaicodot += """
                    <td bgcolor = "white" height = "60" width = "80"></td>"""
                j += 1
            mosaicodot += """
                </tr>"""
            i += 1
        mosaicodot += """ 
            </table>
        >
    ];"""
        return mosaicodot
    
    def conectar(self,x):
        mosaicodot = ''
        i = 1
        while i < x:
            mosaicodot += """
    Foo""" + str(x - 1) + " -> " + "Foo" + str(x)
            i += 1
        return mosaicodot
    
    def getDot(self,cuerpo,conectado):
        mosaicodot = """digraph {
    node [shape = none]
    rankdir=DOWN;\n"""
        mosaicodot += cuerpo
        mosaicodot += conectado
        mosaicodot += """
}"""
        return mosaicodot

    def exportPDF(self,nombre,mosaicodot):
        dot = nombre + '.txt'
        with open('Archivos/' + dot,'w') as mosaico:
            mosaico.write(mosaicodot)
        pdf = 'Inicio.pdf'
        os.system("circo -Tpdf Archivos/" + dot + " -o " + pdf)
        webbrowser.open(pdf)

    def parsePDF(self,nombre):
        dot = nombre + '.txt'
        pdf = 'Final.pdf'
        os.system("circo -Tpdf Archivos/" + dot + " -o " + pdf)
        webbrowser.open(pdf)

    def exportPNG(self,i,mosaicodot):
        dot = 'Archivos/mosaico' + str(i) + '.txt'
        with open(dot,'w') as mosaico:
            mosaico.write(mosaicodot)
        png = 'Patrones/mosaico' + str(i) + '.png'
        os.system("circo -Tpng " + dot + " -o " + png)
        #webbrowser.open(png)