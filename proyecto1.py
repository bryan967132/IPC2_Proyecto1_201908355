from xml.dom import minidom
#import xml.etree.ElementTree as ET
myDoc = minidom.parse('./entrada.xml')
pisosArtesanales = myDoc.getElementsByTagName('piso')
for piso in pisosArtesanales:
    print("Piso:",piso.attributes['nombre'].value.replace(" ","").replace("\n",""))
    r = piso.getElementsByTagName('R')[0].firstChild.data.replace(" ","").replace("\n","")
    c = piso.getElementsByTagName('C')[0].firstChild.data.replace(" ","").replace("\n","")
    f = piso.getElementsByTagName('F')[0].firstChild.data.replace(" ","").replace("\n","")
    s = piso.getElementsByTagName('S')[0].firstChild.data.replace(" ","").replace("\n","")
    print("Filas:",r)
    print("Columnas:",c)
    print("Costo por voltear:",f)
    print("Costo por intercambiar:",s)
    patrones = piso.getElementsByTagName('patron')
    for patron in patrones:
        codigP = patron.attributes['codigo'].value.replace(" ","").replace("\n","")
        patPat = patron.firstChild.data.replace(" ","").replace("\n","")
        print("Código patrón:",codigP)
        print("Patrón:",patPat)
    print()

#for piso in pisosArtesanales:
#    print("Piso:",piso.attrib['nombre'])
#    for campos in piso:
#        print(campos.text)