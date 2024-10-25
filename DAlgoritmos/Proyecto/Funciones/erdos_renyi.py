from Clases.Grafo import Grafo
import random

def grafoErdosRenyi(n, m, dirigido=False):
    grafo = Grafo()
    grafo.crear_nodos(n)

    # Generar todos los pares de nodos                                                    #          comprensión de listas anidada con blucle anidado   
    pares_posibles = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j] # [variable lista[]] = [inicializa variables] [for anidados] [condicion]

    # Elegir m pares al azar
    aristas_elegidas = random.sample(pares_posibles, m) #selecciona "m" elementos de forma aleatoria sin repetirlos.

    for nodo1, nodo2 in aristas_elegidas:
        grafo.crear_aristas(nodo1, nodo2)
        
        if dirigido == True:
            grafo.crear_aristas(nodo2, nodo1)  # Si es dirigido, agregar la arista en ambas direcciones








    grafo.imprimir_lista_aristas()  # Imprimir aristas del grafo
#    grafo.guardar_csv("ErdosRenyi\\ErdosRenyi.csv")
    grafo.guardar_graphviz("ErdosRenyi.gv")  # Guardar en formato GraphViz
    return grafo