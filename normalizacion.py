"""Normalizacion y Escalar"""

def escalar_matriz(A, k):
    """
    Esta función multiplica todos los elementos por el escalar k y retorna una nueva matriz.

    Parámetros:
    A: Matriz de entrada.
    k (float): Número.
    
    Retorna:
    B: Matriz de salida.
    """
    return [[elemento * k for elemento in fila] for fila in A]

def suma_filas(A):
    """
    Esta función suma los elementos de cada fila y retorna un vector (lista).
 
    Parámetros:
    A: Matriz de entrada.
 
    Retorna:
    lista: Vector con la suma de cada fila.
    """
    lista = []
    for i in range(len(A)):
        total = 0
        for j in range(len(A[i])):
            total += A[i][j]
        lista.append(total)
    return lista

def suma_columnas(A):
    """
    Esta función suma los elementos de cada columna y retorna un vector (lista).
 
    Parámetros:
    A: Matriz de entrada.
 
    Retorna:
    resultado: Vector con la suma de cada columna.
    """
    num_columnas = len(A[0])
    lista = [0] * num_columnas
    for i in range(len(A)):
        for j in range(len(A[i])):
            lista[j] += A[i][j]
    return lista

def normalizar_fila(A):
    """
    Función que divide cada elemento entre la suma de su fila. 
    Si la suma es 0, la fila queda en ceros. 
    Retorna una nueva matriz sin modificar la original.
    
    Parámetros:
    A: Matriz de entrada.
 
    Retorna:
    B: Matriz de salida.
    """
    resultado = []
    for i in range(len(A)):
        total = 0

        # Sumar fila
        for j in range(len(A[i])):
            total += A[i][j]

        # Normalizar
        if total == 0:
            nueva_fila = [0] * len(A[i])
        else:
            nueva_fila = []
            for j in range(len(A[i])):
                nueva_fila.append(A[i][j] / total)
        resultado.append(nueva_fila)
    return resultado


if __name__ == '__main__':
    exito = True  # bandera para detectar errores

    A = [
        [10, 20, 70],
        [5,  5,  0],
        [0,  0,  0],   # fila con suma 0
        [3,  1,  6],
    ]

    print("Matriz original:")
    for fila in A:
        print(" ", fila)

    # escalar_matriz
    k = 2
    try:
        B = escalar_matriz(A, k)
        print(f"\nescalar_matriz(A, {k}):")
        for fila in B:
            print(" ", fila)
    except Exception as e:
        print(f"Error en escalar_matriz: {e}")
        exito = False

    # suma_filas
    try:
        sf = suma_filas(A)
        print("\nsuma_filas(A):")
        print(" ", sf)
    except Exception as e:
        print(f"Error en suma_filas: {e}")
        exito = False

    # suma_columnas
    try:
        sc = suma_columnas(A)
        print("\nsuma_columnas(A):")
        print(" ", sc)
    except Exception as e:
        print(f"Error en suma_columnas: {e}")
        exito = False

    # normalizar_fila
    try:
        N = normalizar_fila(A)
        print("\nnormalizar_fila(A):")
        for fila in N:
            print(" ", [round(x, 4) for x in fila])
    except Exception as e:
        print(f"Error en normalizar_fila: {e}")
        exito = False

    # Resultado final
    print()
    if exito:
        print("Resultado de la ejecución es exitoso")
    else:
        print("Resultado de la ejecución es fallido")
