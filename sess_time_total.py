import pandas as pd
import datetime as dt

# Pasar inicio y fin como una tupla (año, mes, dia)
def session_time_total(datos, inicio, fin):
    inicio = dt.date(inicio)
    fin = dt.date(fin)
    aux = list()
    tot_sess = 0
    for i in datos:
        date = pd.to_datetime(i[1])
        date = date.date()
        while date >= inicio and date <= fin:
            aux.append(i)
            tot_sess += i[3]
            break
    return(tot_sess)
