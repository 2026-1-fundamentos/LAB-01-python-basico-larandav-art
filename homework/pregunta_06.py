"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

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
            entries = parts[4].split(",")
            for entry in entries:
                if not entry:
                    continue
                key, value = entry.split(":")
                value = int(value)
                if key not in bounds:
                    bounds[key] = [value, value]
                else:
                    if value < bounds[key][0]:
                        bounds[key][0] = value
                    if value > bounds[key][1]:
                        bounds[key][1] = value
    result = []
    for key in sorted(bounds.keys()):
        minimum, maximum = bounds[key][0], bounds[key][1]
        result.append((key, minimum, maximum))
    return result
