from oListas import cant1,cant2,listaCant1,listaCant2
class pFunc:
    def getCantCol(self,f,c,mosaico1,mosaico2):
        w1 = 0
        b1 = 0
        w2 = 0
        b2 = 0
        for i in range(f):
            for j in range(c):
                if mosaico1.get(i,j) == 'W':
                    w1 += 1
                else:
                    b1 += 1
                if mosaico2.get(i,j) == 'W':
                    w2 += 1
                else:
                    b2 += 1

        p_par0 = cant2(0,0,w1);p_par1 = cant2(0,1,b1)
        s_par0 = cant2(1,0,w2);s_par1 = cant2(1,1,b2)

        pares = listaCant2()
        pares.insertar(p_par0);pares.insertar(p_par1)
        pares.insertar(s_par0);pares.insertar(s_par1)
        return pares
    
    def getMenorC(self,pares):
        if pares.get(0,0) < pares.get(0,1):
            return 'W'
        return 'B'
    
    def getPriSec(self,pares):
        pri = 0
        sec = 0
        if pares.get(0,0) < pares.get(0,1):
            pri = pares.get(0,0)
            sec = pares.get(1,0)
        else:
            pri = pares.get(0,1)
            sec = pares.get(1,1)
        
        primero = cant1(0,pri)
        segundo = cant1(1,sec)

        mayMen = listaCant1()
        mayMen.insertar(primero);mayMen.insertar(segundo)
        return mayMen

    def getCrd(self,f,c,mosaico,color):
        pares = listaCant2()
        fila = 0
        for i in range(f):
            for j in range(c):
                if mosaico.get(i,j) == color:
                    par1 = cant2(fila,0,i)
                    par2 = cant2(fila,1,j)
                    pares.insertar(par1)
                    pares.insertar(par2)
                    fila += 1
        return pares