"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
def read_data():
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return rows

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]
    """
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]

    resultado = []
    for r in rows:
        letra = r[0]
        col4 = len(r[3].split(','))   # cantidad de elementos columna 4
        col5 = len(r[4].split(','))   # cantidad de elementos columna 5
        resultado.append((letra, col4, col5))

    return resultado