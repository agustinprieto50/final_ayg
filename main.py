from file_manager import open_excel
from funcion2 import tiempos_usuario
from users import list_users
from sess_time_total import session_time_total
import pandas as pd
import cmd


# TODO: Volcar en excel [user, f_inicio, f_fin, TST]
# TODO: Validar toma de fecha


if __name__ == "__main__":
    data = open_excel("acts-user.xlsx")
    usuarios = list_users(data)
    # Mostrar usuarios
    print(" LISTA DE USUARIOS ".center(80, "="))
    cli = cmd.Cmd()
    cli.columnize(usuarios, displaywidth=80)
    print("".center(80, "="))

    #========= INPUT user =========
    user = input("\nSeleccione un usuario: ")
    tiempo_usuario = tiempos_usuario(user)

    # ======== INPUT rango =========
    fecha_inicio = input("\nIngrese la fecha de inicio: ")
    fecha_final = input("\nIngrese la fecha final: ")

    rango = session_time_total(tiempo_usuario, fecha_inicio, fecha_final)
    print("\nEl tiempo total de sesion fue de:")
    print(f"\t{rango} segundos")
