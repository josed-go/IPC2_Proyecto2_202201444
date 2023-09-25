from clases.dron import dron
from clases.altura import altura
from clases.contenido import contenido
from clases.sistema_drones import sistema_drones
from clases.instruccion import instruccion
from clases.mensaje import mensaje
from clases.movimiento import movimiento
from listas.lista_drones import lista_drones
from listas.lista_alturas import lista_alturas
from listas.lista_contenido import lista_contenido
from listas.lista_sistema_drones import lista_sistema_drones
from listas.lista_instruccion import lista_instruccion
from listas.lista_mensaje import lista_mensaje
from listas.lista_movimiento import lista_movimiento
import xml.etree.ElementTree as ET

class funciones_archivo:
    def __init__(self):
        self.lista_dron = lista_drones()
        self.lista_sistemas = lista_sistema_drones()
        self.lista_msg = lista_mensaje()

    def leer_xml(self,archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()

        for drones in root.findall("./listaDrones/dron"):
            #print(drones.text)
            nuevo_dron = dron(drones.text)
            self.lista_dron.agregar(nuevo_dron)
        
        self.lista_dron.mostrar_lista()

        for sistema in root.findall("./listaSistemasDrones/sistemaDrones"):
            #print("Nombre sistema:", sistema.get("nombre"))
            nombre = sistema.get("nombre")
            alturamax = sistema.find("alturaMaxima")
            cantidadDrones = sistema.find("cantidadDrones")

            #print("Altura maxima:",alturamax.text, "| Cantidad Drones:", cantidadDrones.text)

            lista_contenido_temp = lista_contenido()
            lista_alturas_graf = lista_alturas()

            cont = 1
            for contenidos in sistema.findall("contenido"):
                dron_contenido = contenidos.find("dron")

                lista_alturas_temp = lista_alturas()

                #print("Dron:", dron_contenido.text+"\n")
                #print("Alturas:")
                if self.validar_dron(dron_contenido.text):
                    for alturas_dron in contenidos.findall("./alturas/altura"):
                        #print("Altura:",alturas_dron.get("valor"), "| Letra:", alturas_dron.text)
                        altura_nueva = altura(alturas_dron.get("valor"), alturas_dron.text, dron_contenido.text, cont)
                        lista_alturas_graf.agregar_ordenado(altura_nueva)
                        lista_alturas_temp.agregar(altura_nueva)

                    #lista_alturas_temp.mostrar_lista()
                

                    cont += 1
                    contenido_nuevo = contenido(dron_contenido.text, lista_alturas_temp)

                    lista_contenido_temp.agregar(contenido_nuevo)
                else :
                    print(dron_contenido.text, "no esta definido en la lista drones\n")

            nuevo_sistema = sistema_drones(nombre, alturamax.text, cantidadDrones.text, lista_contenido_temp, lista_alturas_graf)
            self.lista_sistemas.agregar(nuevo_sistema)
            
            #lista_contenido_temp.mostrar_lista()

        self.lista_sistemas.mostrar_lista()

        for mensajes in root.findall("./listaMensajes/Mensaje"):
            #print("\nNombre mensaje:",mensajes.get("nombre"))

            sistema_mensaje = mensajes.find("sistemaDrones")
            #print("\nMensaje del sistema:", sistema_mensaje.text)

            lista_instruc_temp = lista_instruccion()

            for instrucciones in mensajes.findall("./instrucciones/instruccion"):
                #print("Intruccion dron:", instrucciones.get("dron"), "| Instruccion:", instrucciones.text)
                nueva_instru = instruccion(instrucciones.get("dron"), instrucciones.text)
                lista_instruc_temp.agregar(nueva_instru)
            
            #lista_instruc_temp.mostrar_lista()

            nuevo_msg = mensaje(mensajes.get("nombre"), sistema_mensaje.text, lista_instruc_temp)
            self.lista_msg.agregar(nuevo_msg)

        self.lista_msg.mostrar_lista()
        #self.generar_grafica_sistemas()

    def formar_mensaje(self, nombre_msg):
        lista_movimientos = lista_movimiento()
        mensaje = ""
        msg = self.lista_msg.obtener_msg(nombre_msg)

        sistema = self.lista_sistemas.obtener_sistema(msg.sistema)

        lista_movimientos.agregar(msg, sistema)

        for lista_instru in msg.instrucciones:
            alturas_dron = sistema.contenido.obtener_contenido(lista_instru.dron)
            for alturas in alturas_dron.alturas:
                if lista_instru.instruccion == alturas.altura:
                    mensaje += alturas.valor

        return sistema.nombre, mensaje

    def validar_dron(self, dron):
        for drones in self.lista_dron:
            if dron == drones.nombre:
                return True
            
        return False
    
    def obtener_lista_drones(self):
        return self.lista_dron
    
    def obtener_lista_mensajes(self):
        return self.lista_msg
    
    def obtener_lista_instrucciones_por_mensaje(self, msg):
        for lista in self.lista_msg:
            if lista.nombre_msg == msg:
                return lista
            
        return None
    
    def agregar_nuevo_dron(self, dron_nuevo):

        if self.validar_dron(dron_nuevo):
            return False
        else :
            nuevo_dron = dron(dron_nuevo)
            self.lista_dron.agregar(nuevo_dron)
            return True
        
    def generar_grafica_sistemas(self):
        self.lista_sistemas.graficar()

    def inicializar_sistema(self):
        self.lista_dron.limpiar_datos()
        self.lista_sistemas.limpiar_datos()
        self.lista_msg.limpiar_datos()