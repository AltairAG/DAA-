from Clases.Grafo import Grafo
import random

# Función para Modelo Gn,d Barabási-Albert
def grafoBarabasiAlbert(n, d, dirigido=False):
    grafo = Grafo()
    ind = 0

    
    # Agregar el nodo inicial
    grafo.agregarNodo(0)             # Creamos el primer nodo
    grafo.lista_nodos[0].grado = d    # Le asignamos el grado total para nuevos nodos
    
    
    for i in range(1, n+1):              # i es el indice del nuevo nodo!!
        grafo.agregarNodo(i)             # Creamos el nuevo nodo
        grafo.lista_nodos[i].grado = d    # Le asignamos el grado total para nuevos nodos
        
        for j in range(0, n+1):
            if grafo.lista_nodos[ind].grado > 0:
                grafo.crear_aristas(grafo.lista_nodos[ind], grafo.lista_nodos[i])
                grafo.lista_nodos[ind].grado -= 1 
                grafo.lista_nodos[i].grado -= 1 
                break
            else:
                ind += 1
            
    
    # grafo.imprimir_grados()        
    # grafo.imprimir_lista_pesos()
    grafo.imprimir_lista_aristas()
    # grafo.guardar_csv("BarabasiAlbert\\BarabasiAlbert.csv")
    grafo.guardar_graphviz("BarabasiAlbert.gv")
    
    return grafo

















# from Clases.Grafo import Grafo
# import random

# # Función para Modelo Gn,d Barabási-Albert
# def grafoBarabasiAlbert(n, d, dirigido=False):
#     grafo = Grafo()
#     j = 0

    
#     # Agregar el nodo inicial
#     grafo.agregarNodo(0)             # Creamos el primer nodo
#     grafo.lista_nodos[0].grado = d    # Le asignamos el grado total para nuevos nodos
    
#     for nod2 in range(1, n+1):
#         grafo.agregarNodo(nod2)             # Creamos un nuevo nodo
#         grafo.lista_nodos[nod2].grado = d   # Le asignamos nuevamente el grado total para nuevos nodos
        
                         
#         for nod1 in grafo.lista_nodos:
#             if nod1.grado > 0 and grafo.lista_nodos[nod2].id != nod1:
                
#                 grafo.crear_aristas(nod1.id, grafo.lista_nodos[nod2].id)
#                 nod1.grado -= 1
#                 grafo.lista_nodos[nod2].grado -= 1
#     j = j+1            
            
    
#     # grafo.imprimir_grados()        
#     # grafo.imprimir_lista_pesos()

#     grafo.imprimir_lista_aristas()
#     # grafo.guardar_csv("BarabasiAlbert\\BarabasiAlbert.csv")
#     grafo.guardar_graphviz("BarabasiAlbert.gv")
    
#     return grafo