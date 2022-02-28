class cant1:
    def __init__(self,i,cantC):
        self.i = i
        self.cantC = cantC

class cant2:
    def __init__(self,i,j,cantC):
        self.i = i
        self.j = j
        self.cantC = cantC

class nodo:
    def __init__(self,objeto = None,siguiente = None):
        self.objeto = objeto
        self.siguiente = siguiente

class listaCant1:
    def __init__(self):
        self.primero = None

    def insertar(self,cants):
        if self.primero is None:
            self.primero = nodo(objeto = cants)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(objeto = cants)
    
    def get(self,i):
        actual = self.primero
        while actual:
            if actual.objeto.i == i:
                return actual.objeto.cantC
            if actual.siguiente is None:
                return
            actual = actual.siguiente

class listaCant2:
    def __init__(self):
        self.primero = None

    def insertar(self,cants):
        if self.primero is None:
            self.primero = nodo(objeto = cants)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(objeto = cants)
    
    def get(self,i):
        listaSimple = listaCant1()
        actual = self.primero
        while actual:
            if actual.objeto.i == i:
                p = cant1(actual.objeto.j,actual.objeto.cantC)
                listaSimple.insertar(p)
            if actual.siguiente is None:
                break
            actual = actual.siguiente
        return listaSimple
    
    def get(self,i,j):
        actual = self.primero
        while actual:
            if actual.objeto.i == i and actual.objeto.j == j:
                return actual.objeto.cantC
            if actual.siguiente is None:
                return
            actual = actual.siguiente

    def intercambiar(self,i0,j0,i1,j1):
        actual1 = self.primero
        primero = None
        while actual1:
            if actual1.objeto.i == i0 and actual1.objeto.j == j0:
                primero = actual1
                break
            actual1 = actual1.siguiente
        
        actual2 = self.primero
        segundo = None
        while actual2:
            if actual2.objeto.i == i1 and actual2.objeto.j == j1:
                segundo = actual2
                break
            actual2 = actual2.siguiente

        primero.objeto.i = i1
        primero.objeto.j = j1
        segundo.objeto.i = i0
        segundo.objeto.j = j0
    
    def descartar(self,i,j):
        actual = self.primero
        while actual:
            if actual.objeto.i == i and actual.objeto.j == j:
                actual.objeto.cantC = - 1
                break
            actual = actual.siguiente
    
    def voltear(self,i,j):
        actual = self.primero
        while actual:
            if actual.objeto.i == i and actual.objeto.j == j:
                if actual.objeto.cantC == 'B':
                    actual.objeto.cantC = 'W'
                else:
                    actual.objeto.cantC = 'B'
                break
            actual = actual.siguiente