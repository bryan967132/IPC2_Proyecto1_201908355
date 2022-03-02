class oFunc:
    def getMos(self,f,c,mosaico):
        mos = '\n'
        i = 0
        while i < f:
            mos += '   '
            j = 0
            while j < c:
                if mosaico.get(i,j) == 'B':
                    mos += '░░'
                else:
                    mos += '██'
                j += 1
            mos += '\n'
            i += 1
        mos += '\n'
        return mos
    
    def getMosA(self,f,c,mosaico):
        mos = '\n'
        i = 0
        while i < f:
            mos += '   '
            j = 0
            while j < c:
                if mosaico.get(i,j) == 'W':
                    mos += '░░'
                else:
                    mos += '██'
                j += 1
            mos += '\n'
            i += 1
        mos += '\n'
        return mos
    
    def printPar(self,pares):
        print('W','B')
        for i in range(2):
            print(pares.get(i,0),pares.get(i,1))
    
    def printCrd(self,f,color,crd):
        print('\n' + color,'Ubicados')
        for i in range(f):
            print(crd.get(i,0),',',crd.get(i,1))

    def printRutas(self,t,rutas):
        for i in range(t):
            if rutas.get(i,0) is not None:
                print(rutas.get(i,0),',',rutas.get(i,1),' -> ',rutas.get(i,2),',',rutas.get(i,3),' | PasoX: ',rutas.get(i,4),' | PasoY: ',rutas.get(i,5));
        print()