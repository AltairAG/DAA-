from Clases.Grafo import Grafo
import random

# Función para Modelo Gn,p de Gilbert
def grafoGilbert(n, p, dirigido=False):
    # Crear el grafo
    grafo = Grafo()
    grafo.crear_nodos(n)
    
    # Iterar sobre cada par de nodos
    for n1 in range(1, n + 1):
        for n2 in range(n1 + 1, n + 1):  # Evitar duplicados para grafos no dirigidos
            if dirigido:
                # Si es dirigido, considera aristas en ambos sentidos
                if random.random() <= p:
                    grafo.crear_aristas(n1, n2)  # Crear arista de n1 a n2
                if random.random() <= p:
                    grafo.crear_aristas(n2, n1)  # Crear arista de n2 a n1
            else:
                # Si no es dirigido, crea solo una arista sin duplicados
                if random.random() <= p:
                    grafo.crear_aristas(n1, n2)

    # Imprimir lista de aristas y guardar en GraphViz
    grafo.imprimir_lista_aristas()
    grafo.guardar_graphviz("Gilbert.gv")
    
    return grafo
