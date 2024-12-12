import pandas as pd
import tkinter as tk
from tkinter import filedialog, font

def ventana_principal(datos):
    Principal = tk.Tk()
    pruebaver = tk.Label(Principal, text=datos).grid(column=0, row=0, sticky="nswe")
    Principal.mainloop()

