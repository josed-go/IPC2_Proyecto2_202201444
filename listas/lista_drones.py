from listas.nodo import nodo

class lista_drones:

    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, dron):
        nuevo_nodo = nodo(tipo_dato = dron)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
        
            actual = self.primero
            anterior = None
            while actual is not None and actual.tipo_dato.nombre < nuevo_nodo.tipo_dato.nombre:
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

        self.size += 1

    def agregar_unico(self, dron):
        nuevo_nodo = nodo(tipo_dato = dron)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
        
            actual = self.primero
            anterior = None
            while actual is not None and actual.tipo_dato.nombre != nuevo_nodo.tipo_dato.nombre:
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo
        self.size += 1

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is not None:
            valor_actual = self.actual.tipo_dato
            self.actual = self.actual.siguiente
            return valor_actual
        else:
            raise StopIteration
        
    def obtener_size(self):
        return self.size
    
    def limpiar_datos(self):
        while self.primero != None:
            actual = self.primero
            self.primero = self.primero.siguiente
            del actual
        self.size = 0
        print("-> Lista drones eliminada...")
    
    def mostrar_lista(self):
        print("TOTAL DRONES:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Dron:", actual.tipo_dato.nombre)
            actual = actual.siguiente