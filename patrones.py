class piso_Patron:
    def __init__(self,codigo,patron):
        self.codigo = codigo
        self.patron = patron

class nodo:
    def __init__(self,piso_patron = None,siguiente = None):
        self.piso_patron = piso_patron
        self.siguiente = siguiente

class list_e_pat:
    def __init__(self):
        self.primero = None

    def insertar(self,patron):
        if self.primero is None:
            self.primero = nodo(piso_patron = patron)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(piso_patron = patron)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("\tCodigo:",actual.piso_patron.codigo)
            actual.piso_patron.patron.recorrer()
            actual = actual.siguiente

    def buscar(self,codigo):
        actual = self.primero
        while actual and actual.piso_patron.codigo != codigo:
            if actual.siguiente is None:
                print('El patrón no existe en el sistema')
                return True
            actual = actual.siguiente
        return False

    def getPatron(self,codigo):
        actual = self.primero
        while actual and actual.piso_patron.codigo != codigo:
            actual = actual.siguiente
        return actual.piso_patron.patron