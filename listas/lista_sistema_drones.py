from listas.nodo import nodo
import os

class lista_sistema_drones:

    def __init__(self):
        self.primero = None
        self.size = 0
    
    def agregar(self, sistema_drones):
        nuevo_nodo = nodo(tipo_dato = sistema_drones)

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
        contador = 0
        texto = "digraph G {\n"

        actual = self.primero

        while actual != None:
            texto += f"""a{contador} [ shape="none" fontname="Helvetica" label=<\n
            <TABLE border="0" cellspacing="0.5" cellpadding="10" bgcolor="white">\n
                <TR><TD colspan="{int(actual.tipo_dato.cantidad)+1}" border="1" bgcolor="#aeddeb">{actual.tipo_dato.nombre}</TD></TR>\n"""
            texto += actual.tipo_dato.contenido.graficar()
            texto += actual.tipo_dato.lista_graf.graficar()
            texto += "</TABLE>>]\n"
            contador += 1
            actual = actual.siguiente
        texto += "}"

        f = open('bb.dot', 'w')
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o GRAFICA_SISTEMA.png')
        print("## GRAFICA GENERADA ##")
    
    def mostrar_lista(self):
        print("TOTAL SISTEMAS:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Nombre:", actual.tipo_dato.nombre, "| Altura maxima:", actual.tipo_dato.altura_max, "| Cantidad drones:", actual.tipo_dato.cantidad)
            print("------ Contenido ------")
            actual.tipo_dato.contenido.mostrar_lista()
            actual = actual.siguiente