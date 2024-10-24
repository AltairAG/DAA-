from Clases.Grafo import Grafo
import random

# Función para Modelo Gn,p de Gilbert
def grafoGilbert(n, p, dirigido=False):
    grafo = Grafo()
    grafo.crear_nodos(n)

    # Generar todos los pares de nodos               
    pares_posibles = grafo.combinaciones_posibles(n)
    # pares_posibles = [(i, j) for i in range(1, n + 1) for j in range(1, n + 1) if i != j]
    # pares_posibles_reves = []


    if dirigido == False:
        # for n1,n2 in pares_posibles:
        #     arista_invertida = n2,n1
        #     pares_posibles_reves.append(arista_invertida)

        #     #remover los repetidos inversos en la lista
        #     for i in pares_posibles_reves:
        #         if i in pares_posibles:
        #             pares_posibles.remove(i)



        #Crear Aristas con la lista de pares ya corregida
        for n1, n2 in pares_posibles:
            if random.random() <= p:
                grafo.crear_aristas(n1, n2)
                
            
    elif dirigido == True:
        for i in pares_posibles:
            if random.random() <= p:
                grafo.crear_aristas(n1, n2)
                    
    

    grafo.imprimir_lista_aristas()  # Imprimir aristas del grafo
#    grafo.guardar_csv("Gilbert\\Gilbert.csv")
    grafo.guardar_graphviz("Gilbert\\Gilbert.gv")  # Guardar en formato GraphViz
    return grafo