import pandas as pd
import datetime as dt
import re
from datetime import date


# Validar la fecha ingresada y en caso de que no
# matcheen con la expresion regular se las reemplaza
# por un valor default que es el dia de la fecha
def validate_fecha(fecha):

    #          AÑO   sep        MES          sep               DIA
    regex = r"\d{4}(\-|/| )(0?[1-9]|1[0-2])(\-|/| )(0?[1-9]|[1-2][0-9]|3[0-1])"
    if not re.match(regex, fecha):
        print("[ADVERTENCIA]: El valor ingresado no fue valido y tomara el valor por defecto")
        fecha = date.today().strftime("%Y-%m-%d")
    return fecha


# Pasar datos como lista, inicio y fin como una tupla (año, mes, dia)
# Retorna el tiempo de sesion total para el usuario y rango de fechas dado
def session_time_total(datos, inicio: str, fin: str):
    # Obtener una lista de los numeros que componen la fecha
    fecha_inicio  = re.split("-|/| ", inicio)
    fecha_final  = re.split("-|/| ", fin)

    # Pasarlos al constructor del objeto date time como enteros
    date_inicio = dt.datetime(int(fecha_inicio[0]), int(fecha_inicio[1]), int(fecha_inicio[2])).date()
    date_final = dt.datetime(int(fecha_final[0]), int(fecha_final[1]), int(fecha_final[2])).date()
    sess_time_total = 0

    # Iterar sobre los datos y sumar al contador los que se encuentran dentro del rango
    for i in datos:
        try:
            # Los objetos datetime tienen implementados los operadores de comparacion, por lo que
            # facilitan el hecho de buscar dentro de un rango de fechas
            if pd.to_datetime(i[1]).date() >= date_inicio and pd.to_datetime(i[2]).date() <= date_final:
                sess_time_total += i[3]
        except:
            continue
    return sess_time_total


if __name__ == '__main__':
    '''
    ['mleenw', Timestamp('2019-08-29 08:40:00'), datetime.datetime(2019, 8, 29, 8, 41), 23.0]
    ['mleenw', Timestamp('2019-08-29 08:41:00'), datetime.datetime(2019, 8, 29, 8, 45), 244.0]
    ['mleenw', Timestamp('2019-08-29 09:07:00'), datetime.datetime(2019, 8, 29, 9, 12), 343.0]
    ['mleenw', Timestamp('2019-08-29 10:03:00'), datetime.datetime(2019, 8, 29, 14, 1), 14267.0]
    ['mleenw', Timestamp('2019-08-29 10:32:00'), datetime.datetime(2019, 8, 29, 11, 30), 3491.0]
    ['mleenw', Timestamp('2019-08-29 11:38:00'), datetime.datetime(2019, 8, 29, 12, 14), 2158.0]
    ['mleenw', Timestamp('2019-08-29 12:33:00'), datetime.datetime(2019, 8, 29, 12, 34), 82.0]
    ['mleenw', Timestamp('2019-08-29 12:35:00'), datetime.datetime(2019, 8, 29, 12, 35), 24.0]
    ['mleenw', Timestamp('2019-08-30 08:58:00'), datetime.datetime(2019, 8, 30, 9, 7), 560.0]
    ['mleenw', Timestamp('2019-08-30 09:09:00'), datetime.datetime(2019, 8, 30, 9, 14), 274.0]
    ['mleenw', Timestamp('2019-08-30 09:14:00'), datetime.datetime(2019, 8, 30, 9, 24), 566.0]
    ['mleenw', Timestamp('2019-08-30 10:24:00'), datetime.datetime(2019, 8, 30, 14, 2), 13101.0]
    '''
    # datos = f2.tiempos_usuario('mleenw')
    # rango = session_time_total(datos, '2019-08-29', '2019-08-30')
    # print(rango)
