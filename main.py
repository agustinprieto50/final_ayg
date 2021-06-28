from file_manager import open_excel, read_csv, dump_csv
from funcion2 import tiempos_usuario
from users import list_users
from sess_time_total import session_time_total, validate_fechas
import cmd


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

    fecha_inicio, fecha_final = validate_fechas(fecha_inicio, fecha_final)

    rango = session_time_total(tiempo_usuario, fecha_inicio, fecha_final)
    print("\nEl tiempo total de sesion fue de:")
    print(f"\t{rango} segundos")

    choice = input("\nDesea guardar la busqueda en formato .csv [Y/N]? ").upper()
    if choice.startswith(("Y", "S")):
        dump_csv("user_TST.csv", user, fecha_inicio, fecha_final, rango)
    exit(0)


