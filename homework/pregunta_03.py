"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
def read_data():
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return rows

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]
    """
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]

    sumas = {}
    for r in rows:
        letra = r[0]
        val = int(r[1])
        sumas[letra] = sumas.get(letra, 0) + val

    return sorted(sumas.items())