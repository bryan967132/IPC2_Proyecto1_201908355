class oFunc:
    def printMos(self,f,c,mosaico):
        mos = ""
        for i in range(f):
            for j in range(c):
                if mosaico.get(i,j) == 'B':
                    mos += "░░"
                else:
                    mos += "██"
            mos += "\n"
        print(mos)
    
    def printPar(self,pares):
        print('W','B')
        for i in range(2):
            print(pares.get(i,0),pares.get(i,1))
    
    def printCrd(self,f,color,crd):
        print('\n' + color,'Ubicados')
        for i in range(f):
            print(crd.get(i,0),',',crd.get(i,1))
