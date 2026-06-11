"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    base_dir = __file__.replace("\\", "/").rsplit("/", 1)[0]
    data_path = base_dir + "/../files/input/data.csv"
    bounds = {}
    with open(data_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            letter = parts[0]
            value = int(parts[1])
            if letter not in bounds:
                bounds[letter] = [value, value]
            else:
                if value < bounds[letter][0]:
                    bounds[letter][0] = value
                if value > bounds[letter][1]:
                    bounds[letter][1] = value
    result = []
    for letter in sorted(bounds.keys()):
        minimum, maximum = bounds[letter][0], bounds[letter][1]
        result.append((letter, maximum, minimum))
    return result
