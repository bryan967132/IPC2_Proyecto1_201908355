class oFunc:
    def printMos(self,f,c,patron):
        mos = ""
        for i in range(f):
            for j in range(c):
                if patron.get(i,j) == 'B':
                    mos += "░░"
                else:
                    mos += "██"
            mos += "\n"
        print(mos)
    
    def printPar(self,pares):
        print('W','B')
        for i in range(2):
            print(pares.get(i,0),pares.get(i,1))