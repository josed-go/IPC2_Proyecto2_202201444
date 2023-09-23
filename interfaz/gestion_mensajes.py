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
        self.fuente4 = font.Font(family='Helvetica', size=9)

        self.ventana_gestion.title("Gestión de mensajes")

        label = tk.Label( self.ventana_gestion, text="Gestión de mensajes", font=self.titulo, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        label.grid(row=0, column=0)

        self.button = tk.Button(self.ventana_gestion, text="Cerrar",
            highlightbackground='black', height= 2, width=10, command=self.ventana_gestion.destroy, font = self.fuente3, bg="#ebf7fa", activebackground="#aeddeb")
        self.button.grid(row=2, column=0, sticky="sw")

        self.frame_msg = tk.Frame(self.ventana_gestion, bg="#D7EEF5")

        self.frame_msg.config(width=1250, height=750)
        self.frame_msg.pack_propagate(False)
        self.frame_msg.grid_propagate(False)
        self.frame_msg.grid(row=1, column=0)

        self.frame_table = tk.Frame(self.frame_msg, bg="#aeddeb")
        self.frame_table.pack_propagate(False)
        self.frame_table.config(width=625, height=750)
        self.frame_table.grid(row=0, column=0, padx=15)

        labelmsg = tk.Label( self.frame_table, text="Lista de mensajes", font=self.fuente2, bg="#aeddeb")
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

        labelins = tk.Label( self.frame_table, text="Lista de instrucciones", font=self.fuente2, bg="#aeddeb")
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

        self.frame_mensje = tk.Frame(self.frame_msg, bg="#D7EEF5")
        self.frame_mensje.pack_propagate(False)
        self.frame_mensje.grid_propagate(False)
        self.frame_mensje.config(width=625, height=750)
        self.frame_mensje.grid(row=0, column=1)

        labelen = tk.Label( self.frame_mensje, text="Instrucciones para enviar un mensaje", font=self.fuente2, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        labelen.pack()

        label_pequenio = tk.Label( self.frame_mensje, text="Selecciona un mensaje para procesarlo", font=self.fuente4, bg="#D7EEF5")
        #label.pack(side="top", fill="x", pady=10)
        label_pequenio.pack(pady=25)

        self.button_procesar = tk.Button(self.frame_mensje, text="Procesar mensaje", highlightbackground='black', height= 2, width=15, padx=10, font = self.fuente3, bg="#ebf7fa", activebackground="#aeddeb", command = self.procesar)

        self.button_procesar.pack()

        self.frame_datos_msg = tk.Frame(self.frame_mensje,bg="#D7EEF5")
        self.frame_datos_msg.pack_propagate(False)
        self.frame_datos_msg.grid_propagate(False)
        self.frame_datos_msg.config(width=525, height=350)
        self.frame_datos_msg.pack(pady=50)

        self.label_nombre_sistema = tk.Label( self.frame_datos_msg, text="Sistema de drones a utilizar:", font=self.fuente2, bg="#D7EEF5")
        self.label_nombre_sistema.grid(row=0, column=0, padx=45, pady=25)


        self.nombre = tk.StringVar()
        self.nombre_sistema = tk.Entry(self.frame_datos_msg, width=15, font=self.fuente2, justify="left", state="readonly", textvariable=self.nombre)
        self.nombre_sistema.grid(row=0, column=1)

        self.label_mensaje = tk.Label( self.frame_datos_msg, text="Mensaje a enviar", font=self.fuente2, bg="#D7EEF5")
        self.label_mensaje.grid(row=1, column=0, columnspan=2)

        self.mensaje = tk.Text(self.frame_datos_msg, width=50, height=5, font=self.fuente3, state="disabled")
        self.mensaje.grid(row = 2, column=0, columnspan=2, pady=15)

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

    def procesar(self):
        item_seleccionado = self.table_msg.focus()
        if item_seleccionado:
            datos = self.table_msg.item(item_seleccionado)
            nombre_sistema, mensaje = self.fn.formar_mensaje(datos.get("values")[0])
            self.nombre.set(nombre_sistema)
            self.llenar_mensaje(mensaje)           
        else :
            messagebox.showerror("Error", "Debes seleccinar un mensaje", parent = self.ventana_gestion)

    def llenar_mensaje(self, mensaje):
        self.mensaje.config(state="normal")
        self.mensaje.delete("1.0", tk.END)
        self.mensaje.insert("1.0", mensaje)
        self.mensaje.config(state="disabled")

    def limpiar_tabla(self, table):
        for items in table.get_children():
            table.delete(items)