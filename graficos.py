import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

def graficar(datos):
    fig = plt.figure(figsize=(12, 10))  # Tamaño del gráfico ajustado
    grilla = GridSpec(2, 2, figure=fig)
    fig.suptitle('Resumen de datos', fontsize=16, fontweight='bold')

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
    ax = fig.add_subplot(grilla[0, 0])
    ax.barh(y, x)
    ax.set_xticks(range(0, max_value + 1))
    ax.set_xlabel('Cantidad')
    ax.set_title('Cantidad de productos vendidos', fontsize=12)
    ax.tick_params(axis='y', labelsize=5)  # Reducir el tamaño de las etiquetas del eje Y

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

    ax1 = fig.add_subplot(grilla[0, 1])
    max_value = max(y)
    ax1.bar(x, y)
    ax1.set_yticks(range(0, max_value + 1))
    ax1.set_xlabel('Clientes')
    ax1.set_title('Cantidad de compras por cliente', fontsize=12)
    ax1.tick_params(axis='x', labelrotation=45, labelsize=8)  # Roto 45º las etiquetas para que se vea mejor


    # Tercer gráfico: Gráfico de línea de ingresos totales de cada mes

    diccionario_cantidades_mensuales = {"Enero": 0, "Febrero": 0, "Marzo": 0, "Abril": 0, "Mayo": 0, "Junio": 0, "Julio": 0, "Agosto": 0,"Septiembre": 0, "Octubre": 0, "Noviembre": 0, "Diciembre": 0}
    
    cantidades = datos[['Fecha','Total']].to_numpy()
    
    for cantidad in cantidades:
        if "-01-" in cantidad[0]:
            diccionario_cantidades_mensuales["Enero"] += cantidad[1]
        elif "-02-" in cantidad[0]:
            diccionario_cantidades_mensuales["Febrero"] += cantidad[1]
        elif "-03-" in cantidad[0]:
            diccionario_cantidades_mensuales["Marzo"] += cantidad[1]
        elif "-04-" in cantidad[0]:
            diccionario_cantidades_mensuales["Abril"] += cantidad[1]
        elif "-05-" in cantidad[0]:
            diccionario_cantidades_mensuales["Mayo"] += cantidad[1]
        elif "-06-" in cantidad[0]:
            diccionario_cantidades_mensuales["Junio"] += cantidad[1]
        elif "-07-" in cantidad[0]:
            diccionario_cantidades_mensuales["Julio"] += cantidad[1]
        elif "-08-" in cantidad[0]:
            diccionario_cantidades_mensuales["Agosto"] += cantidad[1]
        elif "-09-" in cantidad[0]:
            diccionario_cantidades_mensuales["Septiembre"] += cantidad[1]
        elif "-10-" in cantidad[0]:
            diccionario_cantidades_mensuales["Octubre"] += cantidad[1]
        elif "-11-" in cantidad[0]:
            diccionario_cantidades_mensuales["Noviembre"] += cantidad[1]
        elif "-12-" in cantidad[0]:
            diccionario_cantidades_mensuales["Diciembre"] += cantidad[1]

    x = list(diccionario_cantidades_mensuales.keys())
    y = list(diccionario_cantidades_mensuales.values())

    ax2 = fig.add_subplot(grilla[1, :])
    ax2.plot(x, y)
    ax2.set_xlabel('Meses')
    ax2.set_title('Total de ingresos por mes', fontsize=12)
    ax2.tick_params(axis='x', labelrotation=45, labelsize=8)

    # Mostrar los gráficos generados
    plt.tight_layout()  # Ajusta automáticamente los márgenes y separaciones
    plt.subplots_adjust(top=0.88, hspace=0.6)
    plt.show()