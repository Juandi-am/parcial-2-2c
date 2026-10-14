# Registro mensual de vehiculos de un taller usando una MATRIZ.
#
# Matriz de 30 filas (una por vehiculo) x 6 columnas:
#   0: Placa | 1: Propietario | 2: Celular | 3: Dia ingreso | 4: Dia salida | 5: Dias reparacion
# Las columnas 4 y 5 quedan vacias ("") hasta que se registra la salida.

MAX_VEHICULOS = 30
COLUMNAS = 6
PLACA, PROPIETARIO, CELULAR, DIA_INGRESO, DIA_SALIDA, DIAS_REPARACION = range(COLUMNAS)

matriz = [["" for _ in range(COLUMNAS)] for _ in range(MAX_VEHICULOS)]
cantidad = 0  # vehiculos registrados hasta el momento


def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  El dato no puede estar vacio.")


def leer_celular():
    while True:
        celular = input("Numero de celular: ").strip()
        if celular.isdigit() and 7 <= len(celular) <= 15:
            return celular
        print("  Ingrese solo digitos (entre 7 y 15).")


def leer_dia(mensaje, minimo=1):
    while True:
        dato = input(mensaje).strip()
        if dato.isdigit() and minimo <= int(dato) <= 31:
            return int(dato)
        print(f"  Ingrese un dia valido entre {minimo} y 31.")


def buscar_placa(placa):
    for i in range(cantidad):
        if matriz[i][PLACA] == placa:
            return i
    return -1


def registrar_ingreso():
    global cantidad
    if cantidad >= MAX_VEHICULOS:
        print(f"\nNo se pueden registrar mas vehiculos (maximo {MAX_VEHICULOS}).")
        return

    print(f"\n--- Ingreso del vehiculo {cantidad + 1} de {MAX_VEHICULOS} ---")
    placa = leer_texto("Placa del vehiculo: ").upper()
    if buscar_placa(placa) != -1:
        print("  Ya existe un vehiculo registrado con esa placa este mes.")
        return

    matriz[cantidad][PLACA] = placa
    matriz[cantidad][PROPIETARIO] = leer_texto("Nombre del propietario: ")
    matriz[cantidad][CELULAR] = leer_celular()
    matriz[cantidad][DIA_INGRESO] = leer_dia("Dia del mes en que ingreso (1-31): ")
    cantidad += 1
    print("Vehiculo registrado correctamente.")


def registrar_salida():
    if cantidad == 0:
        print("\nNo hay vehiculos registrados.")
        return

    placa = leer_texto("\nPlaca del vehiculo que sale: ").upper()
    fila = buscar_placa(placa)
    if fila == -1:
        print("  No se encontro un vehiculo con esa placa.")
        return
    if matriz[fila][DIA_SALIDA] != "":
        print(f"  Ese vehiculo ya fue entregado el dia {matriz[fila][DIA_SALIDA]}.")
        return

    ingreso = matriz[fila][DIA_INGRESO]
    salida = leer_dia(f"Dia de salida ({ingreso}-31): ", ingreso)
    matriz[fila][DIA_SALIDA] = salida
    matriz[fila][DIAS_REPARACION] = salida - ingreso
    print(f"Salida registrada. La reparacion demoro {salida - ingreso} dia(s).")


def reporte_terminados():
    print("\n=========== VEHICULOS TERMINADOS ===========")
    print(f"{'Placa':<10}{'Propietario':<22}{'Ingreso':>8}{'Salida':>8}{'Dias':>6}")
    terminados = 0
    for i in range(cantidad):
        if matriz[i][DIA_SALIDA] != "":
            terminados += 1
            print(f"{matriz[i][PLACA]:<10}{matriz[i][PROPIETARIO]:<22}"
                  f"{matriz[i][DIA_INGRESO]:>8}{matriz[i][DIA_SALIDA]:>8}"
                  f"{matriz[i][DIAS_REPARACION]:>6}")
    if terminados == 0:
        print("(Ningun vehiculo ha sido terminado)")
    print(f"Total de vehiculos terminados: {terminados}")


def reporte_todos():
    print("\n======== VEHICULOS INGRESADOS EN EL MES ========")
    if cantidad == 0:
        print("(No hay vehiculos registrados)")
        return
    print(f"{'#':<4}{'Placa':<10}{'Propietario':<22}{'Celular':<15}")
    for i in range(cantidad):
        print(f"{i + 1:<4}{matriz[i][PLACA]:<10}{matriz[i][PROPIETARIO]:<22}"
              f"{matriz[i][CELULAR]:<15}")
    print(f"Total de vehiculos ingresados: {cantidad}")


def main():
    while True:
        print("\n========== TALLER - MENU PRINCIPAL ==========")
        print("1. Registrar ingreso de vehiculo")
        print("2. Registrar salida de vehiculo")
        print("3. Reporte de vehiculos terminados")
        print("4. Reporte de todos los vehiculos del mes")
        print("5. Salir")
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_ingreso()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            reporte_terminados()
        elif opcion == "4":
            reporte_todos()
        elif opcion == "5":
            print("Aplicacion cerrada. Hasta luego!")
            break
        else:
            print("Opcion no valida, intente de nuevo.")


if __name__ == "__main__":
    main()
