import tkinter as tk
import tkinter.font as font

from tkinter import ttk, messagebox
from funciones.funciones_archivo import funciones_archivo

class gestion_drones:

    def __init__(self, frame, lista, funciones):
        self.frame = frame
        self.lista = lista
        self.funciones = funciones

        self.ventana_gestion = tk.Toplevel(self.frame, bg="#D7EEF5")
        self.ventana_gestion.resizable(0,0)

        self.titulo = font.Font(family='Helvetica', size=25)
        self.fuente1 = font.Font(family='Helvetica', size=20)
        self.fuente2 = font.Font(family='Helvetica', size=15)
        self.fuente3 = font.Font(family='Helvetica', size=13)

        #self.fn = funciones_archivo()
        self.ventana_gestion.title("Gestión de drones")

        label = tk.Label( self.ventana_gestion, text="Gestión de drones", font=self.titulo, bg="#D7EEF5")
        label.pack(side="top", fill="x", pady=10)

        self.contenido = tk.Frame(self.ventana_gestion, bg="#D7EEF5")

        self.contenido.config(width=880, height=450)
        self.contenido.pack_propagate(False)
        self.contenido.grid_propagate(False)
        self.contenido.pack()

        button = tk.Button(self.ventana_gestion, text="Cerrar",
            highlightbackground='black', height= 2, width=10, command=self.ventana_gestion.destroy, font = self.fuente2, bg="#ebf7fa", activebackground="#aeddeb")
        button.pack(anchor="s", side="left")

        self.frame_table = tk.Frame(self.contenido, bg="#D7EEF5")
        self.frame_table.pack_propagate(False)
        self.frame_table.grid_propagate(False)
        self.frame_table.config(width=440, height=450)
        self.frame_table.grid(row=0, column=0)

        self.table = ttk.Treeview(self.frame_table, columns=("col1"), height=450)

        self.table.column("#0",width=220, anchor="center")
        self.table.column("col1",width=220, anchor="center")

        self.table.heading("#0", text="No.", anchor="center")
        self.table.heading("col1", text="Nombre dron", anchor="center")

        self.llenar_tabla()

        self.table.pack()

        self.frame_add = tk.Frame(self.contenido, bg="#D7EEF5")
        self.frame_add.pack_propagate(False)
        self.frame_add.grid_propagate(False)
        self.frame_add.config(width=440, height=450)
        self.frame_add.place(anchor="center")
        self.frame_add.grid(row=0, column=1)

        label1 = tk.Label( self.frame_add, text="Agregar Dron", font=self.fuente1, bg="#D7EEF5")
        label1.pack(side="top", fill="x")

        label2 = tk.Label( self.frame_add, text="Nombre", font=self.fuente2, bg="#D7EEF5")
        label2.pack(side="top", fill="x", pady=60)

        self.agregar = tk.Entry(self.frame_add, width=25, font=self.fuente3, justify="center")
        self.agregar.pack()

        button = tk.Button(self.frame_add, text="Agregar",
            highlightbackground='black', height= 1, width=10, bg="#ebf7fa", activebackground="#aeddeb", font = self.fuente2, command = self.guardar_dron)
        button.pack(anchor="s", side="bottom")

    def llenar_tabla(self):
        #lista_drones = self.fn.obtener_lista_drones()

        if self.lista != 0:
            for index, drones in enumerate(self.lista):
                self.table.insert("", "end", text=f"{index+1}", values=(f"{drones.nombre}"))

    def limpiar_tabla(self):
        for items in self.table.get_children():
            self.table.delete(items)
        self.agregar.delete(0, 'end')

    def guardar_dron(self):
        if self.agregar.get() == '':
            messagebox.showerror("Error", "Debes llenar el espacio.", parent = self.ventana_gestion)
        else :
            if self.funciones.agregar_nuevo_dron(self.agregar.get()):

                messagebox.showinfo("Exito", "Se ha agregado el dron correctamente.", parent = self.ventana_gestion)
                self.limpiar_tabla()
                self.llenar_tabla()
            else:
                messagebox.showerror("Error", "Ya existe un dron con ese nombre.", parent = self.ventana_gestion)
