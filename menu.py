from parseXML import parseXML
class menu:
    #imprimir con tabulación
    #print("Nombre: {:<15} Filas: {:<4} Columnas: {:<4}".format(actual.piso_Artesanal.nombre,actual.piso_Artesanal.filas,actual.piso_Artesanal.columnas))
    #print("Código: {}".format(actual.piso_patron.codigo))
    
    def menuP(self):
        opcion = 0
        while opcion != 3:
            try:
                self.opciones()
                opcion = int(input('Opción: '))
                if opcion == 1:
                    try:
                        ruta = input('Ingrese la ruta del archivo XML de entrada: ')
                        lista_piso = parseXML().getXML(ruta)
                    except:
                        print('\nEl XML no se encuentra en la ubicación especificada\n')
                elif opcion == 2:
                    if lista_piso is not None:
                        self.operaciones()
                    else:
                        print('\nNo se ha cargado información de los pisos\n')
                elif opcion == 3:
                    print('\n¡Finalizado!\n')
                else:
                    print('\nSolo números entre 1 y 5\n')
            except:
                print('\nOpción inválida\n')

        
    def opciones(self):
        print("""Menú Principal
        1. Cargar Archivos XML
        2. Operaciones Con Pisos
        3. Salir""")
    
    def operaciones(self,lista_piso):
        piso1 = input("Ingrese el nombre del primer piso: ")
        while lista_piso.buscarP(piso1):
            piso1 = input("Ingrese el nombre del piso: ")
        
        ptrn1 = input("Ingrese el código del patrón: ")
        while lista_piso.buscarPatron(piso1,ptrn1):
            ptrn1 = input("Ingrese el código del patrón: ")
        
        f = lista_piso.getF(piso1)
        c = lista_piso.getC(piso1)
        
        piso2 = input("Ingrese el nombre del segundo piso: ")
        while lista_piso.buscarS(f,c,piso2):
            piso2 = input("Ingrese el nombre del piso: ")
        
        ptrn2 = input("Ingrese el código del patrón: ")
        while lista_piso.buscarPatron(piso2,ptrn2):
            ptrn2 = input("Ingrese el código del patrón: ")
        
        patron1 = lista_piso.getMos(piso1,ptrn1)
        patron2 = lista_piso.getMos(piso2,ptrn2)
        
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