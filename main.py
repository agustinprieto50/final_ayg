"""
Unimos todo
"""
from file_manager import open_excel
from funcion2 import tiempos_usuario
from users import list_users
from sess_time_total import session_time_total

# TODO: Volcar la lista de la julia en excel


if __name__ == "__main__":
    data = open_excel("acts-user.xlsx")
    usuarios = list_users(data)
    # Mostrar usuarios
    print("========= LISTA DE USUARIOS =========")
    for i in usuarios:
        if i == "nan" or i == "Timestamp":
            continue
        print(f"\t{i}")
    print("=====================================\n")
    #========= INPUT user =========
    user = input("\nSeleccione un usuario: ")
    tiempo_usuario = tiempos_usuario(user)

    # ======== INPUT rango =========
    fecha_inicio = input("\nIngrese la fecha de inicio: ")
    fecha_final = input("\nIngrese la fecha final: ")

    rango = session_time_total(tiempo_usuario, fecha_inicio, fecha_final)
    print("\nEl tiempo total de sesion fue de:")
    print(f"\t{rango} segundos")
