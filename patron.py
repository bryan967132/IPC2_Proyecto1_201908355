class patron_C:
    def __init__(self,y,x,color):
        self.i = y
        self.j = x
        self.color = color

class nodo:
    def __init__(self,patron_C = None,siguiente = None):
        self.patron_C = patron_C
        self.siguiente = siguiente

class list_e_pc:
    def __init__(self):
        self.primero = None

    def insertar(self,color):
        if self.primero is None:
            self.primero = nodo(patron_C = color)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(patron_C = color)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("\t\tColor:",actual.patron_C.color,
                "(",actual.patron_C.i,",",actual.patron_C.j,")")
            actual = actual.siguiente

    def get(self,i,j):
        actual = self.primero
        while actual:
            if actual.patron_C.i == i and actual.patron_C.j == j:
                return actual.patron_C.color
            if actual.siguiente is None:
                return
            actual = actual.siguiente