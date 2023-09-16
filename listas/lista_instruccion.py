from listas.nodo import nodo

class lista_instruccion:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, instruccion):
        nuevo_nodo = nodo(tipo_dato = instruccion)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
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
    
    def mostrar_lista(self):
        print("TOTAL INSTRUCCIONES", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Dron:", actual.tipo_dato.dron, "| Instruccion:", actual.tipo_dato.instruccion)
            actual = actual.siguiente