import re
from file_manager import open_excel
import pandas as pd


# data = pd.read_excel(r'acts-user.xlsx', engine='openpyxl', header=0) 
def list_users(data: list): # pasamos el xlsx
    users = list()
    for i in data:
        if 'nan' not in str(i[1]):
            regex = re.search(r'\b([A-Za-z-\.\/\d*]{1,})\b', str(i)) # busca los nombres 
            if regex:
                users.append(regex.group())
    return list(set(users))


def tiempos_usuario(nombre): 
    df = pd.read_excel('acts-user.xlsx', engine='openpyxl', header=0)
    lista = df.values.tolist()
    r = re.compile(nombre)
    datos_usuario = []
    for i in lista:
        if r.match(str(i[1])): 
            datos_usuario.append([i[1], i[2], i[3], i[4]])

    return datos_usuario
# print(open('acts-user.xlsx'))
# print(list_users(open('acts-user.xlsx')))