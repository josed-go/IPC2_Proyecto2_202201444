from listas.nodo import nodo

class lista_movimiento:

    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, movimiento):
        nuevo_nodo = nodo(tipo_dato = movimiento)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
        self.size += 1

    def formar_movimientos(self, msg, sistema):

        altura_actual = 0

        altura_max = int(sistema.altura_max)

        # for altura in range(1, altura_max+1):
        #     for lista_instru in msg.instrucciones:
        #         #alturas_dron = sistema.contenido.obtener_contenido(lista_instru.dron)
        #         if int(lista_instru.instruccion) >= altura:
        #             print("dron",lista_instru.dron ,"- subir")


        for lista_instru in msg.instrucciones:
            alturas_dron = sistema.contenido.obtener_contenido(lista_instru.dron)
            altura_instruccion = int(lista_instru.instruccion)
            ultima_altura = self.obtener_movimientos_dron(lista_instru.dron)
            
            if altura_actual <= altura_instruccion:
                pass

    def obtener_movimientos_dron(self, dron_buscado):
        actual = self.primero

        movimiento = 0

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                movimiento = actual.tipo_dato.altura
            actual = actual.siguiente

        return movimiento
    
    def obtener_tiempo_dron(self, dron_buscado):
        actual = self.primero

        tiempo = 0

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                tiempo = actual.tipo_dato.tiempo
            actual = actual.siguiente

        return tiempo
    
    def obtener_altura(self, altura):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.altura == altura:
                return True
            actual = actual.siguiente

        return False
    
    def obtener_tiempo(self, tiempo):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.tiempo == tiempo and actual.tipo_dato.movimiento == "Emitir luz":
                return True
            actual = actual.siguiente

        return False

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
    
    def obtener_mayor_tiempo(self):
        if not self.primero:
            return None
        
        actual = self.primero

        tiempo_max = actual.tipo_dato.tiempo
        while actual != None:
            if actual.tipo_dato.tiempo > tiempo_max:
                tiempo_max = actual.tipo_dato.tiempo
            actual = actual.siguiente
        
        return tiempo_max
    
    def mostrar_lista(self):
        print("TOTAL MOVIMIENTOS:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Tiempo:", actual.tipo_dato.tiempo, "| MOVIMIENTO:", actual.tipo_dato.movimiento, "| Dron:", actual.tipo_dato.dron)
            actual = actual.siguiente