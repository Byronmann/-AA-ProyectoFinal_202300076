"""
algoritmos/huffman.py

Implementación del algoritmo de Huffman para codificación óptima.

Incluye:
- Conteo de frecuencias
- Construcción de árbol
- Generación de códigos
- Representación textual del árbol

Cumple con:
- Docstrings estilo PEP-257
- Complejidad teórica
"""

from typing import Dict, Tuple
import heapq


class NodoHuffman:
    """
    Nodo del árbol de Huffman.
    """
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None

    # Para que heapq pueda comparar nodos
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def contar_frecuencias(texto: str) -> Dict[str, int]:
    """
    Cuenta las frecuencias de cada caracter.

    Complejidad: O(n)
    """
    frec = {}
    for c in texto:
        frec[c] = frec.get(c, 0) + 1
    return frec


def construir_arbol(frecuencias: Dict[str, int]) -> NodoHuffman:
    """
    Construye el árbol de Huffman usando una min-heap.

    Complejidad:
        O(n log n), donde n = número de símbolos.
    """
    heap = []

    # Crear nodos iniciales
    for caracter, frec in frecuencias.items():
        heapq.heappush(heap, NodoHuffman(caracter, frec))

    # Unir nodos hasta quedar solo uno (la raíz)
    while len(heap) > 1:
        nodo1 = heapq.heappop(heap)
        nodo2 = heapq.heappop(heap)

        nuevo = NodoHuffman(None, nodo1.frecuencia + nodo2.frecuencia)
        nuevo.izq = nodo1
        nuevo.der = nodo2

        heapq.heappush(heap, nuevo)

    return heap[0]  # raíz del árbol


def generar_codigos(raiz: NodoHuffman) -> Dict[str, str]:
    """
    Genera códigos Huffman recorriendo el árbol.

    Complejidad: O(n)
    """
    codigos = {}

    def _recorrer(nodo, codigo_actual):
        if nodo is None:
            return

        if nodo.caracter is not None:
            codigos[nodo.caracter] = codigo_actual
            return

        _recorrer(nodo.izq, codigo_actual + "0")
        _recorrer(nodo.der, codigo_actual + "1")

    _recorrer(raiz, "")
    return codigos


def representar_arbol(raiz: NodoHuffman, nivel=0) -> str:
    """
    Genera una representación en texto del árbol de Huffman.

    Complejidad: O(n)
    """
    if raiz is None:
        return ""

    resultado = ""
    if raiz.der:
        resultado += representar_arbol(raiz.der, nivel + 1)

    resultado += "    " * nivel
    if raiz.caracter is None:
        resultado += f"* ({raiz.frecuencia})\n"
    else:
        resultado += f"{repr(raiz.caracter)} ({raiz.frecuencia})\n"

    if raiz.izq:
        resultado += representar_arbol(raiz.izq, nivel + 1)

    return resultado
