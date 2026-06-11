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
    base_dir = __file__.replace("\\", "/").rsplit("/", 1)[0]
    data_path = base_dir + "/../files/input/data.csv"
    sums = {}
    with open(data_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            letter = parts[0]
            total = 0
            entries = parts[4].split(",") if parts[4] else []
            for entry in entries:
                if not entry:
                    continue
                total += int(entry.split(":")[1])
            sums[letter] = sums.get(letter, 0) + total
    return sums
