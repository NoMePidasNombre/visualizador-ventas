import pandas as pd



def traer_todo(datos):
    return datos.head(datos.shape[0])
    

def aplicar_filtro(opcion, datos):
    if opcion == "Sin Filtro":
        return datos
    elif opcion == "Nombre - A-Z":
        datos_filtrados = datos.sort_values(by="Cliente", ascending=True)
    elif opcion == "Nombre - Z-A":
        datos_filtrados = datos.sort_values(by="Cliente", ascending=False)
    elif opcion == "Fecha - más antiguo":
        datos_filtrados = datos.sort_values(by="Fecha", ascending=True)
    elif opcion == "Fecha - más recientes":
        datos_filtrados = datos.sort_values(by="Fecha", ascending=False)
    
    return datos_filtrados