from xml.dom import minidom
from pisos import list_e_pis,piso_Artesanal
from patrones import list_e_pat,piso_Patron
#import xml.etree.ElementTree as ET
myDoc = minidom.parse('./entrada.xml')
pisosArtesanales = myDoc.getElementsByTagName('piso')

lista_piso = list_e_pis()

for piso in pisosArtesanales:
    nom = piso.attributes['nombre'].value.replace(" ","").replace("\n","")
    r = piso.getElementsByTagName('R')[0].firstChild.data.replace(" ","").replace("\n","")
    c = piso.getElementsByTagName('C')[0].firstChild.data.replace(" ","").replace("\n","")
    f = piso.getElementsByTagName('F')[0].firstChild.data.replace(" ","").replace("\n","")
    s = piso.getElementsByTagName('S')[0].firstChild.data.replace(" ","").replace("\n","")

    patrones = piso.getElementsByTagName('patron')

    lista_patron = list_e_pat()

    for patron in patrones:
        codigP = patron.attributes['codigo'].value.replace(" ","").replace("\n","")
        patPat = patron.firstChild.data.replace(" ","").replace("\n","")

        nuevoPatron = piso_Patron(codigP,patPat)
        lista_patron.insertar(nuevoPatron)

    nuevoPiso = piso_Artesanal(nom,r,c,f,s,lista_patron)
    lista_piso.insertar(nuevoPiso)

lista_piso.recorrer()

#for piso in pisosArtesanales:
#    print("Piso:",piso.attrib['nombre'])
#    for campos in piso:
#        print(campos.text)