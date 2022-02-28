from oListas import cant1,cant2,listaCant1,listaCant2
class pFunc:
    def getCantCol(self,f,c,mosaico1,mosaico2):
        w1 = 0
        b1 = 0
        w2 = 0
        b2 = 0
        i = 0
        while i < f:
            j= 0
            while j < c:
                if mosaico1.get(i,j) == 'W':
                    w1 += 1
                else:
                    b1 += 1
                if mosaico2.get(i,j) == 'W':
                    w2 += 1
                else:
                    b2 += 1
                j += 1
            i += 1

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
        i = 0
        while i < f:
            j = 0
            while j < c:
                if mosaico.get(i,j) == color:
                    par1 = cant2(fila,0,i)
                    par2 = cant2(fila,1,j)
                    pares.insertar(par1)
                    pares.insertar(par2)
                    fila += 1
                j += 1
            i += 1
        return pares
    
    def getRutas(self,f1,f2,crd1,crd2):
        rutas = listaCant2()
        ruta = 0
        i = 0
        while i < f1:
            x = 0
            while x < f2:
                crd1i0 = cant2(ruta,0,crd1.get(i,0));crd1i1 = cant2(ruta,1,crd1.get(i,1))
                crd2x0 = cant2(ruta,2,crd2.get(x,0));crd2x1 = cant2(ruta,3,crd2.get(x,1))
                dV = cant2(ruta,4,crd2.get(x,1) - crd1.get(i,1));
                dH = cant2(ruta,5,crd2.get(x,0) - crd1.get(i,0));
                rutas.insertar(crd1i0)
                rutas.insertar(crd1i1)
                rutas.insertar(crd2x0)
                rutas.insertar(crd2x1)
                rutas.insertar(dV)
                rutas.insertar(dH)
                ruta += 1
                x += 1
            i += 1
        return rutas

    def cantNoMover(self,t,rutas):
        cant = 0
        i = 0
        while i < t:
            if abs(rutas.get(i,4)) + abs(rutas.get(i,5)) == 0:
                cant += 1
            i += 1
        return cant

    def getNoMover(self,t,rutas):
        preOpt = listaCant2()
        cant = 0
        i = 0
        while i < t:
            if abs(rutas.get(i,4)) + abs(rutas.get(i,5)) == 0:
                rutasi0 = cant2(cant,0,rutas.get(i,0))
                rutasi1 = cant2(cant,1,rutas.get(i,1))
                preOpt.insertar(rutasi0)
                preOpt.insertar(rutasi1)
                cant += 1
            i += 1
        return preOpt

    def cantDescart(self,lenPreOpt,t,preOpt,rutas):
        cant = 0
        i = 0
        while i < lenPreOpt:
            x = 0
            while x < t:
                if (preOpt.get(i,0) == rutas.get(x,0) and preOpt.get(i,1) == rutas.get(x,1)) or (preOpt.get(i,0) == rutas.get(x,2) and preOpt.get(i,1) == rutas.get(x,3)):
                    cant += 1
                x += 1
            i += 1
        return cant

    def getDescart(self,lenPreOpt,t,preOpt,rutas):
        rep = listaCant2()
        cant = 0
        i = 0
        while i < lenPreOpt:
            x = 0
            while x < t:
                if (preOpt.get(i,0) == rutas.get(x,0) and preOpt.get(i,1) == rutas.get(x,1)) or (preOpt.get(i,0) == rutas.get(x,2) and preOpt.get(i,1) == rutas.get(x,3)):
                    rutasx0 = cant2(cant,0,rutas.get(x,0));rutasx1 = cant2(cant,1,rutas.get(x,1))
                    rutasx2 = cant2(cant,2,rutas.get(x,2));rutasx3 = cant2(cant,3,rutas.get(x,3))
                    rutasx4 = cant2(cant,4,rutas.get(x,4));rutasx5 = cant2(cant,5,rutas.get(x,5))
                    rep.insertar(rutasx0);rep.insertar(rutasx1);rep.insertar(rutasx2)
                    rep.insertar(rutasx3);rep.insertar(rutasx4);rep.insertar(rutasx5)
                    cant += 1
                x += 1
            i += 1
        return rep

    def cantOptIn(self,t,lenRep,rutas,rep):
        cant = 0
        i = 0
        while i < t:
            if self.insertar(lenRep,rep,rutas.get(i,0),rutas.get(i,1),rutas.get(i,2),rutas.get(i,3),rutas.get(i,4),rutas.get(i,5)):
                cant += 1
            i += 1
        return cant

    def insertar(self,lenRep,rep,ruta0,ruta1,ruta2,ruta3,ruta4,ruta5):
        i = 0
        while i < lenRep:
            if rep.get(i,0) == ruta0 and rep.get(i,1) == ruta1 and rep.get(i,2) == ruta2 and rep.get(i,3) == ruta3 and rep.get(i,4) == ruta4 and rep.get(i,5) == ruta5:
                return False
            i += 1
        return True
    
    def getOpt(self,t,lenRep,rutas,rep):
        opt = listaCant2()
        cant = 0
        i = 0
        while i < t:
            if self.insertar(lenRep,rep,rutas.get(i,0),rutas.get(i,1),rutas.get(i,2),rutas.get(i,3),rutas.get(i,4),rutas.get(i,5)):
                rutasi0 = cant2(cant,0,rutas.get(i,0));rutasi1 = cant2(cant,1,rutas.get(i,1))
                rutasi2 = cant2(cant,2,rutas.get(i,2));rutasi3 = cant2(cant,3,rutas.get(i,3))
                rutasi4 = cant2(cant,4,rutas.get(i,4));rutasi5 = cant2(cant,5,rutas.get(i,5))
                opt.insertar(rutasi0);opt.insertar(rutasi1);opt.insertar(rutasi2)
                opt.insertar(rutasi3);opt.insertar(rutasi4);opt.insertar(rutasi5)
                cant += 1
            i += 1
        return opt
    
    def cantOpt(self,t,rutas):
        lenPreOpt = self.cantNoMover(t,rutas)
        if lenPreOpt > 0:
            preOpt = self.getNoMover(t,rutas)
            lenRep = self.cantDescart(lenPreOpt,t,preOpt,rutas)
            rep = self.getDescart(lenRep,t,preOpt,rutas)
            cantOpt = self.cantOptIn(t,lenRep,rutas,rep)
            return cantOpt
        else:
            return t

    def optRutas(self,t,rutas):
        lenPreOpt = self.cantNoMover(t,rutas)
        if lenPreOpt > 0:
            preOpt = self.getNoMover(t,rutas)
            lenRep = self.cantDescart(lenPreOpt,t,preOpt,rutas)
            rep = self.getDescart(lenRep,t,preOpt,rutas)
            opt = self.getOpt(t,lenRep,rutas,rep)
            return opt
        else:
            return rutas
    
    def cantFalts(self,mosaico1,lencrd2,crd2,color):
        cant = 0
        i = 0
        while i < lencrd2:
            if mosaico1.get(crd2.get(i,0),crd2.get(i,1)) is not color:
                cant += 1
        return cant
    
    def crearCaminos(self,f,c,mosaico1,lenRutas,rutas,lencrd2,crd2,color):
        lenFalts = self.cantFalts(mosaico1,lencrd2,crd2,color)
        print(lenFalts)
        #falts = self.getFalts()