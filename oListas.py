class cant2:
    def __init__(self,i,j,cantC):
        self.i = i
        self.j = j
        self.cantC = cantC

class nodo:
    def __init__(self,objeto = None,siguiente = None):
        self.objeto = objeto
        self.siguiente = siguiente

class listaCant:
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
    
    def get(self,i,j):
        actual = self.primero
        while actual:
            if actual.objeto.i == i and actual.objeto.j == j:
                return actual.objeto.cantC
            if actual.siguiente is None:
                return
            actual = actual.siguiente
