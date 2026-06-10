"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
def read_data():
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]
    return rows

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}
    """
    with open("files/data.csv", "r") as f:
        rows = [line.strip().split('\t') for line in f if line.strip()]

    sumas = {}
    for r in rows:
        letra = r[0]
        total = sum(int(item.split(':')[1]) for item in r[4].split(','))
        sumas[letra] = sumas.get(letra, 0) + total

    return dict(sorted(sumas.items()))