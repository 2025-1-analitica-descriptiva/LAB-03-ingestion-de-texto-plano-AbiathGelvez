"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


import pandas as pd
import re

def pregunta_01():
    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    data = []
    current = []

    for line in lines[4:]:
        if line.strip() == "":
            continue

        if re.match(r"^\s+\d+\s+\d+\s+\d+,\d+\s", line):
            if current:
                data.append(current)
            current = [line.strip()]
        else:
            current.append(line.strip())

    if current:
        data.append(current)

    registros = []
    for grupo in data:
        texto = " ".join(grupo)
        match = re.match(
            r"^\s*(\d+)\s+(\d+)\s+(\d+,\d+)\s+(.*)$", texto)
        if match:
            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(",", "."))
            palabras = match.group(4).replace("  ", " ")
            palabras = re.sub(r"\s+", " ", palabras).strip().strip(".").lstrip("%").strip()
            registros.append((cluster, cantidad, porcentaje, palabras))

    df = pd.DataFrame(registros, columns=[
        "cluster",
        "cantidad_de_palabras_clave",
        "porcentaje_de_palabras_clave",
        "principales_palabras_clave"
    ])
    return df
