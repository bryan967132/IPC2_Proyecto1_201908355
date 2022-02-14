from xml.dom import minidom
#import xml.etree.ElementTree as ET
myDoc = minidom.parse('./entrada.xml')
pisosArtesanales = myDoc.getElementsByTagName('piso')
for piso in pisosArtesanales:
    print("Piso:",piso.attributes['nombre'].value.replace(" ","").replace("\n",""))
    r = piso.getElementsByTagName('R')
    c = piso.getElementsByTagName('C')
    f = piso.getElementsByTagName('F')
    s = piso.getElementsByTagName('S')
    print("Filas:",r[0].firstChild.data.replace(" ","").replace("\n",""))
    print("Columnas:",c[0].firstChild.data.replace(" ","").replace("\n",""))
    print("Costo por voltear:",f[0].firstChild.data.replace(" ","").replace("\n",""))
    print("Costo por intercambiar:",s[0].firstChild.data.replace(" ","").replace("\n",""))
    patrones = piso.getElementsByTagName('patron')
    for patron in patrones:
        print("Código patrón:",patron.attributes['codigo'].value.replace(" ","").replace("\n",""))
        print("Patrón:",patron.firstChild.data.replace(" ","").replace("\n",""))
    print()

#for piso in pisosArtesanales:
#    print("Piso:",piso.attrib['nombre'])
#    for campos in piso:
#        print(campos.text)