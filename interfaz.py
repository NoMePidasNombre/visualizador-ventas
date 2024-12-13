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
    Principal.columnconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1)
    ancho_ventana = 700
    alto_ventana = 400
    ancho_pantalla = Principal.winfo_screenwidth()
    alto_pantalla = Principal.winfo_screenheight()
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2) - 70
    Principal.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    fonttitulo = font.Font(family="Lucida Fax", size=16, weight="bold")

    #Creo un frame para la barra de busqueda y el botón de buscar
    frame_busqueda = tk.Frame(Principal)
    frame_busqueda.grid(row=0, column=0, columnspan=5)

    global barrabusqueda
    barrabusqueda = tk.Entry(frame_busqueda)
    barrabusqueda.grid(row=0, column=0, columnspan=4)
    barrabusqueda.insert(0, "Ingrese aquí para buscar...")
    barrabusqueda.bind("<FocusIn>", on_entry_click)  # Al hacer clic
    barrabusqueda.bind("<FocusOut>", on_focusout)  # Al perder el foco

    btn_buscar = tk.Button(frame_busqueda, text="Buscar", command=lambda: buscar(barrabusqueda.get(), datos))
    btn_buscar.grid(row=0, column=5)

    #Creo el frame de visualizacion e inserto treeview
    global tree
    frame = tk.Frame(Principal) 
    frame.grid(row=1, column=0, columnspan=7, padx=10, pady=16, sticky="nsew")
    tree = ttk.Treeview(frame, show="headings")
    tree.grid(row=1, column=0, sticky="nsew")
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    tree.configure(yscrollcommand=scrollbar.set)

    #Configuro las columnas del treeview 
    tree["columns"] = ["Fecha", "Cliente", "Producto", "Cantidad", "Precio Unitario", "Total"] 
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=100) 
    global total
    total = tk.Label(Principal, text=f"Total:")
    total.grid(row=11, column=6)

    #Ajusto el tamaño del frame para que sea flexible
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    #Boton de filtros
    global filtro_seleccionado
    filtro_seleccionado = tk.StringVar(value="Sin filtro")
    filtros = ["Sin filtro", "Nombre - A-Z", "Nombre - Z-A", "Fecha - más antiguo", "Fecha - más recientes"]
    menu_opciones = tk.OptionMenu(Principal, filtro_seleccionado, *filtros).grid(column=5,row=0, sticky="nswe")
    boton_mostrar = tk.Button(Principal, text="Mostrar Selección", command=functools.partial(mostrar_seleccion, datos)).grid(column=6,row=0, sticky="nswe")

    #Muestro todos los datos del archivo sin filtro
    mostrar(traer_todo(datos)) 

    Principal.mainloop()

#Funcion que servira para los filtros
def mostrar_seleccion(datos):
    opcion = filtro_seleccionado.get()
    if opcion != "Sin filtro":
        datos_filtrados = aplicar_filtro(opcion, datos)
        mostrar(datos_filtrados)
    else: 
        mostrar(datos.head(datos.shape[0]))

def buscar(texto, datos):
    texto = texto.lower()
    if texto and texto != "Ingrese aquí para buscar...":
        # Filtra filas que contienen el texto en alguna columna
        resultado = datos[datos.apply(lambda row: row.astype(str).str.contains(texto, case=False).any(), axis=1)]
        mostrar(resultado)  # Actualiza el Treeview con los resultados
    else:
        mostrar(datos)  # Muestra todos los datos si no hay texto


#Funcion que itera segun el Dataframe que recibe como parámetro para mostrarlo en el treeview
def mostrar(datos):
    sumatotal = 0
    #Borro lo que estaba en el treeview
    for row in tree.get_children():
        tree.delete(row)
    #Muestro los datos que pasaron como parametro
    for _, row in datos.iterrows():
        tree.insert("", "end", values=list(row))
    sumatotal = datos["Total"].sum()
    total.config(text=f"Total: ${sumatotal}")


#Funciones para manejar el placeholder en la barra de busqueda
def on_entry_click(event):
    if barrabusqueda.get() == "Ingrese aquí para buscar...":
        barrabusqueda.delete(0, tk.END)  #Borra el texto

def on_focusout(event):
    if barrabusqueda.get() == "":
        barrabusqueda.insert(0, "Ingrese aquí para buscar...")  #Restaura el texto
