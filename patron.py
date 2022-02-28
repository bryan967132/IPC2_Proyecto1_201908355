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

    def intercambiar(self,i1,j1,i2,j2):
        actual1 = self.primero
        primero = None
        while actual1:
            if actual1.patron_C.i == i1 and actual1.patron_C.j == j1:
                primero = actual1
                break
            actual1 = actual1.siguiente
        
        actual2 = self.primero
        segundo = None
        while actual2:
            if actual2.patron_C.i == i2 and actual2.patron_C.j == j2:
                segundo = actual2
                break
            actual2 = actual2.siguiente
        
        primero.patron_C.i = i2
        primero.patron_C.j = j2
        segundo.patron_C.i = i1
        segundo.patron_C.j = j1
    
    def voltear(self,i,j):
        actual = self.primero
        while actual:
            if actual.patron_C.i == i and actual.patron_C.j == j:
                if actual.patron_C.color == 'B':
                    actual.patron_C.color = 'W'
                else:
                    actual.patron_C.color = 'B'
                break
            actual = actual.siguiente