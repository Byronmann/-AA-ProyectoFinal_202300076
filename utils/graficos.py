"""
utils/graficos.py

Funciones para generar imágenes PNG de los grafos
y sus árboles de expansión mínima (MST).

Para dibujar se utiliza networkx + matplotlib.
Si las librerías no están instaladas, se muestra un mensaje
amigable y el programa no se detiene.
"""

from typing import Dict, List, Tuple

Grafo = Dict[str, List[Tuple[str, float]]]


def dibujar_grafo_con_mst(grafo: Grafo,
                          mst: List[Tuple[str, str, float]],
                          nombre_archivo: str = "prim_mst.png") -> None:
    """
    Dibuja un grafo no dirigido resaltando las aristas del MST.

    :param grafo: Diccionario de adyacencia del grafo.
    :param mst: Lista de aristas del MST (u, v, peso).
    :param nombre_archivo: Nombre del archivo PNG de salida.
                           Para este proyecto debe ser 'prim_mst.png'.

    Complejidad:
        La construcción del grafo y dibujo es aproximadamente O(V + E).
    """
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        print(" No se pudieron importar networkx/matplotlib.")
        print("   No se generará la imagen PNG, pero el algoritmo sí se ejecutó.")
        return

    G = nx.Graph()

    # Agregar nodos y aristas del grafo completo
    for u, vecinos in grafo.items():
        G.add_node(u)
        for v, peso in vecinos:
            # Evitar duplicar aristas en grafo no dirigido
            if G.has_edge(u, v):
                continue
            G.add_edge(u, v, weight=peso)

    # Normalizar aristas del MST (para comparar sin orden)
    mst_normalizadas = set()
    for u, v, _peso in mst:
        if u <= v:
            mst_normalizadas.add((u, v))
        else:
            mst_normalizadas.add((v, u))

    # Preparar estilos
    pos = nx.spring_layout(G, seed=42)  # Layout fijo para que no cambie mucho

    # Colores y grosores: MST en grueso, resto tenue
    edge_colors = []
    edge_widths = []
    for u, v in G.edges():
        par = (u, v) if u <= v else (v, u)
        if par in mst_normalizadas:
            edge_colors.append("red")
            edge_widths.append(2.5)
        else:
            edge_colors.append("lightgray")
            edge_widths.append(1.0)

    pesos = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(6, 4))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        font_size=10,
        edge_color=edge_colors,
        width=edge_widths,
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=8)

    plt.title("Árbol de Expansión Mínima - Prim")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"Imagen PNG generada: {nombre_archivo}")


def dibujar_rutas_dijkstra(grafo, distancias, pre, origen,
                           nombre_archivo="dijkstra_paths.png"):
    """
    Dibuja el grafo resaltando las rutas más cortas desde un origen.

    Complejidad:
        O(V + E) para construir el dibujo.
    """
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        print("⚠️ No se pudieron importar networkx/matplotlib.")
        return

    G = nx.Graph()

    # Construir grafo
    for u, vecinos in grafo.items():
        for v, peso in vecinos:
            if not G.has_edge(u, v):
                G.add_edge(u, v, weight=peso)

    pos = nx.spring_layout(G, seed=42)

    # Rutas: marcar aristas que pertenecen al árbol de caminos mínimos
    aristas_resaltadas = set()

    for nodo in grafo:
        actual = nodo
        while pre[actual] is not None:
            u = pre[actual]
            par = tuple(sorted((u, actual)))
            aristas_resaltadas.add(par)
            actual = u

    # Estilo
    edge_colors = []
    edge_widths = []
    for (u, v) in G.edges():
        if tuple(sorted((u, v))) in aristas_resaltadas:
            edge_colors.append("blue")
            edge_widths.append(2.5)
        else:
            edge_colors.append("lightgray")
            edge_widths.append(1.0)

    pesos = nx.get_edge_attributes(G, "weight")

    plt.figure(figsize=(6, 4))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=700,
        font_size=10,
        edge_color=edge_colors,
        width=edge_widths,
    )
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=8)

    plt.title(f"Rutas más cortas desde {origen} - Dijkstra")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f" Imagen PNG generada: {nombre_archivo}")


def dibujar_arbol_huffman(raiz, nombre_archivo="huffman_tree.png"):
    """
    Genera una imagen PNG del árbol de Huffman usando networkx.

    Complejidad: O(n)
    """
    try:
        import networkx as nx
        import matplotlib.pyplot as plt
    except ImportError:
        print(" No se pudieron importar networkx/matplotlib.")
        print("   No se generará la imagen del árbol Huffman.")
        return

    G = nx.DiGraph()

    # Construir grafo recursivamente
    def agregar_nodos(nodo, nombre):
        if nodo is None:
            return

        etiqueta = (
            f"{repr(nodo.caracter)}\n({nodo.frecuencia})"
            if nodo.caracter is not None
            else f"* ({nodo.frecuencia})"
        )
        G.add_node(nombre, label=etiqueta)

        if nodo.izq:
            izq_nombre = nombre + "0"
            G.add_edge(nombre, izq_nombre)
            agregar_nodos(nodo.izq, izq_nombre)

        if nodo.der:
            der_nombre = nombre + "1"
            G.add_edge(nombre, der_nombre)
            agregar_nodos(nodo.der, der_nombre)

    agregar_nodos(raiz, "root")

    # Usamos siempre spring_layout para evitar depender de pygraphviz
    pos = nx.spring_layout(G, seed=42)

    etiquetas = nx.get_node_attributes(G, "label")

    plt.figure(figsize=(10, 8))
    nx.draw(
        G,
        pos,
        labels=etiquetas,
        node_size=1500,
        font_size=8,
        arrows=False,
        node_color="#E5E5FF",
        linewidths=1,
    )

    plt.title("Árbol de Huffman")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f" Imagen generada: {nombre_archivo}")

def dibujar_frecuencias_huffman(frecuencias, nombre_archivo="huffman_freq.png"):
    """
    Genera una imagen PNG de barras con las frecuencias de cada caracter.

    Complejidad: O(n)
    """
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        print("No se pudo importar matplotlib.")
        print("   No se generará la imagen de frecuencias.")
        return

    caracteres = list(frecuencias.keys())
    valores = list(frecuencias.values())

    plt.figure(figsize=(12, 4))
    plt.bar(caracteres, valores)
    plt.title("Frecuencias de Huffman")
    plt.xlabel("Caracter")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.savefig(nombre_archivo)
    plt.close()

    print(f"✅ Imagen generada: {nombre_archivo}")
