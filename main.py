from file_manager import open_excel, read_csv, dump_csv
from users import list_users, tiempos_usuario
from sess_time_total import session_time_total, validate_fecha
import cmd
from datetime import date
from os import system


if __name__ == "__main__":
    data = open_excel("acts-user.xlsx")
    usuarios = list_users(data)

    while True:
        # Limpiar pantalla
        system("clear")

        # Mostrar usuarios
        print(" LISTA DE USUARIOS ".center(80, "="))
        cli = cmd.Cmd()
        cli.columnize(usuarios, displaywidth=80)
        print("".center(80, "="))

        # ========= INPUT user =========
        user = input("\nSeleccione un usuario: ")

        # Obtener todos los registros asociados a ese usuario
        tiempo_usuario = tiempos_usuario(user)

        # ======== INPUT rango de fechas =========
        today = date.today().strftime("%Y-%m-%d")

        # Ingresar fecha de inicio y validar
        fecha_inicio = input(f"\nIngrese la fecha de inicio en formato YYYY-MM-DD [default={today}]: ")
        fecha_inicio = validate_fecha(fecha_inicio)

        # Ingresar fecha final y validar
        fecha_final = input(f"\nIngrese la fecha final YYYY-MM-DD [default={today}]: ")
        fecha_final = validate_fecha(fecha_final)

        # Obtener el TST para el usuario segun el rango de fecha ingresado
        rango = session_time_total(tiempo_usuario, fecha_inicio, fecha_final)
        
        # Muestra el resultado formateado
        print("")
        print(" RESULTADO DE LA BUSQUEDA ".center(80, "="))
        print(f"Usuario: {user}")
        print(f"Fecha de inicio: {fecha_inicio}")
        print(f"Fecha final: {fecha_final}")
        print(f"TST [segundos]: {rango}")

        # Eleccion si se desa guardar la busqueda realizada
        choice = input("\nDesea guardar la busqueda en formato .csv [Y/N]? ").upper()
        if choice.startswith(("Y", "S")):
            dump_csv("user_TST.csv", user, fecha_inicio, fecha_final, rango)

        # Eleccion si se desea realizar una nueva busqueda
        choice = input("\nDesea realizar otra busqueda [Y/N]? ").upper()
        if choice.startswith("N"):
            break


    exit(0)


