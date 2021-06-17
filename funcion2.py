import pandas as pd
import re 


def tiempos_usuario(nombre): 
    df = pd.read_excel('acts-user.xlsx', engine='openpyxl', header=0)
    lista = df.values.tolist()
    r = re.compile(nombre)
    datos_usuario = []
    for i in lista:
        if r.match(str(i[1])): 
            datos_usuario.append([i[1], i[2], i[3], i[4]])

    return datos_usuario

if __name__ == '__main__': 
    datos = tiempos_usuario('mleenw')
    # datos : lista de listas [nombre_usuario, inicio_conexion, fin_conexion, session_time]
    for i in datos: 
        print(i)