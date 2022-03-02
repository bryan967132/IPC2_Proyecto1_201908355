import io
from graficar import graficar
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
d = pFunc()
#g = graficar()

#mdot1 = g.dibujar(f,c,mosaico1)
#mdot1 = g.getDot(mdot1,'')
#g.exportPDF('mosaico0',mdot1)
#g.exportPNG(0,mdot1)

print(p.getMos(f,c,mosaico1))
print(p.getMos(f,c,mosaico2))

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
d.transMos(f,c,lenRutas,rutas,mosaico1,mosaico2,color,costInt,costVolt)
intercambios = d.getIntercambios()
volteos = d.getVolteos()
minCost = d.minCost()
print('Costo Mínimo: Q',minCost)
print('Costo por Intercambiar:',costInt)
print('Costo por Voltear:',costVolt)
print('Intercambios:',intercambios)
print('Volteos:',volteos,'\n')

proConsola = d.getInstConsola()
#proArchivo = d.getInstArchivo()
print(proConsola+'\n')

#d.getInstArchivo()

#with io.open("Instrucciones.txt","w",encoding="utf-8") as f:
#    f.write(proArchivo)

#g.parsePDF('mosaico' + str(intercambios + volteos))