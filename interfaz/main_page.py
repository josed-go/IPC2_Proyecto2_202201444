import tkinter as tk
import tkinter.font as font

from tkinter import filedialog, messagebox

from interfaz.ayuda import ayuda
from interfaz.gestion_drones import gestion_drones
from funciones.funciones_archivo import funciones_archivo

class main_page:

    def __init__(self, raiz):
        self.raiz = raiz

        self.funciones = funciones_archivo()

        self.raiz.config(bg="#D7EEF5")

        self.titulo = font.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        self.fuente = font.Font(family='Helvetica', size=15)

        self.raiz.title("Proyecto 2")
        self.raiz.resizable(0,0)

        self.archivo = ''
        

        self.menu = tk.Menu(self.raiz)

        """self.opciones_menu = tk.Menu(self.raiz, tearoff=0)
        self.opciones_menu.add_command(label="Abrir", command=self.mostrar_ayuda)
        self.opciones_menu.add_separator()
        self.opciones_menu.add_command(label="Salir", command=self.raiz.quit)

        self.menu.add_cascade(label="Archivo", menu=self.opciones_menu)
        self.menu.add_cascade(label="Archivo2")
        self.menu.add_cascade(label="Archivo3")

        self.raiz.config(menu=self.menu)"""

        self.label = tk.Label(self.raiz, text="Encriptador", font = self.titulo, bg="#c3e5f0")
        self.label.pack(side="top", fill="x", pady=10)

        self.button1 = tk.Button(self.raiz, text="Cargar archivo", highlightbackground='black', height= 2, width=25, padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb", command = self.cargar_archivo)
        self.buttonP = tk.Button(self.raiz, text="Procesar archivo", highlightbackground='black', height= 2, width=25 ,padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb", command = self.procesar_archivo)
        self.button2 = tk.Button(self.raiz, text="Generar archivo", highlightbackground='black', height= 2, width=25 ,padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb")
        self.button3 = tk.Button(self.raiz, text="Gestión de drones",highlightbackground='black', height= 2, width=25 ,padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb", command = self.gestion_drones)
        self.button4 = tk.Button(self.raiz, text="Gestión de sitemas de drones", highlightbackground='black', height=2, width=25 ,padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb")
        self.button7 = tk.Button(self.raiz, text="Gestión de mensajes", highlightbackground='black', height=2, width=25 ,padx=10, pady=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb")
        self.button5 = tk.Button(self.raiz, text="Ayuda", highlightbackground='black', height= 4, width=10, font = self.fuente, command = self.mostrar_ayuda, bg="#ebf7fa", activebackground="#aeddeb")
        self.button6 = tk.Button(self.raiz, text="Inicializar", highlightbackground='black', height= 4, width=10, font = self.fuente, bg="#ebf7fa", activebackground="#aeddeb")

        self.button1.pack()
        self.buttonP.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button7.pack()
        self.button5.pack(anchor="s", side="right")
        self.button6.pack(anchor="s", side="left")

    def center_window(self, window, ancho, alto):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2
        window.geometry(f"{ancho}x{alto}+{x}+{y}")

    def mostrar_ayuda(self):
        ventana = ayuda(self.raiz)
        self.center_window(ventana.ventana, 850, 450)

    def gestion_drones(self):
        lista_dron = self.funciones.obtener_lista_drones()
        ventana = gestion_drones(self.raiz, lista_dron, self.funciones)
        self.center_window(ventana.ventana_gestion, 1050, 650)

    def cargar_archivo(self):
        self.archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.xml")])
        if self.archivo:
            messagebox.showinfo("Exito!", "Archivo cargado correctamente.")
        else:
            messagebox.showerror("Error!", "Archivo no encontrado.")
        

    def procesar_archivo(self):
        if self.archivo:
            self.funciones.leer_xml(self.archivo)
        else:
            messagebox.showwarning("Error!", "Debes de cargar un archivo antes.")