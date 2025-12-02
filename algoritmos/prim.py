"""
# Implementación del algoritmo de Prim para el Proyecto Final
algoritmos/prim.py

Implementación del algoritmo de Prim para generar
el Árbol de Expansión Mínima (MST).

Este archivo sigue las reglas del proyecto:
- Docstrings estilo PEP-257
- Complejidad teórica indicada
- Funciones modulares
"""

from typing import Dict, List, Tuple
import heapq

# Tipo de grafo utilizado en el proyecto
# grafo[u] = lista de (v, peso)
Grafo = Dict[str, List[Tuple[str, float]]]


def prim_mst(grafo: Grafo, nodo_inicial: str = None):
    """
    Ejecuta el algoritmo de Prim para construir el MST.

    :param grafo: Diccionario de adyacencia del grafo.
    :param nodo_inicial: Nodo desde donde iniciar (opcional).
                         Si es None, se toma el primer nodo del grafo.
    :return: Tupla (mst, costo_total)
             - mst: Lista de aristas del MST con formato (u, v, peso)
             - costo_total: Suma de los pesos de las aristas del MST.

    Complejidad:
        O(E log V), debido al uso de una cola de prioridad (heapq),
        donde E es el número de aristas y V el número de nodos.
    """
    if not grafo:
        return [], 0.0

    # Elegir nodo inicial si no se especifica
    if nodo_inicial is None:
        nodo_inicial = next(iter(grafo))

    visitados = set()
    mst: List[Tuple[str, str, float]] = []
    costo_total = 0.0

    # Cola de prioridad: (peso, u, v)
    heap: List[Tuple[float, str, str]] = []

    # Marcar nodo inicial como visitado y agregar sus aristas
    visitados.add(nodo_inicial)
    for vecino, peso in grafo[nodo_inicial]:
        heapq.heappush(heap, (peso, nodo_inicial, vecino))

    # Mientras haya aristas por procesar y no hayamos cubierto todos los nodos
    while heap and len(visitados) < len(grafo):
        peso, u, v = heapq.heappop(heap)

        if v in visitados:
            continue  # Evitar ciclos

        # Aceptamos la arista (u, v)
        visitados.add(v)
        mst.append((u, v, peso))
        costo_total += peso

        # Agregamos las aristas salientes de v
        for vecino, peso_vecino in grafo[v]:
            if vecino not in visitados:
                heapq.heappush(heap, (peso_vecino, v, vecino))

    return mst, costo_total
