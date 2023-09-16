import tkinter as tk
import tkinter.font as font

class ayuda:
    def __init__(self, frame):
        self.frame = frame

        self.ventana = tk.Toplevel(self.frame, bg="#D7EEF5")

        #self.ventana.geometry("850x450")

        self.titulo = font.Font(family='Helvetica', size=25)
        self.fuente1 = font.Font(family='Helvetica', size=20)
        self.fuente2 = font.Font(family='Helvetica', size=15)

        self.ventana.title("Ayuda")

        label = tk.Label(self.ventana, text="Información sobre el programa", font=self.titulo, bg="#D7EEF5")
        label.pack(side="top", fill="x", pady=10)

        label1 = tk.Label(self.ventana, text="Datos del estudiante:", font = self.fuente1, bg="#D7EEF5")
        label1.pack(side="top", fill="x", pady=10)
        
        label2 = tk.Label(self.ventana, text="-> José David Góngora Olmedo\n-> 202201444\n-> Introducción a la Programación y Computación 2 sección ""D""\n-> Ingenieria en Ciencias y Sistemas\n-> 4to Semestre", font = self.fuente2, bg="#D7EEF5")
        label2.pack(side="top", fill="x", pady=10)

        label3 = tk.Label(self.ventana, text="Documentación", font = self.fuente1, bg="#D7EEF5")
        label3.pack(side="top", fill="x", pady=10)

        label4 = tk.Label(self.ventana, text="lolo", font = self.fuente2, bg="#D7EEF5")
        label4.pack(side="top", fill="x", pady=10)
        
        button = tk.Button(self.ventana, text="Cerrar",
            highlightbackground='black', height= 4, width=10, command=self.ventana.destroy, bg="#ebf7fa", activebackground="#aeddeb")
        button.pack(anchor="s", side="left")
        