import pandas as pd


def open_excel(path): # abre el excel
    data = pd.read_excel(path, engine='openpyxl', header=0)
    raw_list = data.values.tolist() # la convertimos en lista
    for i in raw_list: # filtramos los datos
        del i[0], i[4], i[4], i[4], i[4]
    return raw_list
