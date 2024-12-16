import matplotlib.pyplot as plt

# Crear una figura con dos subgráficos (2 filas, 1 columna)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))  # figsize ajusta el tamaño de la ventana

# Primer gráfico: Gráfico de barras
fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax1.bar(fruits, counts, label=bar_labels, color=bar_colors)
ax1.set_ylabel('fruit supply')
ax1.set_title('Fruit supply by kind and color')
ax1.legend(title='Fruit color')

# Segundo gráfico: Gráfico de barras horizontales con huecos
ax2.broken_barh([(110, 30), (150, 10)], (10, 9), facecolors='tab:blue')
ax2.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                facecolors=('tab:orange', 'tab:green', 'tab:red'))
ax2.set_ylim(5, 35)
ax2.set_xlim(0, 200)
ax2.set_xlabel('seconds since start')
ax2.set_yticks([15, 25], labels=['Bill', 'Jim'])  # Modificar etiquetas del eje Y
ax2.grid(True)  # Hacer visibles las líneas de la cuadrícula
ax2.annotate('race interrupted', (61, 25),
             xytext=(0.8, 0.9), textcoords='axes fraction',
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12,
             horizontalalignment='right', verticalalignment='top')

# Ajustar espacio entre gráficos
fig.tight_layout()

# Mostrar gráficos
plt.show()
