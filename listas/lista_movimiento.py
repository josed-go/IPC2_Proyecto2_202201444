from listas.nodo import nodo
from clases.movimiento import movimiento
import os

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

    def agregar_ordenado(self, movimiento):
        nuevo_nodo = nodo(tipo_dato = movimiento)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (int(actual.tipo_dato.tiempo) < int(nuevo_nodo.tipo_dato.tiempo) or (int(actual.tipo_dato.tiempo) == int(nuevo_nodo.tipo_dato.tiempo) and int(actual.tipo_dato.num_instruccion) < int(nuevo_nodo.tipo_dato.num_instruccion))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.primero
                self.primero = nuevo_nodo
            else:
                nuevo_nodo.siguiente = actual
                anterior.siguiente = nuevo_nodo

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
    
    def obtener_numero_dron(self, dron_buscado):
        actual = self.primero

        numero = 0

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                numero = actual.tipo_dato.num_instruccion
            actual = actual.siguiente

        return numero
    
    def obtener_numero_dron_primero(self, dron_buscado):
        actual = self.primero

        numero = 0

        while actual != None:
            if actual.tipo_dato.dron == dron_buscado:
                numero = actual.tipo_dato.num_instruccion
                return numero
            actual = actual.siguiente
        
        return 0
    
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
    
    def validar_posicion(self, tiempo, dron_buscado):
        actual = self.primero

        while actual:
            if actual.tipo_dato.tiempo == tiempo and actual.tipo_dato.dron == dron_buscado:
                return True
            actual = actual.siguiente

        return False
    
    def completar_esperar(self, dron_buscar, altura, num):
        tiempo = int(self.obtener_mayor_tiempo())

        for tiempos in range(1, tiempo+1):
            if self.validar_posicion(tiempos, dron_buscar) == False:
                nuevo_movimiento = movimiento("Esperar", tiempos, dron_buscar,altura, num)
                self.agregar_ordenado(nuevo_movimiento)

    def generar_grafica(self, cantidad, name_msg, drones):
        texto = """digraph G {
                    charset="UTF-8"

                    a1 [ shape="none" fontname="Helvetica" label=<

                        <TABLE border="0" cellspacing="0.5" cellpadding="10" bgcolor="white">\n"""
        
        texto += f"""<TR><TD colspan="{int(cantidad)+1}" border="1" bgcolor="#aeddeb">"""+name_msg+"""</TD></TR>\n"""
        
        texto += """<TR>\n<TD border="1" bgcolor="white">Tiempo (s)</TD>"""
        for dron in drones:
            texto += f"""<TD border="1" bgcolor="white">{dron.nombre}</TD>\n"""
        texto += "</TR>"
        texto += self.agregar_movimientos_grafica()

        texto += "</TABLE>>]\n}"

        f = open('bb.dot', 'w', encoding="utf-8")
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o GRAFICA_MENSAJE_{name_msg}.png')

    def agregar_movimientos_grafica(self):
        texto = ""

        actual = self.primero
        sentinela = actual.tipo_dato.tiempo
        texto = f"""<TR>\n<TD border="1" bgcolor="white">{actual.tipo_dato.tiempo}</TD>\n"""
        fila = False
        while actual != None:
            if int(sentinela) != int(actual.tipo_dato.tiempo):
                sentinela = actual.tipo_dato.tiempo
                fila = False
                texto += f"""</TR>\n<TR>\n<TD border="1" bgcolor="white">{actual.tipo_dato.tiempo}</TD>\n"""
            if fila == False:
                fila = True
                texto += f"""<TD border="1" bgcolor="white">{actual.tipo_dato.movimiento}</TD>\n"""
            else:
                texto += f"""<TD border="1" bgcolor="white">{actual.tipo_dato.movimiento}</TD>\n"""

            actual = actual.siguiente
        texto += "</TR>\n"       
        return texto     
    

    def mostrar_lista(self):
        print("TOTAL MOVIMIENTOS:", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Tiempo:", actual.tipo_dato.tiempo, "| MOVIMIENTO:", actual.tipo_dato.movimiento, "| Dron:", actual.tipo_dato.dron, "| No. In:", actual.tipo_dato.num_instruccion)
            actual = actual.siguiente