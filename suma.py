# pylint: disable=consider-using-enumerate
"""
SUMA Y RESTA DE MATRICES
"""

def validar_dimenciones(a,b):
    """
    Esta función recibe dos matrices y valida que sus dimenciones coincidan
    
    Parámetros:
    A (matriz) = Primera matriz a validar
    b (matriz) = Segunda matriz a validar

    Retorna:
    booleano: True o False
    """

    filasa = len(a)
    columnasa = len(a[0])

    filasb = len(b)
    columnasb = len(b[0])

    if filasa == filasb and columnasa == columnasb:
        return True
    else:
        return False

def sumar_matrices(a,b):
    """
    Esta función recibe dos matrices y valida que sus dimenciones coincidan
    
    Parámetros:
    a (matriz) = Primera matriz a validar
    b (matriz) = Segunda matriz a validar

    Retorna:
    booleano: True o False
    """
    dimensionador = validar_dimenciones(a,b)

    if dimensionador is True:
        c = []
        for i in range(len(a)):
            fila = []
            for j in range(len(a[i])):
                fila.append(a[i][j] + b[i][j])
            c.append(fila)
        return c
    else:
        return dimensionador


def restar_matrices(a,b):
    """
    Esta función recibe dos matrices y valida que sus dimenciones coincidan
    
    Parámetros:
    a (matriz) = Primera matriz a validar
    b (matriz) = Segunda matriz a validar

    Retorna:
    booleano: True o False
    """
    dimensionador = validar_dimenciones(a,b)
    if dimensionador is True:
        c = []
        for i in range(len(a)):
            fila = []
            for j in range(len(a[i])):
                fila.append(a[i][j] - b[i][j])
            c.append(fila)
        return c
    else:
        return dimensionador
