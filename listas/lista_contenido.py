from listas.nodo import nodo

class lista_contenido:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, contenido):
        nuevo_nodo = nodo(tipo_dato = contenido)

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
    
    def graficar(self):
        texto = """<TR>\n<TD border="1" bgcolor="white">Altura (mts)</TD>"""

        actual = self.primero

        while actual != None:
            texto += f"""<TD border="1" bgcolor="white">{actual.tipo_dato.dron}</TD>\n"""
            actual = actual.siguiente
        texto += "</TR>"
        
        return texto

    def obtener_grafica_altura(self, altura):
        contador = 1
        datos = ""
        actual = self.primero

        for i in range(1,int(altura)+1):
            datos += f"""<TR>\n<TD border="1" bgcolor="white">{i}</TD>\n"""

            while actual != None and contador <= int(altura):
                datos += actual.tipo_dato.alturas.graficar()
                actual = actual.siguiente
            
            datos += "</TR>"
        
        return datos
    
    def mostrar_lista(self):
        print("TOTAL CONTENIDOS:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Dron:", actual.tipo_dato.dron)
            print("------ Alturas ------")
            actual.tipo_dato.alturas.mostrar_lista()
            actual = actual.siguiente