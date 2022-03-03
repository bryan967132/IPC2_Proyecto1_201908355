from xml.dom import minidom
from pisos import list_e_pis,piso_Artesanal
from patrones import list_e_pat,piso_Patron
from patron import list_e_pc,patron_C
class parseXML:
    def getXML(self,ruta):
        myDoc = minidom.parse(ruta)
        pisosArtesanales = myDoc.getElementsByTagName('piso')

        lista_piso = list_e_pis()

        for piso in pisosArtesanales:
            nom = piso.attributes['nombre'].value.replace(" ","").replace("\n","")
            r = 0;c = 0;f = 0;s = 0
            for elemento in piso.getElementsByTagName('R'):
                r = int(elemento.firstChild.data)
            for elemento in piso.getElementsByTagName('C'):
                c = int(elemento.firstChild.data)
            for elemento in piso.getElementsByTagName('F'):
                f = float(elemento.firstChild.data)
            for elemento in piso.getElementsByTagName('S'):
                s = float(elemento.firstChild.data)

            patrones = piso.getElementsByTagName('patron')

            lista_patron = list_e_pat()

            for patron in patrones:
                codigP = str(patron.attributes['codigo'].value.replace(" ","").replace("\n",""))
                patPat = str(patron.firstChild.data.replace(" ","").replace("\n",""))

                lista_color = list_e_pc()
                x = 0
                y = 0
                for color in patPat:
                    nuevoColor = patron_C(y,x,color)
                    lista_color.insertar(nuevoColor)
                    if x == c - 1:
                        x = -1
                        y += 1
                    x += 1

                nuevoPatron = piso_Patron(codigP,lista_color)
                lista_patron.insertar(nuevoPatron)

            nuevoPiso = piso_Artesanal(nom,r,c,f,s,lista_patron)
            lista_piso.insertar(nuevoPiso)
        
        return lista_piso