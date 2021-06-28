import pandas as pd
import datetime as dt
import re
from datetime import date


# Validar la fecha ingresadas y en caso de que no
# matcheen con la expresion regular se las reempleza
# porun valor default que es el dia de la fecha
def validate_fechas(fecha_inicio, fecha_fin):
    regex = r"(\d{4})(-|/| )(\d{1,2})(-|/| )(\d{1,2})"
    if not re.match(regex, fecha_inicio):
        fecha_inicio = date.today().strftime("%Y-%m-%d")
    if not re.match(regex, fecha_fin):
        fecha_fin = date.today().strftime("%Y-%m-%d")
    return fecha_inicio, fecha_fin


# Pasar inicio y fin como una tupla (año, mes, dia)
def session_time_total(datos, inicio: str, fin: str):
    fecha_inicio  = re.split("-|/| ", inicio)
    fecha_final  = re.split("-|/| ", fin)
    date_inicio = dt.datetime(int(fecha_inicio[0]), int(fecha_inicio[1]), int(fecha_inicio[2])).date()
    date_final = dt.datetime(int(fecha_final[0]), int(fecha_final[1]), int(fecha_final[2])).date()
    sess_time_total = 0
    for i in datos:
        try:
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
