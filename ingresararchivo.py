import pandas as pd
import tkinter as tk
from tkinter import filedialog


def carga_archivo():
    archivo = filedialog.askopenfilename(
        title="Seleccionar archivo CSV",
        filetypes=[("Archivos CSV", "*.csv")]
    )
    if archivo:
        try:
            datos = pd.read_csv(archivo)
            print("Datos cargados correctamente:")
            print(datos.head())
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")


ventanaArch = tk.Tk()
ventanaArch.title("Ingresar archivo")
ventanaArch.geometry("400x200")

botoncarga = tk.Button(text="Cargar", command=carga_archivo)
botoncarga.grid(column=0, row=0, sticky="nswe")
ventanaArch.mainloop()