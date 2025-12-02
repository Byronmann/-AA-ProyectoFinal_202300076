#  Universidad Da Vinci de Guatemala

## Facultad de Ingeniería, Industria y Tecnología

### **Análisis de Algoritmos -- Proyecto Final**

**Estudiante:** Byron Rodolfo Maldonado Palacios\
**Carnet:** 202300076\
**Fecha:** Diciembre 2024

------------------------------------------------------------------------

#  PROYECTO FINAL

# **Implementación y Visualización de Algoritmos Avanzados**

##  **Objetivo General**

Desarrollar un programa en Python capaz de implementar, analizar y
visualizar los algoritmos Prim, Kruskal, Dijkstra y Huffman utilizando
archivos externos como entrada, generando imágenes PNG como evidencia,
documentando el trabajo de forma profesional y aplicando un flujo de
trabajo Gitflow.

------------------------------------------------------------------------

## **Objetivos Específicos**

-   Implementar de forma modular:
    -   ✔ Prim (Árbol de Expansión Mínima)\
    -   ✔ Kruskal (Árbol de Expansión Mínima)\
    -   ✔ Dijkstra (Rutas más cortas)\
    -   ✔ Huffman (Codificación óptima)\
-   Leer grafos desde archivos CSV y textos desde archivos TXT.\
-   Generar imágenes PNG obligatorias.\
-   Documentar el proyecto mediante un `README.md`.\
-   Aplicar Gitflow completo con ramas, PRs, merges, release, hotfix y
    tags.\
-   Explicar la complejidad teórica de cada algoritmo.

------------------------------------------------------------------------

#  **Explicación Teórica de Algoritmos**

##  **Prim**

Algoritmo que construye un Árbol de Expansión Mínima seleccionando
siempre la arista más barata desde el conjunto de nodos ya conectados.\
**Complejidad:** `O(E log V)`

##  **Kruskal**

Selecciona todas las aristas del grafo en orden creciente de peso y
utiliza Union-Find para evitar ciclos.\
**Complejidad:** `O(E log E)`

##  **Dijkstra**

Calcula las rutas más cortas desde un origen hacia todos los nodos
usando una cola de prioridad (heap).\
**Complejidad:** `O((V + E) log V)`

##  **Huffman**

Construye un árbol de codificación óptima basado en frecuencias para
comprimir datos sin pérdida.\
**Complejidad:** `O(n log n)`

------------------------------------------------------------------------

#  **Formato de Entrada**

## Grafo (CSV)

Ejemplo:

    origen,destino,peso
    A,B,4
    A,C,2
    B,C,1
    B,D,5

## Texto (TXT)

Archivo dado por el ingeniero (incluye símbolos, espacios y caracteres
especiales).

------------------------------------------------------------------------

#  **Ejecución del Programa**

Ejecutar en terminal:

    python main.py

Aparece un menú con:

1.  Prim\
2.  Kruskal\
3.  Dijkstra\
4.  Huffman\
5.  Salir

------------------------------------------------------------------------

#  **Imágenes PNG Generadas**

(Se mostrarán automáticamente cuando las librerías estén instaladas)

-   **prim_mst.png**\
-   **kruskal_mst.png**\
-   **dijkstra_paths.png**\
-   **huffman_tree.png**\
-   **huffman_freq.png**

------------------------------------------------------------------------

#  **Flujo Gitflow aplicado**

Ramas obligatorias creadas:

    main
    develop
    feature/prim
    feature/kruskal
    feature/dijkstra
    feature/huffman
    hotfix/nombre_ficticio
    release/v1.0.0

Evidencias (ubicadas en `docs/evidencias/`): - `git branch -a`\
- `git log --oneline --decorate --graph`\
- PRs de cada feature hacia develop\
- PR de develop → main\
- Tag `v1.0.0` creado al finalizar

------------------------------------------------------------------------

#  **Conclusiones**

Este proyecto permitió comprender e implementar algoritmos fundamentales
para grafos y compresión, así como aplicar prácticas profesionales de
desarrollo como modularidad, documentación, manejo de archivos,
generación de imágenes y control de versiones con Gitflow. La
experiencia fortaleció la lógica, la organización y las habilidades
técnicas clave para la ingeniería de software.
