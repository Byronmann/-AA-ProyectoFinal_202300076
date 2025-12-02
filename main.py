"""
main.py
Proyecto Final - Implementación y Visualización de Algoritmos Avanzados

Menú principal para ejecutar:
- Prim
- Kruskal
- Dijkstra
- Huffman
"""

from utils.grafo_loader import cargar_grafo_desde_csv
from algoritmos.prim import prim_mst
from utils.graficos import dibujar_grafo_con_mst
from algoritmos.kruskal import kruskal_mst
from algoritmos.dijkstra import dijkstra, reconstruir_ruta
from algoritmos.huffman import (
    contar_frecuencias,
    construir_arbol,
    generar_codigos,
    representar_arbol
)




def mostrar_menu():
    print("\n==============================================")
    print("  PROYECTO FINAL: ALGORITMOS AVANZADOS")
    print("==============================================")
    print("1. Ejecutar Prim (Árbol de Expansión Mínima)")
    print("2. Ejecutar Kruskal (Árbol de Expansión Mínima)")
    print("3. Ejecutar Dijkstra (Rutas más cortas)")
    print("4. Ejecutar Huffman (Codificación óptima)")
    print("0. Salir")
    print("==============================================")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("\n[Prim] Ejecutando algoritmo de Prim...")

            ruta = "data/grafos/grafo_prim.csv"
            grafo = cargar_grafo_desde_csv(ruta)

            mst, costo = prim_mst(grafo)

            print("\nÁrbol de Expansión Mínima (MST):")
            for u, v, peso in mst:
                print(f"{u} - {v} (peso: {peso})")
            print(f"Costo total: {costo}")

            # Generar imagen PNG obligatoria
            dibujar_grafo_con_mst(grafo, mst, nombre_archivo="prim_mst.png")

        elif opcion == "2":
            print("\n[Kruskal] Ejecutando algoritmo de Kruskal...")

            ruta = "data/grafos/grafo_prim.csv"
            grafo = cargar_grafo_desde_csv(ruta)

            mst, costo = kruskal_mst(grafo)

            print("\nÁrbol de Expansión Mínima (MST):")
            for u, v, peso in mst:
                print(f"{u} - {v} (peso: {peso})")
            print(f"Costo total: {costo}")

            # Dibujar PNG
            dibujar_grafo_con_mst(grafo, mst, nombre_archivo="kruskal_mst.png")


        elif opcion == "3":
            print("\n[Dijkstra] Ejecutando algoritmo de Dijkstra...")

            ruta = "data/grafos/grafo_prim.csv"
            grafo = cargar_grafo_desde_csv(ruta)

            nodo_origen = input("Ingrese nodo origen (ej. A): ").strip().upper()

            if nodo_origen not in grafo:
                print("El nodo no existe en el grafo.")
                continue

            distancias, predecesores = dijkstra(grafo, nodo_origen)

            print("\nDistancias mínimas desde", nodo_origen)
            for nodo, costo in distancias.items():
                print(f"{nodo}: {costo}")

            print("\nRutas reconstruidas:")
            for nodo in grafo:
                ruta = reconstruir_ruta(predecesores, nodo)
                print(f"{nodo_origen} → {nodo}: {ruta}")

            # Dibujar rutas (PNG)
            try:
                from utils.graficos import dibujar_rutas_dijkstra
                dibujar_rutas_dijkstra(grafo, distancias, predecesores,
                                    nodo_origen,
                                    nombre_archivo="dijkstra_paths.png")
            except ImportError:
                print("No se pudo generar la imagen PNG de Dijkstra.")


        elif opcion == "4":
            print("\n[Huffman] Ejecutando algoritmo de Huffman...")

            ruta = "data/textos/huffman.txt"
            try:
                with open(ruta, "r", encoding="utf-8") as f:
                    texto = f.read()
            except FileNotFoundError:
                print("⚠️ No se encontró el archivo huffman.txt en data/textos/")
                continue

            frecuencias = contar_frecuencias(texto)
            raiz = construir_arbol(frecuencias)
            codigos = generar_codigos(raiz)

            print("\nFrecuencias:")
            for c, f in frecuencias.items():
                print(f"{repr(c)} : {f}")

            print("\nCódigos Huffman:")
            for c, code in codigos.items():
                print(f"{repr(c)} : {code}")

            print("\nÁrbol de Huffman (representación textual):")
            print(representar_arbol(raiz))

                # Dibujar imágenes obligatorias
            from utils.graficos import dibujar_arbol_huffman, dibujar_frecuencias_huffman
            
            dibujar_arbol_huffman(raiz, "huffman_tree.png")
            dibujar_frecuencias_huffman(frecuencias, "huffman_freq.png")


    # PNGs se generan más adelante cuando pip funcione


        elif opcion == "0":
            print("\nSaliendo del programa. ¡Gracias!")
            break

        else:
            print("\nOpción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
