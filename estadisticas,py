"""
ESTADISTICAS DE MATRICES
"""

def mayor_elemento(A):
    """
    Retorna el elemento mayor de la matriz.

    Parámetros:
    A (matriz): Matriz de entrada

    Retorna:
    numero: Valor máximo
    """
    mayor = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] > mayor:
                mayor = A[i][j]

    return mayor


def menor_elemento(A):
    """
    Retorna el elemento menor de la matriz.

    Parámetros:
    A (matriz): Matriz de entrada

    Retorna:
    numero: Valor mínimo
    """
    menor = A[0][0]

    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] < menor:
                menor = A[i][j]

    return menor


def promedio_matriz(A):
    """
    Calcula el promedio de todos los elementos.

    Parámetros:
    A (matriz): Matriz de entrada

    Retorna:
    float: Promedio de la matriz
    """
    suma = 0
    cantidad = 0

    for i in range(len(A)):
        for j in range(len(A[i])):
            suma += A[i][j]
            cantidad += 1

    return suma / cantidad


def suma_diagonal(A):
    """
    Suma la diagonal principal de una matriz cuadrada.

    Parámetros:
    A (matriz): Matriz de entrada

    Retorna:
    numero o None
    """

    filas = len(A)
    columnas = len(A[0])

    if filas != columnas:
        return None

    suma = 0

    for i in range(filas):
        suma += A[i][i]

    return suma


if __name__ == '__main__':

    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matriz:")
    for fila in A:
        print(fila)

    print("\nMayor elemento:", mayor_elemento(A))
    print("Menor elemento:", menor_elemento(A))
    print("Promedio:", promedio_matriz(A))
    print("Suma diagonal:", suma_diagonal(A))