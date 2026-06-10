"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

def read_data():
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return rows

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214
    """
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return sum(int(r[1]) for r in rows)