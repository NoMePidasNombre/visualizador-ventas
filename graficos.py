import matplotlib.pyplot as plt
import pandas as pd

def graficar(datos):
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))  # Tamaño del gráfico ajustado
    fig.suptitle('Resumen de datos')

    # Primer gráfico: Gráfico de barras horizontal (cantidad de productos vendidos)
    diccionario_productos = {}
    productos = datos[['Producto', 'Cantidad']].to_numpy()
    for producto in productos:
        if producto[0] in diccionario_productos:
            diccionario_productos[producto[0]] += producto[1]
        else:
            diccionario_productos[producto[0]] = producto[1]

    y = list(diccionario_productos.keys())
    x = list(diccionario_productos.values())

    max_value = max(x)
    ax[0, 0].barh(y, x)
    ax[0, 0].set_xticks(range(0, max_value + 1))
    ax[0, 0].set_xlabel('Cantidad')
    ax[0, 0].set_title('Cantidad de productos vendidos')
    ax[0, 0].tick_params(axis='y', labelsize=8)  # Reducir el tamaño de las etiquetas del eje Y

    # Segundo gráfico: Gráfico de barras (cantidad de compras por cliente)
    diccionario_clientes = {}
    clientes = datos[['Cliente', 'Cantidad']].to_numpy()
    for cliente in clientes:
        if cliente[0] in diccionario_clientes:
            diccionario_clientes[cliente[0]] += cliente[1]
        else:
            diccionario_clientes[cliente[0]] = cliente[1]

    x = list(diccionario_clientes.keys())
    y = list(diccionario_clientes.values())

    max_value = max(y)
    ax[0, 1].bar(x, y)
    ax[0, 1].set_yticks(range(0, max_value + 1))
    ax[0, 1].set_xlabel('Clientes')
    ax[0, 1].set_title('Cantidad de compras por cliente')
    ax[0, 1].tick_params(axis='x', labelrotation=45, labelsize=8)  # Rotar etiquetas del eje X y reducir tamaño

    plt.tight_layout()  # Ajusta automáticamente los márgenes y separaciones
    plt.subplots_adjust(top=0.9)  # Ajusta el espacio del título principal
    plt.show()


    # Tercer gráfico: Gráfico de línea de productos vendidos a lo largo del tiempo

    # Cuarto gráfico: Gráfico de barras cantidad de productos vendidos

    # Quinto gráfico: Gráfico de ingresos por cada mes
    