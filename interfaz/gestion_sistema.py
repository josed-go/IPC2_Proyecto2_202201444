import tkinter as tk
import tkinter.font as font

from tkinter import messagebox
import subprocess

class gestion_sistema:
    def __init__(self, raiz, funciones):
        self.raiz = raiz
        self.funciones = funciones

        self.ventana_gestion = tk.Toplevel(self.raiz, bg="#D7EEF5")
        self.ventana_gestion.resizable(0,0)
        #self.ventana_gestion.anchor("center")

        self.titulo = font.Font(family='Helvetica', size=25)
        self.fuente1 = font.Font(family='Helvetica', size=8)
        self.fuente2 = font.Font(family='Helvetica', size=15)
        self.fuente3 = font.Font(family='Helvetica', size=13)

        #self.fn = funciones_archivo()
        self.ventana_gestion.title("Gestión de sistema de drones")

        label = tk.Label( self.ventana_gestion, text="Gestión de sistema", font=self.titulo, bg="#D7EEF5")
        label.pack()

        self.button1 = tk.Button(self.ventana_gestion, text="Generar grafica", highlightbackground='black', height= 2, width=15, padx=6, pady=4, font = self.fuente3, bg="#ebf7fa", activebackground="#aeddeb", command = self.generar_grafica)

        self.button1.pack()

        self.button = tk.Button(self.ventana_gestion, text="Cerrar",
            highlightbackground='black', height= 2, width=10, command=self.ventana_gestion.destroy, font = self.fuente1, bg="#ebf7fa", activebackground="#aeddeb")
        self.button.pack(anchor="s", side="left")
        

    def generar_grafica(self):
        self.funciones.generar_grafica_sistemas()
        messagebox.showinfo("Exito", "Grafica generada con exito", parent = self.ventana_gestion)
        self.mostrar_imagen()

    def mostrar_imagen(self):
        # self.button2 = tk.Button(self.ventana_gestion, text="Generar grafica", highlightbackground='black', height= 2, width=15, padx=6, pady=6, font = self.fuente1, bg="#ebf7fa", activebackground="#aeddeb")

        # self.button2.grid(row=1, column=2)
        self.grafica = tk.PhotoImage(file="GRAFICA_SISTEMA.png")
        self.labelimg = tk.Label(self.ventana_gestion, image=self.grafica)
        self.labelimg.pack()

        self.button2 = tk.Button(self.ventana_gestion, text="Abrir grafica", highlightbackground='black', height= 2, width=15, padx=6, pady=6, font = self.fuente1, bg="#ebf7fa", activebackground="#aeddeb", command = self.abrir_img)

        self.button2.pack()

    def abrir_img(self):
        subprocess.Popen(["explorer", "GRAFICA_SISTEMA.png"])