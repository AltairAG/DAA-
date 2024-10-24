from Clases.Grafo import Grafo
import random

# Función para Modelo Gn Dorogovtsev-Mendes
def grafoDorogovtsevMendes(n, dirigido=False):
    grafo = Grafo()
    grafo.crear_nodos(3)

    # Crear un triángulo inicial
    grafo.crear_aristas(1, 2)
    grafo.crear_aristas(2, 3)
    grafo.crear_aristas(3, 1)

    # Agregar los nodos adicionales
    for nuevo_nodo in range(4, n + 1):
        grafo.agregar_nodo(nuevo_nodo)
        # Seleccionar una arista al azar
        arista_aleatoria = random.choice(grafo.lista_aristas)
        grafo.crear_aristas(nuevo_nodo, arista_aleatoria.nodo_origen)
        grafo.crear_aristas(nuevo_nodo, arista_aleatoria.nodo_destino)

    grafo.imprimir_lista_aristas()
#    grafo.guardar_csv("DorogovtsevMendes\\DorogovtsevMendes.csv")
    grafo.guardar_graphviz("DorogovtsevMendes\\DorogovtsevMendes.gv")
    return grafo