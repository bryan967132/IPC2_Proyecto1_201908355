#from menu import menu
#m = menu()
#m.menuP()

from parseXML import parseXML
lista_piso = parseXML().getXML('entrada.xml')

piso1 = "ejemplo02"
ptrn1 = "cod21"
piso2 = "ejemplo02"
ptrn2 = "cod22"
patron1 = lista_piso.getMos(piso1,ptrn1)
patron2 = lista_piso.getMos(piso2,ptrn2)
f = lista_piso.getF(piso1)
c = lista_piso.getC(piso1)

mos1 = ""
for i in range(f):
    for j in range(c):
        mos1 += str(patron1.get(i,j)) + " "
    mos1 += "\n"
print(mos1)

mos2 = ""
for i in range(f):
    for j in range(c):
        mos2 += str(patron2.get(i,j)) + " "
    mos2 += "\n"
print(mos2)