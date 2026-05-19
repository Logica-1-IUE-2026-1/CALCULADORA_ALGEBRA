"""
    Este archivo contiene 3 funciones para determinar:
    si una matriz es cuadra, transponerla y validar si es simetrica
"""
import logging

# Configuración básica de los logs para mostrar mensajes en consola
logging.basicConfig(
    filename="Mylog.log",
    level=logging.DEBUG, #Nivel del logs, el debug es el mas bajo
    format='%(asctime)s - %(levelname)s - %(message)s', #Formato del mensaje
    datefmt='%Y-%m-%d %H:%M:%S' #Formato de la fecha y hora
)


def es_cuadrada(A):
    """
    Determina si una matriz es cuadrada (mismo número de filas y columnas).
    Es totalmente independiente y solo valida esta propiedad geométrica.
    
    Parámetros:
    A (list): Matriz representada como una lista de listas.
    
    Retorna:
    bool: True si es cuadrada, False en caso contrario.
    """
    try:
        num_filas = len(A)
        num_columnas = len(A[0])

        assert num_columnas > 0

    except (IndexError, TypeError, AssertionError):
        logging.warning("La matriz está vacía, no es válida o no tiene un formato correcto.")
        return False
        
    
    for i in range(num_filas):
        fila = A[i]
        try:
            assert len(fila) == num_columnas
        except AssertionError:
            logging.error(f"La fila {i} no tiene el mismo tamaño que las demás.")
            return False

    try:
        # Verificación final de la propiedad cuadrada
        assert num_filas == num_columnas
        logging.info(f"Evaluando es_cuadrada: Dimensiones {num_filas}x{num_columnas} -> True")
        return True
    except AssertionError:
        logging.info(f"Evaluando es_cuadrada: Dimensiones {num_filas}x{num_columnas} -> False")
        return False


def transponer(A):
    """
    Calcula la transpuesta de una matriz
    
    Parámetros:
    A (list): Matriz representada como una lista de listas.
    
    Retorna:
    list: Nueva matriz transpuesta, o lista vacía si los datos son inválidos.
    """
    try:
        num_filas = len(A)
        num_columnas = len(A[0])
        assert num_columnas > 0
    except (IndexError, TypeError, AssertionError):
        logging.error("No se puede transponer una matriz vacía o con formato inválido.")
        return []
        
    logging.info(f"Calculando la transpuesta de una matriz de {num_filas}x{num_columnas}...")
    
    # Creamos la matriz destino T invirtiendo filas y columnas de forma dinámica (n x m)
    # Cada fila de T tendrá un tamaño igual al número de filas de A
    T = [[None for _ in range(num_filas)] for _ in range(num_columnas)]
    
    # El algoritmo recorre la matriz original celda por celda de manera segura
    for i in range(num_filas):
        for j in range(num_columnas):
            try:
                T[j][i] = A[i][j]
            except IndexError:
                # Protección por si una fila interna viniera mocha o incompleta
                logging.error(f"Error de índice al intentar acceder a A[{i}][{j}]. Matriz mal formada.")
                return []
            
    return T


def es_simetrica(A):
    """
    Determina si una matriz es simétrica utilizando las otras funciones.
    Sigue las consideraciones del negocio de manera estricta y limpia.
    
    Parámetros:
    A (list): Matriz representada como una lista de listas.
    
    Retorna:
    bool: True si la matriz es simétrica, False en caso contrario.
    """
    logging.info("Iniciando validación de simetría...")
    
    try:
        # Consideración 1: Debe llamar internamente a es_cuadrada.
        # Si devuelve False, el assert falla y corta el flujo de inmediato al except.
        assert es_cuadrada(A) == True
        
        # Consideración 2: Llama internamente a transponer 
        A_transpuesta = transponer(A)
        
        # Consideración 3: Compara la matriz con su propia transpuesta
        assert A == A_transpuesta
        
        logging.info("¡Éxito! La matriz es cuadrada y perfectamente simétrica.")
        return True
        
    except AssertionError:
        logging.warning("La validación falló: La matriz no es" \
        " cuadrada o no coincide con su transpuesta.")
        return False

