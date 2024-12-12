import pandas as pd
import tkinter as tk
from tkinter import filedialog, font

def ventana_principal(datos):
    # nombres = datos['Cliente'][1]
    filas = datos.shape[0]
    print(filas)
    Principal = tk.Tk()
    Principal.title("Visualizador de ventas")

    for x in range(filas):

        Fecha = datos['Fecha'][x]
        tk.Label(Principal, text=Fecha).grid(row=x+1, column=0, sticky="nswe")

        nombre = datos['Cliente'][x]
        tk.Label(Principal, text=nombre).grid(row=x+1, column=1, sticky="nswe")

        Producto = datos['Producto'][x]
        tk.Label(Principal, text=Producto).grid(row=x+1, column=2, sticky="nswe")

        Cantidad = datos['Cantidad'][x]
        tk.Label(Principal, text=Cantidad).grid(row=x+1, column=3, sticky="nswe")

        Precio = datos['Precio Unitario'][x]
        tk.Label(Principal, text=Precio).grid(row=x+1, column=4, sticky="nswe")

        total = Cantidad*Precio
        tk.Label(Principal, text=total).grid(row=x+1, column=5, sticky="nswe")

    ancho_ventana = 400
    alto_ventana = 400
    ancho_pantalla = Principal.winfo_screenwidth()
    alto_pantalla = Principal.winfo_screenheight()
    pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
    pos_y = (alto_pantalla // 2) - (alto_ventana // 2) - 70
    Principal.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
    fonttitulo = font.Font(family="Lucida Fax", size=16, weight="bold")




    Principal.mainloop()

