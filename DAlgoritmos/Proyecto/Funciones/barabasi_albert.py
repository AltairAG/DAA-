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
                n1 = str(grafo.lista_nodos[ind])
                n2 = str( grafo.lista_nodos[i])
                grafo.crear_aristas(n1, n2)
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
