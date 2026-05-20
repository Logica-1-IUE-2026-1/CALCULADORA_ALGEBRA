"""
MENU PRINCIPAL - CALCULADORA DE ALGEBRA LINEAL
"""

import logging
import suma
import estadisticas
import normalizacion
import transpuesta


# CONFIGURACION DEL LOGGING
logging.basicConfig(
    filename="main-data.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def ingresar_matriz(filas, columnas, nombre):
    """
    Solicita una matriz al usuario.
    """

    logging.info("Ingresando matriz %s", nombre)

    matriz = []

    for i in range(filas):

        fila = []

        for j in range(columnas):

            while True:

                try:

                    valor = float(
                        input(f"{nombre}[{i}][{j}]: ")
                    )

                    fila.append(valor)

                    break

                except ValueError:

                    logging.error(
                        "Valor invalido en %s[%s][%s]",
                        nombre,
                        i,
                        j
                    )

                    print(
                        "Error: Debe ingresar un numero valido."
                    )

        matriz.append(fila)

    logging.info(
        "Matriz %s ingresada correctamente",
        nombre
    )

    return matriz


def mostrar_matriz(A, titulo):
    """
    Muestra una matriz organizada.
    """

    print(f"\n{titulo}")

    for fila in A:

        for elemento in fila:

            print(f"{elemento:10.2f}", end=" ")

        print()


def mostrar_vector(v, titulo):
    """
    Muestra un vector.
    """

    print(f"\n{titulo}")

    for i in range(len(v)):

        print(f"[{i}] = {v[i]}")


def pedir_entero(mensaje):
    """
    Solicita un numero entero valido.
    """

    while True:

        try:

            valor = int(input(mensaje))

            if valor <= 0:

                print(
                    "Error: Debe ingresar un numero mayor que 0."
                )

                continue

            return valor

        except ValueError:

            logging.error(
                "El usuario ingreso un entero invalido"
            )

            print(
                "Error: Debe ingresar un numero entero."
            )


def pedir_float(mensaje):
    """
    Solicita un numero decimal valido.
    """

    while True:

        try:

            return float(input(mensaje))

        except ValueError:

            logging.error(
                "El usuario ingreso un numero decimal invalido"
            )

            print(
                "Error: Debe ingresar un numero valido."
            )


def main():

    logging.info("Programa iniciado")

    while True:

        print("\n===== CALCULADORA DE ALGEBRA LINEAL =====")
        print("1. Suma y resta de matrices")
        print("2. Transpuesta y simetría")
        print("3. Estadísticas")
        print("4. Normalización y escalar")
        print("5. Salir")

        opcion = input("\nSeleccione una opción: ")

        logging.info(
            "Opcion seleccionada: %s",
            opcion
        )

        try:

            # OPCION 1
            if opcion == "1":

                filas = pedir_entero(
                    "Número de filas: "
                )

                columnas = pedir_entero(
                    "Número de columnas: "
                )

                A = ingresar_matriz(
                    filas,
                    columnas,
                    "A"
                )

                B = ingresar_matriz(
                    filas,
                    columnas,
                    "B"
                )

                suma_resultado = suma.sumar_matrices(
                    A,
                    B
                )

                resta_resultado = suma.restar_matrices(
                    A,
                    B
                )

                mostrar_matriz(
                    A,
                    "Matriz A"
                )

                mostrar_matriz(
                    B,
                    "Matriz B"
                )

                mostrar_matriz(
                    suma_resultado,
                    "A + B"
                )

                mostrar_matriz(
                    resta_resultado,
                    "A - B"
                )

                logging.info(
                    "Operacion suma/resta completada"
                )

            # OPCION 2
            elif opcion == "2":

                filas = pedir_entero(
                    "Número de filas: "
                )

                columnas = pedir_entero(
                    "Número de columnas: "
                )

                A = ingresar_matriz(
                    filas,
                    columnas,
                    "A"
                )

                mostrar_matriz(
                    A,
                    "Matriz original"
                )

                T = transpuesta.transponer(A)

                mostrar_matriz(
                    T,
                    "Matriz transpuesta"
                )

                print(
                    "\n¿Es cuadrada?:",
                    transpuesta.es_cuadrada(A)
                )

                print(
                    "¿Es simétrica?:",
                    transpuesta.es_simetrica(A)
                )

                logging.info(
                    "Operacion transpuesta completada"
                )

            # OPCION 3
            elif opcion == "3":

                filas = pedir_entero(
                    "Número de filas: "
                )

                columnas = pedir_entero(
                    "Número de columnas: "
                )

                A = ingresar_matriz(
                    filas,
                    columnas,
                    "A"
                )

                mostrar_matriz(
                    A,
                    "Matriz"
                )

                print(
                    "\nMayor elemento:",
                    estadisticas.mayor_elemento(A)
                )

                print(
                    "Menor elemento:",
                    estadisticas.menor_elemento(A)
                )

                print(
                    "Promedio:",
                    estadisticas.promedio_matriz(A)
                )

                diagonal = estadisticas.suma_diagonal(A)

                if diagonal is None:

                    print(
                        "Suma diagonal: "
                        "La matriz no es cuadrada"
                    )

                    logging.warning(
                        "Matriz no cuadrada para diagonal"
                    )

                else:

                    print(
                        "Suma diagonal:",
                        diagonal
                    )

                logging.info(
                    "Operacion estadisticas completada"
                )

            # OPCION 4
            elif opcion == "4":

                filas = pedir_entero(
                    "Número de filas: "
                )

                columnas = pedir_entero(
                    "Número de columnas: "
                )

                A = ingresar_matriz(
                    filas,
                    columnas,
                    "A"
                )

                k = pedir_float(
                    "Ingrese el escalar k: "
                )

                mostrar_matriz(
                    A,
                    "Matriz original"
                )

                escalada = normalizacion.escalar_matriz(
                    A,
                    k
                )

                mostrar_matriz(
                    escalada,
                    f"Matriz escalada por {k}"
                )

                sf = normalizacion.suma_filas(A)

                mostrar_vector(
                    sf,
                    "Suma de filas"
                )

                sc = normalizacion.suma_columnas(A)

                mostrar_vector(
                    sc,
                    "Suma de columnas"
                )

                normalizada = (
                    normalizacion.normalizar_fila(A)
                )

                mostrar_matriz(
                    normalizada,
                    "Matriz normalizada"
                )

                logging.info(
                    "Operacion normalizacion completada"
                )

            # OPCION 5
            elif opcion == "5":

                logging.info(
                    "Programa finalizado por el usuario"
                )

                print("\nPrograma finalizado.")

                break

            else:

                logging.warning(
                    "Opcion invalida ingresada"
                )

                print(
                    "\nOpción inválida. "
                    "Intente nuevamente."
                )

        except Exception as e:

            logging.critical(
                "Error inesperado: %s",
                e
            )

            print(
                "\nOcurrió un error inesperado."
            )


if __name__ == '__main__':
    main()