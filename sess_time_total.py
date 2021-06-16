# Seguimiento del tiempo de sesión (Session Time) de un usuario en un período de tiempo establecido (rango de fechas). 
# Debe incluir una lista de usuarios y la posibilidad de ingresar un rango de fechas.


'''['mleenw', Timestamp('2019-08-29 08:40:00'), datetime.datetime(2019, 8, 29, 8, 41), 23.0]
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
['mleenw', Timestamp('2019-08-30 10:24:00'), datetime.datetime(2019, 8, 30, 14, 2), 13101.0]'''

import pandas as pd
import funcion2 as f2
import datetime as dt

def session_time_total(datos, inicio, fin):
    aux = list()
    tot_sess = 0
    for i in datos:
        date = pd.to_datetime(i[1])
        date = date.date()
        while date >= inicio and date <= fin:
            aux.append(i)
            tot_sess += i[3]
            break
    for i in aux:
        print(i)
    print(tot_sess)


if __name__ == '__main__':
    datos = f2.tiempos_usuario('mleenw')
    inicio = dt.date(2019, 8, 29)
    fin = dt.date(2019, 8, 30)
    session_time_total(datos, inicio, fin)