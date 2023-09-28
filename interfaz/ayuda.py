import tkinter as tk
import tkinter.font as font
from tkinter.font import Font, nametofont
from tkinter import ttk
import webbrowser
import os

class ayuda:
    def __init__(self, frame):
        self.frame = frame

        self.ventana = tk.Toplevel(self.frame, bg="#D7EEF5")
        self.ventana.resizable(0,0)

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
        label3.pack(side="top", pady=10)

        # label4 = tk.Label(self.ventana, text="lolo", font = self.fuente2, bg="#D7EEF5")
        # label4.pack()

        self.link = Linkbutton(self.ventana, text=" Abrir documentación del proyecto", command = self.abrir_documentacion)
        self.link.pack( pady=10)
        
        button = tk.Button(self.ventana, text="Cerrar",
            highlightbackground='black', height= 4, width=10, command=self.ventana.destroy, bg="#ebf7fa", activebackground="#aeddeb", font = self.fuente2)
        button.pack(anchor="s", side="left")

    def abrir_documentacion(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(script_dir, '..', 'documentos', 'Documentacion_Proyecto2_202201444.pdf')
        webbrowser.open_new(pdf_path)
        # os.system(pdf_path)

class Linkbutton(ttk.Button):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Obtener el nombre de la fuente por defecto.
        label_font = nametofont("TkDefaultFont").cget("family")
        self.font = font.Font(family='Helvetica', size=15)
        
        # Crear un estilo para el hipervínculo.
        style = ttk.Style()
        style.configure(
            "Link.TLabel", foreground="#357fde", font=self.font, background="#D7EEF5")
        
        
        # Aplicarlo a la clase actual.
        self.configure(style="Link.TLabel", cursor="hand2")
        
        # Configurar los eventos de entrada y salida del mouse.
        self.bind("<Enter>", self.on_mouse_enter)
        self.bind("<Leave>", self.on_mouse_leave)
    
    def on_mouse_enter(self, event):
        # Aplicar subrayado.
        self.font.configure(underline=True)
    
    def on_mouse_leave(self, event):
        # Remover subrayado.
        self.font.configure(underline=False)