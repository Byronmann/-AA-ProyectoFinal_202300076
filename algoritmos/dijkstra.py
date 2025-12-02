"""
algoritmos/dijkstra.py

Implementación del algoritmo de Dijkstra para rutas más cortas
desde un nodo origen hacia todos los demás nodos.

Este archivo cumple con:
- Docstrings PEP-257
- Complejidad teórica
- Modularidad
"""

from typing import Dict, List, Tuple
import heapq

# grafo[u] = lista de (v, peso)
Grafo = Dict[str, List[Tuple[str, float]]]


def dijkstra(grafo: Grafo, origen: str):
    """
    Ejecuta el algoritmo de Dijkstra.

    :param grafo: Diccionario de adyacencia.
    :param origen: Nodo origen desde el cual calcular distancias.
    :return:
        distancias -> dict {nodo: costo}
        predecesores -> dict {nodo: nodo_anterior}

    Complejidad:
        O((V + E) log V) usando heapq.
    """

    # Inicialización
    dist = {nodo: float("inf") for nodo in grafo}
    dist[origen] = 0

    pre = {nodo: None for nodo in grafo}

    pq = [(0, origen)]  # (costo, nodo)

    while pq:
        costo_actual, u = heapq.heappop(pq)

        if costo_actual > dist[u]:
            continue

        for v, peso in grafo[u]:
            nuevo_costo = costo_actual + peso
            if nuevo_costo < dist[v]:
                dist[v] = nuevo_costo
                pre[v] = u
                heapq.heappush(pq, (nuevo_costo, v))

    return dist, pre


def reconstruir_ruta(predecesores, destino):
    """
    Reconstruye la ruta desde el origen hacia el destino
    usando el diccionario de predecesores.

    :param predecesores: dict {nodo: nodo_anterior}
    :param destino: nodo final
    :return: lista con la ruta ordenada
    """
    ruta = []
    actual = destino

    while actual is not None:
        ruta.append(actual)
        actual = predecesores[actual]

    ruta.reverse()
    return ruta
