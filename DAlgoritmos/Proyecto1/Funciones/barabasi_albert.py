from Clases.Grafo import Grafo
import random

# Función para Modelo Gn,d Barabási-Albert
def grafoBarabasiAlbert(n, d, dirigido=False):
    grafo = Grafo()
    grafo.crear_nodos(n)

    # Conectar los primeros d nodos completamente
    for i in range(d):
        for j in range(i + 1, d + 1):
            grafo.crear_aristas(i + 1, j + 1)

    # Agregar los nodos restantes con probabilidad proporcional al grado
    for nuevo_nodo in range(d + 1, n + 1):
        nodos_existentes = [i for i in range(1, nuevo_nodo)]
        grados = [sum(1 for arista in grafo.lista_aristas if arista.nodo_origen == i or arista.nodo_destino == i)
                  for i in nodos_existentes]
        total_grados = sum(grados)
        probabilidades = [grado / total_grados for grado in grados]

        for _ in range(d):
            nodo_existente = random.choices(nodos_existentes, weights=probabilidades, k=1)[0]
            grafo.crear_aristas(nuevo_nodo, nodo_existente)
            if not dirigido:
                grafo.crear_aristas(nodo_existente, nuevo_nodo)

    grafo.imprimir_lista_aristas()
#    grafo.guardar_csv("BarabasiAlbert\\BarabasiAlbert.csv")
    grafo.guardar_graphviz("BarabasiAlbert\\BarabasiAlbert.gv")
    return grafo