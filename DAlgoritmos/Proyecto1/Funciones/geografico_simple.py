from Clases.Grafo import Grafo
import random
from math import sqrt

# Función para Modelo Gn,r geográfico simple
def grafoGeografico(n, r, dirigido=False):
    grafo = Grafo()
    grafo.crear_nodos(n)

    # Asignar coordenadas aleatorias a cada nodo
    coordenadas = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(n)]
    for i, (x, y) in enumerate(coordenadas):
        grafo.asignar_coordenadas(i, x, y)

    # Crear aristas basadas en la distancia
    for i in range(n):
        for j in range(i + 1, n):
            distancia = sqrt((coordenadas[i][0] - coordenadas[j][0]) ** 2 + 
                                  (coordenadas[i][1] - coordenadas[j][1]) ** 2)
            if distancia <= r:
                grafo.crear_aristas(grafo.lista_nodos[i].id, grafo.lista_nodos[j].id)
                if not dirigido:
                    grafo.crear_aristas(grafo.lista_nodos[j].id, grafo.lista_nodos[i].id)  # Si no es dirigido




    grafo.imprimir_lista_aristas()  # Imprimir aristas del grafo
#   grafo.guardar_csv("Geografico_simple\\Geografico.csv")
    grafo.guardar_graphviz("Geografico_simple\\Geografico.gv")  # Guardar en formato GraphViz
    
    
    return grafo


