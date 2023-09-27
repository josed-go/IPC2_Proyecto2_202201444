from clases.dron import dron
from clases.altura import altura
from clases.contenido import contenido
from clases.sistema_drones import sistema_drones
from clases.instruccion import instruccion
from clases.mensaje import mensaje
from clases.movimiento import movimiento
from clases.mensaje_procesado import mensaje_procesado
from listas.lista_drones import lista_drones
from listas.lista_alturas import lista_alturas
from listas.lista_contenido import lista_contenido
from listas.lista_sistema_drones import lista_sistema_drones
from listas.lista_instruccion import lista_instruccion
from listas.lista_mensaje import lista_mensaje
from listas.lista_movimiento import lista_movimiento
from listas.lista_msg_procesado import lista_msg_procesado
import xml.etree.ElementTree as ET
import threading

class funciones_archivo:
    def __init__(self):
        self.lista_dron = lista_drones()
        self.lista_sistemas = lista_sistema_drones()
        self.lista_msg = lista_mensaje()
        self.lista_msg_procesado = lista_msg_procesado()

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
        self.procesar_mensajes()
        #self.generar_grafica_sistemas()

    def procesar_mensajes(self):
        for mensajes in self.lista_msg:
            mensaje = ""
            lista_movi = lista_movimiento()
            sistema = self.lista_sistemas.obtener_sistema(mensajes.sistema)
            for index, instru in enumerate(mensajes.instrucciones):
                tiempo = 0
                self.movimientos_dron(instru.instruccion, instru.dron, lista_movi, tiempo, index)
                alturas_dron = sistema.contenido.obtener_contenido(instru.dron)
                for alturas in alturas_dron.alturas:
                    if instru.instruccion == alturas.altura:
                        mensaje += alturas.valor

            for index, lista_instru in enumerate(mensajes.instrucciones):
                lista_movi.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)

            tiempo_optimo = lista_movi.obtener_mayor_tiempo()

            nuevo_ms_procesado = mensaje_procesado(mensajes.nombre_msg, mensaje, sistema.nombre, tiempo_optimo, lista_movi)
            self.lista_msg_procesado.agregar(nuevo_ms_procesado)

        # self.lista_msg_procesado.mostrar_lista()

    def formar_mensaje(self, nombre_msg):
        lista_movimientos = lista_movimiento()
        mensaje = ""
        msg = self.lista_msg.obtener_msg(nombre_msg)
        sistema = self.lista_sistemas.obtener_sistema(msg.sistema)

        for index, lista_instru in enumerate(msg.instrucciones):
            tiempo = 0
            self.movimientos_dron(lista_instru.instruccion, lista_instru.dron, lista_movimientos, tiempo, index)
            alturas_dron = sistema.contenido.obtener_contenido(lista_instru.dron)
            for alturas in alturas_dron.alturas:
                if lista_instru.instruccion == alturas.altura:
                    mensaje += alturas.valor
        #self.movimientos(msg.instrucciones, lista_movimientos)

        for index, lista_instru in enumerate(msg.instrucciones):
            lista_movimientos.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)

        tiempo_optimo = lista_movimientos.obtener_mayor_tiempo()
        
        return sistema.nombre, mensaje, tiempo_optimo
    
    # def movimientos(self, instrucciones, lista_mov):
    #     for instru in instrucciones:
    #         t = threading.Thread(target=self.movimientos_dron, args=(instru.instruccion, instru.dron, lista_mov))
    #         t.start()

    def graficar_movimientos(self, nombre_msg):
        lista_movimientos = lista_movimiento()
        lista_dron_temp = lista_drones()
        msg = self.lista_msg.obtener_msg(nombre_msg)
        sistema = self.lista_sistemas.obtener_sistema(msg.sistema)

        for index, lista_instru in enumerate(msg.instrucciones):
            tiempo = 0
            self.movimientos_dron(lista_instru.instruccion, lista_instru.dron, lista_movimientos, tiempo, index)
            if self.validar_dron_unico(lista_instru.dron, lista_dron_temp) == False:
                nuevo_dron = dron(lista_instru.dron)
                lista_dron_temp.agregar_unico(nuevo_dron)

        for index, lista_instru in enumerate(msg.instrucciones):
            lista_movimientos.completar_esperar(lista_instru.dron, lista_instru.instruccion, index)

        # print("Tiempo Max:", lista_movimientos.obtener_mayor_tiempo())

        # lista_dron_temp.mostrar_lista()

        # lista_movimientos.mostrar_lista()

        lista_movimientos.generar_grafica(sistema.cantidad,msg.nombre_msg, lista_dron_temp)
    
    def movimientos_dron(self, altura_, dron_, lista_movi, tiempo, num):
        tiempo_temp = tiempo
        altura_llegar = int(altura_)
        altura_temp = int(lista_movi.obtener_movimientos_dron(dron_))
        ultimo_tiempo = int(lista_movi.obtener_tiempo_dron(dron_))
        indice = int(lista_movi.obtener_indice_dron(dron_, num))
        if ultimo_tiempo > 0:
            tiempo_temp = ultimo_tiempo

        primer_num = int(lista_movi.obtener_numero_dron_primero(dron_))

        numero_ins = int(lista_movi.obtener_numero_dron(dron_))
        if numero_ins != 0:
            num = numero_ins
        # debe_esperar = lista_movi.obtener_tiempo(tiempo_temp)
        # debe_esperar2 = lista_movi.obtener_altura(altura_)
        # print("Dron:", dron_)
        # print(debe_esperar)

        # if debe_esperar and debe_esperar2:
        #     tiempo_temp += 1
        #     print(dron_, "Esperar", tiempo_temp)
        #     nuevo_movimiento = movimiento("Esperar", tiempo_temp, dron_, altura_)
        #     lista_movi.agregar(nuevo_movimiento)
            
        # else:

        if altura_temp < int(altura_):
            while altura_temp < altura_llegar:
                altura_temp += 1
                tiempo_temp += 1
                nuevo_movimiento = movimiento("Subir", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                #print(dron_, "subir", tiempo_temp)
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                #print(dron_, "Esperar", tiempo_temp)
                nuevo_movimiento = movimiento("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else :
                #print(dron_, "Emitir luz", tiempo_temp)
                nuevo_movimiento = movimiento("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
        elif altura_temp > int(altura_):
            while altura_temp > altura_llegar:
                tiempo_temp += 1
                #print(dron_, "bajar", tiempo_temp)
                nuevo_movimiento = movimiento("Bajar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                altura_temp -= 1
            
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                #print(dron_, "Esperar", tiempo_temp)
                nuevo_movimiento = movimiento("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else :
                #print(dron_, "Emitir luz", tiempo_temp)
                nuevo_movimiento = movimiento("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
        elif altura_temp == int(altura_):
            tiempo_temp += 1
            bandera = lista_movi.obtener_tiempo(tiempo_temp)
            if bandera:
                #print(dron_, "Esperar", tiempo_temp)
                nuevo_movimiento = movimiento("Esperar", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
                self.movimientos_dron(altura_, dron_, lista_movi, tiempo_temp, indice)
            else:
                #print(dron_, "Emitir luz", tiempo_temp)
                nuevo_movimiento = movimiento("Emitir luz", tiempo_temp, dron_, altura_, indice)
                lista_movi.agregar_ordenado(nuevo_movimiento)
    

    def validar_dron(self, dron):
        for drones in self.lista_dron:
            if dron == drones.nombre:
                return True
            
        return False
    
    def validar_dron_unico(self, dron, lista_dron):
        for drones in lista_dron:
            if dron == drones.nombre:
                return True
            
        return False
    
    def obtener_lista_drones(self):
        return self.lista_dron
    
    def obtener_lista_mensajes(self):
        return self.lista_msg
    
    def generar_xml(self):
        self.lista_msg_procesado.generar_xml(self.lista_msg)

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