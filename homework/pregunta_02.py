"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
def read_data():
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return rows

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]

    conteo = {}
    for r in rows:
        letra = r[0]
        conteo[letra] = conteo.get(letra, 0) + 1

    return sorted(conteo.items())