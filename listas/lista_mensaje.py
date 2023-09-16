from listas.nodo import nodo

class lista_mensaje:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, mensaje):
        nuevo_nodo = nodo(tipo_dato = mensaje)

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
        print("TOTAL MENSAJES", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Nombre:", actual.tipo_dato.nombre_msg, "| Sistema:", actual.tipo_dato.sistema)
            print("------- Instrucciones -------")
            actual.tipo_dato.instrucciones.mostrar_lista()
            actual = actual.siguiente