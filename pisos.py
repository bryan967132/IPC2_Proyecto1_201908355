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

    def ordenar(self):
        actual = self.primero
        while actual.siguiente:
            actual1 = actual
            while actual1.siguiente:
                if actual.piso_Artesanal.nombre > actual1.siguiente.piso_Artesanal.nombre:
                    tmp = actual.piso_Artesanal.nombre
                    actual.piso_Artesanal.nombre = actual1.siguiente.piso_Artesanal.nombre
                    actual1.siguiente.piso_Artesanal.nombre = tmp
                    tmp = actual.piso_Artesanal.filas
                    actual.piso_Artesanal.filas = actual1.siguiente.piso_Artesanal.filas
                    actual1.siguiente.piso_Artesanal.filas = tmp
                    tmp = actual.piso_Artesanal.columnas
                    actual.piso_Artesanal.columnas = actual1.siguiente.piso_Artesanal.columnas
                    actual1.siguiente.piso_Artesanal.columnas = tmp
                    tmp = actual.piso_Artesanal.cVolt
                    actual.piso_Artesanal.cVolt = actual1.siguiente.piso_Artesanal.cVolt
                    actual1.siguiente.piso_Artesanal.cVolt = tmp
                    tmp = actual.piso_Artesanal.cInt
                    actual.piso_Artesanal.cInt = actual1.siguiente.piso_Artesanal.cInt
                    actual1.siguiente.piso_Artesanal.cInt = tmp
                    tmp = actual.piso_Artesanal.patrones
                    actual.piso_Artesanal.patrones = actual1.siguiente.piso_Artesanal.patrones
                    actual1.siguiente.piso_Artesanal.patrones = tmp
                actual1 = actual1.siguiente
            actual = actual.siguiente

    def recorrer(self):
        actual = self.primero
        print()
        while actual is not None:
            print("Nombre: {:<15} Filas: {:<10} Columnas: {:<10} Costo por Volteo: Q {:<10} Costo por Intercambio: {:<10}".format(actual.piso_Artesanal.nombre,actual.piso_Artesanal.filas,actual.piso_Artesanal.columnas,actual.piso_Artesanal.cVolt,actual.piso_Artesanal.cInt))
            actual.piso_Artesanal.patrones.ordenar()
            actual.piso_Artesanal.patrones.recorrer(actual.piso_Artesanal.filas,actual.piso_Artesanal.columnas)
            actual = actual.siguiente
        print()

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
    
    def buscarPatronP(self,nombre,codigo):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.patrones.buscar(codigo)

    def buscarPatronS(self,nombre1,codigo1,nombre,codigo):
        if nombre == nombre1 and codigo == codigo1:
            print("El nombre y código del segundo son los mismos que el primero")
            return True
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.patrones.buscar(codigo)


    def getMos(self,nombre,codigo):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.patrones.getPatron(codigo)
    
    def getCostV(self,nombre):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.cVolt

    def getCostI(self,nombre):
        actual = self.primero
        while actual and actual.piso_Artesanal.nombre != nombre:
            actual = actual.siguiente
        return actual.piso_Artesanal.cInt