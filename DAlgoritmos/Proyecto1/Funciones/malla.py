from Clases.Grafo import Grafo

# Función para Método Malla
def grafoMalla(filas, columnas, dirigido=False):
    grafo1 = Grafo()
    # Crear nodos
    total_nodos = filas * columnas
    grafo1.crear_nodos(total_nodos)

    # Crear conexiones
    for i in range(filas):
        for j in range(columnas):
            vertice = i * columnas + j  # Índice del nodo actual

            # Conexión hacia la derecha
            if j < columnas - 1:
                grafo1.crear_aristas(grafo1.lista_nodos[vertice].id, grafo1.lista_nodos[vertice + 1].id)
                if not dirigido:
                    grafo1.crear_aristas(grafo1.lista_nodos[vertice + 1].id, grafo1.lista_nodos[vertice].id)  # Arista en ambas direcciones

            # Conexión hacia abajo
            if i < filas - 1:
                grafo1.crear_aristas(grafo1.lista_nodos[vertice].id, grafo1.lista_nodos[vertice + columnas].id)
                if not dirigido:
                    grafo1.crear_aristas(grafo1.lista_nodos[vertice + columnas].id, grafo1.lista_nodos[vertice].id)  # Arista en ambas direcciones

       
    
    grafo1.imprimir_lista_aristas()  # Imprimir aristas del grafo
#    grafo1.guardar_csv("Malla\\Malla.csv")  # Guardar en CSV
    grafo1.guardar_graphviz("Malla\\Malla.gv")  # Guardar en formato GraphViz
    

    return grafo1


