"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

    """
    base_dir = __file__.replace("\\", "/").rsplit("/", 1)[0]
    data_path = base_dir + "/../files/input/data.csv"
    sums = {}
    with open(data_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            value = int(parts[1])
            letters = parts[3].split(",") if parts[3] else []
            for letter in letters:
                sums[letter] = sums.get(letter, 0) + value
    return dict(sorted(sums.items()))
