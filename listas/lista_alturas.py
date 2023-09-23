from listas.nodo import nodo

class lista_alturas:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, altura):
        nuevo_nodo = nodo(tipo_dato = altura)

        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return
        
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente

        actual.siguiente = nuevo_nodo
        self.size += 1

    def agregar_ordenado(self, altura):
        nuevo_nodo = nodo(tipo_dato = altura)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.tipo_dato.altura) < int(nuevo_nodo.tipo_dato.altura) or (int(actual.tipo_dato.altura) == int(nuevo_nodo.tipo_dato.altura) and int(actual.tipo_dato.num_contenido) < int(nuevo_nodo.tipo_dato.num_contenido))):
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
    
    def graficar(self):
        texto = ""
        actual = self.primero
        sentinela = actual.tipo_dato.altura
        texto = f"""<TR>\n<TD border="1" bgcolor="white">{actual.tipo_dato.altura}</TD>\n"""
        fila = False
        while actual != None:
            if int(sentinela) != int(actual.tipo_dato.altura):
                sentinela = actual.tipo_dato.altura
                fila = False
                texto += f"""</TR>\n<TR>\n<TD border="1" bgcolor="white">{actual.tipo_dato.altura}</TD>\n"""
            if fila == False:
                fila = True
                texto += f"""<TD border="1" bgcolor="white">{actual.tipo_dato.valor}</TD>\n"""
            else:
                texto += f"""<TD border="1" bgcolor="white">{actual.tipo_dato.valor}</TD>\n"""

            actual = actual.siguiente
        texto += "</TR>\n"       
        return texto     
    
    def obtener_alturas(self, dron_buscado):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                return actual.tipo_dato
            actual = actual.siguiente

        return None
    
    def mostrar_lista(self):
        print("TOTAL ALTURAS", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Altura:", actual.tipo_dato.altura, "| Valor:", actual.tipo_dato.valor)
            actual = actual.siguiente