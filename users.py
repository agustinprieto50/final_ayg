import re
from file_manager import open_excel
import pandas as pd


def list_users(data: list): # pasamos el xlsx
    users = list()

    # recorremos la lista con la raw data
    for i in data:
        # buscamos que no hayan lineas vacias
        # str(i[1]) se fija en la columna de usuarios
        if 'nan' not in str(i[1]):
            # \b busca la palabra completa
            # [A-Za-z-\.\/\d*] busca nombres con mayus, minusculas, digitos (pueden estar o no), puntos o guiones "-".
            regex = re.search(r'\b([A-Za-z-\.\/\d*]{1,})\b', str(i)) # busca los nombres 
            # si encuentra alguna coincidencia, lo agrega a la lista de users
            if regex:
                # group devuelve el match como string
                users.append(regex.group())
    
    users = list(set(users))
    users.pop(users.index('nan'))
        
    return users


# Obtener los registros del usuario ingresado
# Retorna una lista de registros con los siguientes campos:
#   [USER, FECHA_INICIO, FECHA_FIN, TST]
def tiempos_usuario(nombre): 
    df = pd.read_excel('acts-user.xlsx', engine='openpyxl', header=0)
    lista = df.values.tolist()

    # A modo de utilizar regex, se realiza una expresion regular con
    # el nombre del usuario y cada vez que matchea se agrega el registro
    # con los campos de interes unicamente a una lista
    r = re.compile(nombre)
    datos_usuario = []
    for i in lista:
        if r.match(str(i[1])): 
            datos_usuario.append([i[1], i[2], i[3], i[4]])
    return datos_usuario
