from parseXML import parseXML
from otrasF import oFunc
from princF import pFunc

lista_piso = parseXML().getXML('entrada.xml')

piso1 = "ejemplo02"
ptrn1 = "cod21"
piso2 = "ejemplo02"
ptrn2 = "cod22"

f = lista_piso.getF(piso1)
c = lista_piso.getC(piso1)

mosaico1 = lista_piso.getMos(piso1,ptrn1)
mosaico2 = lista_piso.getMos(piso2,ptrn2)

costInt = lista_piso.getCostI(piso1)
costVolt = lista_piso.getCostV(piso1)
p = oFunc()
print()
p.printMos(f,c,mosaico1)
p.printMos(f,c,mosaico2)
d = pFunc()
pares = d.getCantCol(f,c,mosaico1,mosaico2)
color = d.getMenorC(pares)
priSec = d.getPriSec(pares)
crd1 = d.getCrd(f,c,mosaico1,color)
crd2 = d.getCrd(f,c,mosaico2,color)
rutas = d.getRutas(priSec.get(0),priSec.get(1),crd1,crd2)
lenRutas = d.cantOpt(priSec.get(0) * priSec.get(1),rutas)
rutas = d.optRutas(priSec.get(0) * priSec.get(1),rutas)
rutas = d.crearCaminos(mosaico1,lenRutas,rutas,priSec.get(1),crd2,color)
lenRutas = d.optCmns(mosaico1,priSec.get(1),crd2,color)
intercambios = d.getMovT(f,c,lenRutas,rutas,mosaico1,mosaico2,color)
volteos = d.getVoltT(f,c,lenRutas,rutas,mosaico1,mosaico2,color)
minCost = d.minCost(intercambios,volteos,costInt,costVolt)
print('Costo Mínimo: Q',minCost)
print('Intercambios:',intercambios)
print('Volteos:',volteos,'\n')
print('Transición')
p.printMos(f,c,mosaico1)
d.transMos(f,c,lenRutas,rutas,mosaico1,mosaico2,color,costInt,costVolt)