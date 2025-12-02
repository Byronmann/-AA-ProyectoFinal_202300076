"""
algoritmos/kruskal.py

Implementación del algoritmo de Kruskal para generar
el Árbol de Expansión Mínima (MST).

Este archivo sigue las reglas del proyecto:
- Docstrings estilo PEP-257
- Complejidad teórica indicada
- Funciones modulares
"""

from typing import Dict, List, Tuple

# Tipo de grafo usado en el proyecto
Grafo = Dict[str, List[Tuple[str, float]]]


class UnionFind:
    """
    Estructura Union-Find (Disjoint Set Union - DSU)
    para manejar componentes conectados.

    Complejidad amortizada: casi O(1) por operación.
    """

    def __init__(self, elementos):
        self.padre = {e: e for e in elementos}
        self.rango = {e: 0 for e in elementos}

    def encontrar(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.encontrar(self.padre[x])
        return self.padre[x]

    def unir(self, x, y):
        raiz_x = self.encontrar(x)
        raiz_y = self.encontrar(y)

        if raiz_x == raiz_y:
            return False  # ya están unidos

        # Unión por rango
        if self.rango[raiz_x] < self.rango[raiz_y]:
            self.padre[raiz_x] = raiz_y
        elif self.rango[raiz_x] > self.rango[raiz_y]:
            self.padre[raiz_y] = raiz_x
        else:
            self.padre[raiz_y] = raiz_x
            self.rango[raiz_x] += 1

        return True


def kruskal_mst(grafo: Grafo):
    """
    Ejecuta el algoritmo de Kruskal para generar el MST.

    :param grafo: Diccionario de adyacencia.
    :return: Tupla (mst, costo_total)

    Complejidad:
        O(E log E), dominado por el ordenamiento de aristas.
    """

    # Construir lista de aristas sin duplicados
    aristas = []
    for u, vecinos in grafo.items():
        for v, peso in vecinos:
            if (v, u, peso) not in aristas:
                aristas.append((u, v, peso))

    # Ordenar aristas por peso
    aristas.sort(key=lambda x: x[2])

    # Inicializar Union-Find
    nodos = list(grafo.keys())
    uf = UnionFind(nodos)

    mst = []
    costo_total = 0.0

    for u, v, peso in aristas:
        if uf.unir(u, v):  # Si no forma ciclo
            mst.append((u, v, peso))
            costo_total += peso

        # Si ya tenemos V - 1 aristas, terminar
        if len(mst) == len(nodos) - 1:
            break

    return mst, costo_total
