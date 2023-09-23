import tkinter as tk
from tkinter import font, ttk, messagebox
class gestion_mensajes:
    def __init__(self, raiz, funciones):
        self.raiz = raiz

        self.fn = funciones

        self.ventana_gestion = tk.Toplevel(self.raiz, bg="#D7EEF5")
        self.ventana_gestion.resizable(0,0)
        self.ventana_gestion.pack_propagate(False)
        self.ventana_gestion.rowconfigure(0, weight=1)
        self.ventana_gestion.rowconfigure(1, weight=1)
        self.ventana_gestion.rowconfigure(2, weight=1)

        self.titulo = font.Font(family='Helvetica', size=25)
        self.fuente1 = font.Font(family='Helvetica', size=20)
        self.fuente2 = font.Font(family='Helvetica', size=15)
        self.fuente3 = font.Font(family='Helvetica', size=13)

        self.ventana_gestion.title("Gestión de mensajes")

        label = tk.Label( self.ventana_gestion, text="Gestión de mensajes", font=self.titulo, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=0)

        self.button = tk.Button(self.ventana_gestion, text="Cerrar",
            highlightbackground='black', height= 2, width=10, command=self.ventana_gestion.destroy, font = self.fuente3, bg="#ebf7fa", activebackground="#aeddeb")
        self.button.grid(row=2, column=0, sticky="sw")

        self.frame_msg = tk.Frame(self.ventana_gestion, bg="red")

        self.frame_msg.config(width=1250, height=750)
        self.frame_msg.pack_propagate(False)
        self.frame_msg.grid_propagate(False)
        self.frame_msg.grid(row=1, column=0)

        self.frame_table = tk.Frame(self.frame_msg, bg="#D7EEF5")
        self.frame_table.pack_propagate(False)
        self.frame_table.config(width=625, height=750)
        self.frame_table.grid(row=0, column=0)

        labelmsg = tk.Label( self.frame_table, text="Lista de mensajes", font=self.fuente2, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        labelmsg.pack()

        self.table_msg = ttk.Treeview(self.frame_table, columns=("col1", "col2"), height=10)

        self.table_msg.column("#0",width=75, anchor="center")
        self.table_msg.column("col1",width=200, anchor="center")
        self.table_msg.column("col2",width=200, anchor="center")

        self.table_msg.heading("#0", text="No.", anchor="center")
        self.table_msg.heading("col1", text="Nombre mensaje", anchor="center")
        self.table_msg.heading("col2", text="Sistema", anchor="center")

        self.table_msg.pack(pady=25)

        self.llenar_tabla_msg()

        self.button2 = tk.Button(self.frame_table, text="Cargar instrucciones", highlightbackground='black', height= 2, width=15, padx=10, font = self.fuente3, bg="#ebf7fa", activebackground="#aeddeb", command = self.mensaje_seleccionado)

        self.button2.pack()

        labelins = tk.Label( self.frame_table, text="Lista de instrucciones", font=self.fuente2, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        labelins.pack(pady=15)

        self.table_ins= ttk.Treeview(self.frame_table, columns=("col1", "col2"), height=8)

        self.table_ins.column("#0", width=125, anchor="center")
        self.table_ins.column("col1", width=125, anchor="center")
        self.table_ins.column("col2", width=125, anchor="center")

        self.table_ins.heading("#0", text="No.", anchor="center")
        self.table_ins.heading("col1", text="Dron", anchor="center")
        self.table_ins.heading("col2", text="Instruccion", anchor="center")

        self.table_ins.pack(pady=25)

        self.frame_mensje = tk.Frame(self.frame_msg, bg="yellow")
        self.frame_mensje.pack_propagate(False)
        self.frame_mensje.grid_propagate(False)
        self.frame_mensje.config(width=625, height=750)
        self.frame_mensje.grid(row=0, column=1)

        labelen = tk.Label( self.frame_mensje, text="Instrucciones para enviar un mensaje", font=self.fuente2, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        labelen.pack()

    def llenar_tabla_msg(self):
        lista_msg = self.fn.obtener_lista_mensajes()
        if lista_msg.obtener_size() != 0:
            for index, msg in enumerate(lista_msg):
                self.table_msg.insert("", "end", text=f"{index+1}", values=(f"{msg.nombre_msg}",f"{msg.sistema}"))

    def mensaje_seleccionado(self):
        self.limpiar_tabla(self.table_ins)
        item_seleccionado = self.table_msg.focus()
        if item_seleccionado:
            datos = self.table_msg.item(item_seleccionado)
            lista_msg = self.fn.obtener_lista_instrucciones_por_mensaje(datos.get("values")[0])
            self.fn.formar_mensaje(datos.get("values")[0])
            for index, ins in enumerate(lista_msg.instrucciones):
                self.table_ins.insert("", "end", text=f"{index+1}", values=(f"{ins.dron}",f"{ins.instruccion}"))
        else :
            messagebox.showerror("Error", "Debes seleccinar un mensaje", parent = self.ventana_gestion)

    def limpiar_tabla(self, table):
        for items in table.get_children():
            table.delete(items)