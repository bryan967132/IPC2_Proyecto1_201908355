#from menu import menu
#m = menu()
#m.menuP()

from parseXML import parseXML
from otrasF import oFunc
from princF import pFunc

lista_piso = parseXML().getXML('entrada.xml')

piso1 = "ejemplo02"
ptrn1 = "cod21"
f = lista_piso.getF(piso1)
c = lista_piso.getC(piso1)
piso2 = "ejemplo02"
ptrn2 = "cod22"
mosaico1 = lista_piso.getMos(piso1,ptrn1)
mosaico2 = lista_piso.getMos(piso2,ptrn2)

costInt = lista_piso.getCostI(piso1)
costVolt = lista_piso.getCostV(piso1)

p = oFunc()
p.printMos(f,c,mosaico1)
p.printMos(f,c,mosaico2)

d = pFunc()
pares = d.getCantCol(f,c,mosaico1,mosaico2)
#p.printPar(pares)
color = d.getMenorC(pares)
#print('\n' + color)
priSec = d.getPriSec(pares)
#print(priSec.get(0),priSec.get(1))
crd1 = d.getCrd(f,c,mosaico1,color)
#p.printCrd(priSec.get(0),color,crd1)
crd2 = d.getCrd(f,c,mosaico2,color)
#p.printCrd(priSec.get(1),color,crd2)
rutas = d.getRutas(priSec.get(0),priSec.get(1),crd1,crd2)
#p.printRutas(priSec.get(0) * priSec.get(1),rutas)
lenRutas = d.cantOpt(priSec.get(0) * priSec.get(1),rutas)
rutas = d.optRutas(priSec.get(0) * priSec.get(1),rutas)
#p.printRutas(lenRutas,rutas)
rutas = d.crearCaminos(mosaico1,lenRutas,rutas,priSec.get(1),crd2,color)
lenRutas = d.optCmns(mosaico1,priSec.get(1),crd2,color)
#p.printRutas(lenRutas,rutas)
intercambios = d.getMovT(f,c,lenRutas,rutas,mosaico1,mosaico2,color)
volteos = d.getVoltT(f,c,lenRutas,rutas,mosaico1,mosaico2,color)
minCost = d.minCost(intercambios,volteos,costInt,costVolt)
print('Costo Mínimo: Q',minCost)
print('Intercambios:',intercambios)
print('Volteos:',volteos,'\n')
print('Transición')
p.printMos(f,c,mosaico1)
d.transMos(f,c,lenRutas,rutas,mosaico1,mosaico2,color)