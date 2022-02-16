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
            
            actual = actual.siguiente