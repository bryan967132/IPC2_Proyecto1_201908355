from oListas import listaCant,cant2
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

        p_par0 = cant2(0,0,w1)
        p_par1 = cant2(0,1,b1)
        s_par0 = cant2(1,0,w2)
        s_par1 = cant2(1,1,b2)

        pares = listaCant()
        pares.insertar(p_par0);pares.insertar(p_par1)
        pares.insertar(s_par0);pares.insertar(s_par1)
        return pares
    