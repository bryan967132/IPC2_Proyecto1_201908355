import io
import webbrowser
from parsePDF import pdfExport
from parseXML import parseXML
from graficar import graficar
from princF import pFunc
class menu:
    def menuP(self):
        lista_piso = None
        opcion = 0
        print()
        while opcion != 4:
            try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    try:
                        ruta = input('\nIngrese la ruta del archivo XML de entrada: ')
                        lista_piso = parseXML().getXML(ruta)
                        print('Información cargada\n')
                    except:
                        print('El XML no se encuentra en la ubicación especificada\n')
                elif opcion == 2:
                    if lista_piso:
                        lista_piso.ordenar()
                        lista_piso.recorrer()
                    else:
                        print('\nNo se ha cargado información de los pisos\n')
                elif opcion == 3:
                    if lista_piso:
                        self.operaciones(lista_piso)
                    else:
                        print('\nNo se ha cargado información de los pisos\n')
                elif opcion == 4:
                    print('\n¡Finalizado!')
                else:
                    print('\nSolo números entre 1 y 5\n')
            except:
                print('\nOpción inválida\n')

        
    def opciones(self):
        print("""Menú Principal
1. Cargar Archivos XML
2. Ver Pisos Y Patrones
3. Operaciones Con Pisos
4. Salir""")
    
    def operaciones(self,lista_piso):
        g = graficar()
        piso1 = input("\nIngrese el nombre del primer piso: ")
        while lista_piso.buscarP(piso1):
            piso1 = input("Ingrese el nombre del primer piso: ")
        ptrn1 = input("Ingrese el código del patrón: ")
        while lista_piso.buscarPatronP(piso1,ptrn1):
            ptrn1 = input("Ingrese el código del patrón: ")
        f = lista_piso.getF(piso1)
        c = lista_piso.getC(piso1)
        mosaico1 = lista_piso.getMos(piso1,ptrn1)
        mdot1 = g.dibujar(f,c,mosaico1)
        mdot1 = g.getDot(mdot1,'')
        g.exportPDF('mosaico0',mdot1)
        g.exportPNG(0,mdot1)
        print()
        piso2 = input("Ingrese el nombre del segundo piso: ")
        while lista_piso.buscarS(f,c,piso2):
            piso2 = input("Ingrese el nombre del segundo piso: ")
        ptrn2 = input("Ingrese el código del patrón: ")
        while lista_piso.buscarPatronS(piso1,ptrn1,piso2,ptrn2):
            ptrn2 = input("Ingrese el código del patrón: ")
        print()
        mosaico2 = lista_piso.getMos(piso2,ptrn2)
        costInt = lista_piso.getCostI(piso1)
        costVolt = lista_piso.getCostV(piso1)
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
        d.transMos(f,c,lenRutas,rutas,mosaico1,mosaico2,color,costInt,costVolt)
        intercambios = d.getIntercambios()
        volteos = d.getVolteos()
        minCost = d.minCost()
        print('Costo Mínimo: Q',minCost)
        print('Intercambios:',intercambios)
        print('Volteos:',volteos,'\n')
        self.menuInstrucciones(f,c,d)
        g.parsePDF('mosaico' + str(intercambios + volteos))
    
    def menuInstrucciones(self,fil,col,d):
        opcion = 0
        while True:
            try:
                print("""Ver Instrucciones
1. Ver En Consola
2. Exportar En Archivo .txt
3. Exportar En Archivo .pdf""")
                opcion = int(input('Opción: '))
                if opcion == 1:
                    print('\n' + d.getInstConsola() + '\n')
                    break
                elif opcion == 2:
                    with io.open("Instrucciones.txt","w",encoding="utf-8") as f:
                        f.write(d.getInstArchivo())
                    webbrowser.open("Instrucciones.txt")
                    print('\nInstrucciones Exportadas\n')
                    break
                elif opcion == 3:
                    pdfExport().exportarPDF(fil,col,d.getIntercambios() + d.getVolteos(),d.getListaInst())
                    print('\nInstrucciones Exportadas\n')
                    break
            except:
                print('\nOpción Inválida\n')