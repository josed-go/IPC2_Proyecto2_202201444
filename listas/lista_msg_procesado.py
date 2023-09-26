from listas.nodo import nodo
import xml.etree.ElementTree as ET

class lista_msg_procesado:
    def __init__(self):
        self.primero = None
        self.size = 0

    def agregar(self, mensaje_procesado):
        nuevo_nodo = nodo(tipo_dato = mensaje_procesado)

        if self.size == 0:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
        
            actual = self.primero
            anterior = None
            while actual is not None and actual.tipo_dato.nombre_mensaje.lower() < nuevo_nodo.tipo_dato.nombre_mensaje.lower():
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
    
    def obtener_datos_msg(self, msg):
        actual = self.primero

        while actual != None:
            if actual.tipo_dato.nombre_mensaje == msg:
                return actual.tipo_dato
            actual = actual.siguiente
        
    def generar_xml(self , mensajes):
        data = ET.Element('respuesta')
        lista = ET.SubElement(data, 'listaMensajes')

        for msg in mensajes:
            msg_buscado = self.obtener_datos_msg(msg.nombre_msg)
            mensaje = ET.SubElement(lista, 'mensaje', nombre=f"{msg.nombre_msg}")

            sistema = ET.SubElement(mensaje, 'sistemaDrones')
            sistema.text = msg.sistema

            tiempo_optimo = ET.SubElement(sistema, 'tiempoOptimo')
            tiempo_optimo.text = str(msg_buscado.tiempo)

            mensaje_recibido = ET.SubElement(sistema, 'mensajeRecibido')
            mensaje.text = msg_buscado.mensaje

            instrucciones = ET.SubElement(sistema, 'instrucciones')

            for i in range(1,int(msg_buscado.tiempo)+1):
                tiempo = ET.SubElement(instrucciones, 'tiempo', valor=f"{i}")
                acciones = ET.SubElement(tiempo, 'acciones')
                for movi in msg_buscado.movimientos:

                    if int(movi.tiempo) == i:
                        dron = ET.SubElement(acciones, 'dron', nombre=f"{movi.dron}")
                        dron.text = movi.movimiento
            prueba = ET.tostring(data)

        self.prettify_xml(data)
        tree = ET.ElementTree(data)
        tree.write("archivo_salida.xml",encoding="UTF-8",xml_declaration=True)
        

    def prettify_xml(self,element, indent='    '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level+1) 
            if queue:
                element.tail = '\n' + indent * queue[0][0]  
            else:
                element.tail = '\n' + indent * (level-1)  
            queue[0:0] = children

    
    def mostrar_lista(self):
        print("TOTAL MENSAJES", self.size)
        print("")

        actual = self.primero
        while actual != None:
            print("Nombre:", actual.tipo_dato.nombre_mensaje, "| Sistema:", actual.tipo_dato.sistema, "| Mensaje:", actual.tipo_dato.mensaje)
            print("------- Instrucciones -------")
            actual.tipo_dato.movimientos.mostrar_lista()
            actual = actual.siguiente