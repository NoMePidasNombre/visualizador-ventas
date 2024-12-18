import pandas as pd
import tkinter as tk
from tkinter import filedialog, font, messagebox
from interfaz import ventana_principal

def carga_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    if archivo:
        try:
            
            global datos
            datos = pd.read_csv(archivo)
            nombre_columnas = list(datos.columns)
            if 'Fecha' in nombre_columnas and 'Cantidad' in nombre_columnas and 'Cliente' in nombre_columnas and 'Total' in nombre_columnas and 'Producto' in nombre_columnas and 'Precio Unitario' in nombre_columnas:
                ventanaArch.destroy()
                ventana_principal(datos)
            else:
                messagebox.showerror("Error", "El archivo ingresado no es válido.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar el archivo: {e}")


def iniciar():      
    global ventanaArch
    ventanaArch = tk.Tk()
    ventanaArch.title("Ingresar archivo")
    ventanaArch.columnconfigure([0, 1, 2], weight=1)

    ancho_ventana = 400
    alto_ventana = 90
    ancho_pantalla = ventanaArch.winfo_screenwidth()
    alto_pantalla = ventanaArch.winfo_screenheight()
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2) - 70
    ventanaArch.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    fonttitulo = font.Font(family="Lucida Fax", size=16, weight="bold")
    ventanaArch.minsize(400, 90)
    ventanaArch.maxsize(400, 90)

    tk.Label(ventanaArch, text="Visualizador de Ventas", font=fonttitulo).grid(row=0, column=1, sticky="nswe")
    tk.Button(text="Cargar archivo .csv", command=carga_archivo).grid(column=1, row=1, sticky="nswe")
    tk.Label(ventanaArch, text="By: Tomas D.", font=fonttitulo).grid(row=2, column=1, sticky="nswe")
    ventanaArch.mainloop()