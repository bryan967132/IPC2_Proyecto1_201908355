class oFunc:
    def printMos(self,f,c,mosaico):
        mos = ''
        for i in range(f):
            for j in range(c):
                if mosaico.get(i,j) == 'B':
                    mos += '░░'
                else:
                    mos += '██'
            mos += '\n'
        print(mos)
    
    def printPar(self,pares):
        print('W','B')
        for i in range(2):
            print(pares.get(i,0),pares.get(i,1))
    
    def printCrd(self,f,color,crd):
        print('\n' + color,'Ubicados')
        for i in range(f):
            print(crd.get(i,0),',',crd.get(i,1))

    def printRutas(self,t,rutas):
        print()
        for i in range(t):
            print(rutas.get(i,0),',',rutas.get(i,1),' -> ',rutas.get(i,2),',',rutas.get(i,3),' | PasoX: ',rutas.get(i,4),' | PasoY: ',rutas.get(i,5));
        print()