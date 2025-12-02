"""
utils/grafo_loader.py

Funciones para leer grafos no dirigidos y ponderados desde archivos CSV.
Formato esperado del CSV:
origen,destino,peso
A,B,4
A,C,2
...

Todas las aristas se consideran no dirigidas.
"""

import csv
from typing import Dict, List, Tuple

# Tipo para claridad
# grafo[u] = lista de (v, peso)
Grafo = Dict[str, List[Tuple[str, float]]]


def cargar_grafo_desde_csv(ruta_csv: str) -> Grafo:
    """
    Lee un grafo no dirigido y ponderado desde un archivo CSV.

    :param ruta_csv: Ruta al archivo CSV.
    :return: Diccionario de adyacencia {nodo: [(vecino, peso), ...]}.
    Complejidad: O(E), donde E es el número de aristas en el archivo.
    """
    grafo: Grafo = {}

    with open(ruta_csv, mode="r", encoding="utf-8") as f:
        lector = csv.DictReader(f)
        for fila in lector:
            u = fila["origen"].strip()
            v = fila["destino"].strip()
            peso = float(fila["peso"])

            # Agregar u -> v
            if u not in grafo:
                grafo[u] = []
            grafo[u].append((v, peso))

            # Como es NO dirigido, agregar v -> u
            if v not in grafo:
                grafo[v] = []
            grafo[v].append((u, peso))

    return grafo


if __name__ == "__main__":
    # Pequeña prueba rápida
    ruta = "data/grafos/grafo_prim.csv"
    g = cargar_grafo_desde_csv(ruta)
    print("Nodos del grafo:", list(g.keys()))
    for nodo, vecinos in g.items():
        print(f"{nodo} -> {vecinos}")
