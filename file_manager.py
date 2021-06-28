"""
En este modulo se encuentran las funciones relacionadas al manejo
de archivos, tales como, lectura, escritura y creacion.
"""
import pandas as pd


def open_excel(path): # abre el excel
    data = pd.read_excel(path, engine='openpyxl', header=0)
    raw_list = data.values.tolist() # la convertimos en lista
    for i in raw_list: # filtramos los datos
        del i[0], i[4], i[4], i[4], i[4]
    return raw_list


# Lee un archivo csv y devuelve el dataframe
def read_csv(path):
    df = pd.read_csv(path)
    return df


# Guarda en un archivo csv el nuevo registro obtenido
# ** El nuevo registro se guarda al final **
def dump_csv(path, user, fecha_inicio, fecha_final, rango):
    df = pd.DataFrame({"Usuario": [user],
                       "Fecha comienzo": [fecha_inicio],
                       "Fecha final": [fecha_final],
                       "TST [segundos]": [rango]})
    df.to_csv("user_TST.csv", encoding="utf-8", index=False, header=None, mode="a")
    return
