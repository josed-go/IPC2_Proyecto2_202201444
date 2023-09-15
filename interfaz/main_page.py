import tkinter as tk
import tkinter.font as font

from interfaz.ayuda import ayuda

class main_page:

    def __init__(self, raiz):
        self.raiz = raiz

        self.titulo = font.Font(family='Helvetica', size=25, weight="bold", slant="italic")
        self.fuente = font.Font(family='Helvetica', size=15)

        self.raiz.title("Proyecto 2")
        self.raiz.resizable(0,0)

        

        self.menu = tk.Menu(self.raiz)

        """self.opciones_menu = tk.Menu(self.raiz, tearoff=0)
        self.opciones_menu.add_command(label="Abrir", command=self.mostrar_ayuda)
        self.opciones_menu.add_separator()
        self.opciones_menu.add_command(label="Salir", command=self.raiz.quit)

        self.menu.add_cascade(label="Archivo", menu=self.opciones_menu)
        self.menu.add_cascade(label="Archivo2")
        self.menu.add_cascade(label="Archivo3")

        self.raiz.config(menu=self.menu)"""

        self.label = tk.Label(self.raiz, text="Encriptador", font = self.titulo)
        self.label.pack(side="top", fill="x", pady=10)

        self.button1 = tk.Button(self.raiz, text="Cargar archivo", highlightbackground='black', height= 2, width=25, padx=10, pady=10, font = self.fuente)
        self.button2 = tk.Button(self.raiz, text="Generar archivo", highlightbackground='black', height= 2, width=25 ,padx=10, pady=10, font = self.fuente)
        self.button3 = tk.Button(self.raiz, text="Gestión de drones",highlightbackground='black', height= 2, width=25 ,padx=10, pady=10, font = self.fuente)
        self.button4 = tk.Button(self.raiz, text="Gestión de sitemas de drones", highlightbackground='black', height=2, width=25 ,padx=10, pady=10, font = self.fuente)
        self.button7 = tk.Button(self.raiz, text="Gestión de mensajes", highlightbackground='black', height=2, width=25 ,padx=10, pady=10, font = self.fuente)
        self.button5 = tk.Button(self.raiz, text="Ayuda", highlightbackground='black', height= 5, width=10, font = self.fuente, command = self.mostrar_ayuda)
        self.button6 = tk.Button(self.raiz, text="Inicializar", highlightbackground='black', height= 5, width=10, font = self.fuente)

        self.button1.pack()
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