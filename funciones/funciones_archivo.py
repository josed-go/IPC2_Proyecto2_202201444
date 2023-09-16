from clases.dron import dron
from clases.altura import altura
from clases.contenido import contenido
from clases.sistema_drones import sistema_drones
from clases.instruccion import instruccion
from clases.mensaje import mensaje
from listas.lista_drones import lista_drones
from listas.lista_alturas import lista_alturas
from listas.lista_contenido import lista_contenido
from listas.lista_sistema_drones import lista_sistema_drones
from listas.lista_instruccion import lista_instruccion
from listas.lista_mensaje import lista_mensaje
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

            for contenidos in sistema.findall("contenido"):
                dron_contenido = contenidos.find("dron")

                lista_alturas_temp = lista_alturas()

                #print("Dron:", dron_contenido.text+"\n")
                #print("Alturas:")
                for alturas_dron in contenidos.findall("./alturas/altura"):
                    #print("Altura:",alturas_dron.get("valor"), "| Letra:", alturas_dron.text)
                    altura_nueva = altura(alturas_dron.get("valor"), alturas_dron.text)
                    lista_alturas_temp.agregar(altura_nueva)

                #lista_alturas_temp.mostrar_lista()

                contenido_nuevo = contenido(dron_contenido.text, lista_alturas_temp)

                lista_contenido_temp.agregar(contenido_nuevo)

            nuevo_sistema = sistema_drones(nombre, alturamax.text, cantidadDrones.text, lista_contenido_temp)

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