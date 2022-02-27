class piso_Artesanal:
    def __init__(self,nombre,filas,columnas,cVolt,cInt,patrones):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.cVolt = cVolt
        self.cInt = cInt
        self.patrones = patrones

class nodo:
    def __init__(self,piso_Artesanal = None,siguiente = None):
        self.piso_Artesanal = piso_Artesanal
        self.siguiente = siguiente

class list_e_pis:
    def __init__(self):
        self.primero = None

    def insertar(self,piso):
        if self.primero is None:
            self.primero = nodo(piso_Artesanal = piso)
            return
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nodo(piso_Artesanal = piso)

    def recorrer(self):
        actual = self.primero
        while actual is not None:
            print("Nombre:",actual.piso_Artesanal.nombre,
                "Filas:",actual.piso_Artesanal.filas,
                "Columnas:",actual.piso_Artesanal.columnas,
                "Costo por voltear:",actual.piso_Artesanal.cVolt,
                "Costo por intercambiar:",actual.piso_Artesanal.cInt)
            actual.piso_Artesanal.patrones.recorrer()            
            print()
            actual = actual.siguiente

    def getF(self,nombre):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.filas
    
    def getC(self,nombre):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.columnas

    def buscarP(self,nombre):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            if actual.siguiente is None:
                print("El piso no existe en el sistema")
                return True
            actual = actual.siguiente
        return False
    
    def buscarS(self,filas,columnas,nomS):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nomS:
            if actual.siguiente is None:
                print("El piso no existe en el sistema")
                return True
            actual = actual.siguiente
            
        if actual.piso_Artesanal.filas == filas and actual.piso_Artesanal.columnas == columnas:
            return False
        print("El piso no tiene las mismas dimensiones que el primero")
        return True
    
    def buscarPatron(self,nombre,codigo):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.patrones.buscar(codigo)


    def getMos(self,nombre,codigo):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.patrones.getPatron(codigo)