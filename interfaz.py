import pandas as pd
import tkinter as tk
from tkinter import filedialog, font, ttk, messagebox
from filtrar import *
import functools

def ventana_principal(datos):
    #Inicio la interfaz principal
    global Principal
    global sinfiltro
    sinfiltro = datos
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
    Principal.minsize(700,400)
    Principal.maxsize(1200, 900)
    fonttitulo = font.Font(family="Lucida Fax", size=16, weight="bold")

    #Creo un frame para la barra de busqueda y el botón de buscar
    frame_busqueda = tk.Frame(Principal)
    frame_busqueda.grid(row=0, column=0)

    global barrabusqueda
    barrabusqueda = tk.Entry(frame_busqueda, width=50)
    barrabusqueda.grid(row=0, column=0, sticky="nsew")
    barrabusqueda.insert(0, "Ingrese aquí para buscar...")
    barrabusqueda.bind("<FocusIn>", on_entry_click)  # Al hacer clic
    barrabusqueda.bind("<FocusOut>", on_focusout)  # Al perder el foco

    btn_buscar = tk.Button(frame_busqueda, text="Buscar", command=lambda: buscar(barrabusqueda.get(), datos))
    btn_buscar.grid(row=0, column=5, padx=10)

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
    

    #Ajusto el tamaño del frame para que sea flexible
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)

    #Menu que filtra los datos del treeview o tabla
    global filtro_seleccionado
    filtro_seleccionado = tk.StringVar(value="Sin filtro")
    filtros = ["Sin filtro", "Nombre - A-Z", "Nombre - Z-A", "Fecha - más antiguo", "Fecha - más recientes"]
    menu_opciones = tk.OptionMenu(Principal, filtro_seleccionado, *filtros).grid(column=6,row=0, sticky="nswe")
    filtro_seleccionado.trace("w", lambda *args: treeview_to_dataframe(tree)) #Activa el cambio de filtro automaticamente, sin boton "Filtrar"

    #Frame de botones de acciones
    frame_botones = tk.Frame(Principal)
    frame_botones.grid(row=11, column=0, columnspan=7, sticky="nsew")

    #Boton para exportar los datos seleccionados en otro csv o excel
    boton_exportar = tk.Button(frame_botones, text="Exportar selección", command=exportar_seleccion)
    boton_exportar.grid(row=11, column=0, sticky="nsew", padx=10)

    #Boton para generar gráficos
    boton_graficos = tk.Button(frame_botones, text="Generar gráficos", command=elegir_otro)
    boton_graficos.grid(row=11, column=1, sticky="nsew", padx=10)

    #Boton para subir otro archivo
    boton_otro = tk.Button(frame_botones, text="Seleccionar otro archivo", command=elegir_otro)
    boton_otro.grid(row=11, column=2, sticky="nsew", padx=10)

    #Total de la tabla
    global total
    frame_botones.columnconfigure(3, weight=3)  # Espacio extra para la última columna
    total = tk.Label(frame_botones, text=f"Total:", anchor="e")
    total.grid(row=11, column=3, padx=(5, 15), sticky="e")

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
        mostrar(sinfiltro.head(sinfiltro.shape[0]))

#Funcion del buscador de datos
def buscar(texto, datos):
    texto = texto.lower()
    if texto and texto != "ingrese aquí para buscar...":
        # Filtra filas que contienen el texto en alguna columna
        resultado = datos[datos.apply(lambda row: row.astype(str).str.contains(texto, case=False).any(), axis=1)]
        mostrar(resultado)  # Actualiza el Treeview con los resultados
    else:
        mostrar(datos)  # Muestra todos los datos


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

# Funcion para tomar los datos del treeview y transformarlos a dataframe nuevamente
def treeview_to_dataframe(treeview):
    # Obtengo los encabezados
    encabezados = [treeview.heading(col)["text"] for col in treeview["columns"]]
    
    # Obtengo los datos de las filas
    filas = [treeview.item(item)["values"] for item in treeview.get_children()]
    
    # Creo el DataFrame y lo paso como parametro a la funcion mostrar()
    nuevos_datos = pd.DataFrame(filas, columns=encabezados) # Utilizando pandas creo un Dataframe(filasdatos, encabezados)
    mostrar_seleccion(nuevos_datos)

def exportar_seleccion(formato="csv"):
    # Obtengo los datos seleccionados
    selected_items = tree.selection()
    if not selected_items:
        messagebox.showwarning("Advertencia", "¡No se ha seleccionado nada!")
    else:
         # Extraigo los datos seleccionados y los convierto a dataframe
        filas = [tree.item(item)["values"] for item in selected_items]
        encabezados = [tree.heading(col)["text"] for col in tree["columns"]]

        
        datos_seleccionados = pd.DataFrame(filas, columns=encabezados)

        # Abro un cuadro de diálogo para que el usuario guarde el archivo en el formato que desee
        filetypes = [("Archivos CSV", "*.csv")] if formato == "csv" else [("Archivos Excel", "*.xlsx")]
        extension = ".csv" if formato == "csv" else ".xlsx"
    
        file_path = filedialog.asksaveasfilename(
            defaultextension=extension,
            filetypes=filetypes,
            title="Guardar archivo como"
        )

        # Exporto a CSV o Excel
        try:
            if formato == "csv":
                datos_seleccionados.to_csv(file_path, index=False)
                messagebox.showinfo("Exportar", "¡Datos exportados con éxito!.")
            else:
                datos_seleccionados.to_excel(file_path, index=False)
                messagebox.showinfo("Exportar", "¡Datos exportados con éxito!.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo exportar: {e}")

#Funcion que permite elegir otro archivo
def elegir_otro():
    Principal.destroy()
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    if archivo:
        try:
            datos = pd.read_csv(archivo)
            ventana_principal(datos)
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
            return

#Funciones para manejar el texto en la barra de busqueda
def on_entry_click(event):
    if barrabusqueda.get() == "Ingrese aquí para buscar...":
        barrabusqueda.delete(0, tk.END)  #Borra el texto

def on_focusout(event):
    if barrabusqueda.get() == "":
        barrabusqueda.insert(0, "Ingrese aquí para buscar...")  #Restaura el texto
