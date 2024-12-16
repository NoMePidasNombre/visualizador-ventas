import matplotlib.pyplot as plt
import pandas as pd

def graficar(datos):

    productos = datos.get(['Producto'])
    print(productos.to_numpy()) #Lo convierto a un arreglo de arreglos

    # Segundo gráfico: Gráfico de barras cantidad de compras por cada cliente

    # Tercer gráfico: Gráfico de línea de productos vendidos a lo largo del tiempo

    # Cuarto gráfico: Gráfico de barras cantidad de productos vendidos

    # Quinto gráfico: Gráfico de ingresos por cada mes
    