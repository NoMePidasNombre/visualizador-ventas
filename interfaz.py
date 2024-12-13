import pandas as pd
import tkinter as tk
from tkinter import filedialog, font, ttk
from filtrar import *
import functools

def ventana_principal(datos):
    #Inicio la interfaz principal
    global Principal
    
    Principal = tk.Tk()
    Principal.title("Visualizador de ventas")
    ancho_ventana = 700
    alto_ventana = 400
    ancho_pantalla = Principal.winfo_screenwidth()
    alto_pantalla = Principal.winfo_screenheight()
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2) - 70
    Principal.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    fonttitulo = font.Font(family="Lucida Fax", size=16, weight="bold")

    #Creo el frame e inserto treeview
    global tree
    frame = tk.Frame(Principal) 
    frame.grid(row=1, column=0, columnspan=6, padx=10, pady=10)
    tree = ttk.Treeview(frame, show="headings")
    tree.grid(row=1, column=0, sticky="nsew")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    #Configuro las columnas del treeview 
    tree["columns"] = ["Fecha", "Cliente", "Producto", "Cantidad", "Precio Unitario", "Total"] 
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=100) 

    #Ajusto el tamaño del frame para que sea flexible
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    #Muestro todos los datos del archivo sin filtro
    mostrar(traer_todo(datos)) 

    #Boton de filtros
    global filtro_seleccionado
    filtro_seleccionado = tk.StringVar(value="Sin filtro")
    filtros = ["Sin filtro", "Nombre - A-Z", "Nombre - Z-A", "Fecha - más antiguo", "Fecha - más recientes"]
    menu_opciones = tk.OptionMenu(Principal, filtro_seleccionado, *filtros).grid(column=2,row=0, sticky="nswe")
    boton_mostrar = tk.Button(Principal, text="Mostrar Selección", command=functools.partial(mostrar_seleccion, datos)).grid(column=3,row=0, sticky="nswe")

    
    Principal.mainloop()

#Funcion que servira para los filtros
def mostrar_seleccion(datos):
    opcion = filtro_seleccionado.get()
    if opcion != "Sin filtro":
        datos_filtrados = aplicar_filtro(opcion, datos)
        mostrar(datos_filtrados)
    else: 
        mostrar(datos.head())
    

#Funcion que itera segun el Dataframe que recibe como parámetro para mostrarlo en el treeview
def mostrar(datos):
    #Borro lo que estaba en el treeview
    for row in tree.get_children():
        tree.delete(row)
    #Muestro los datos que pasaron como parametro
    for _, row in datos.iterrows():
        tree.insert("", "end", values=list(row))
    