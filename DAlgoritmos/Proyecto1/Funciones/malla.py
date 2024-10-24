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
                nodo_actual = grafo1.lista_nodos[vertice].id
                nodo_derecha = grafo1.lista_nodos[vertice + 1].id

                if dirigido:
                    # Si es dirigido, permitir aristas en ambas direcciones
                    grafo1.crear_aristas(nodo_actual, nodo_derecha)
                    grafo1.crear_aristas(nodo_derecha, nodo_actual)
                else:
                    # Si no es dirigido, solo agregar la arista si no existe
                    if nodo_actual != nodo_derecha and not grafo1.existe_arista(nodo_actual, nodo_derecha):
                        grafo1.crear_aristas(nodo_actual, nodo_derecha)

            # Conexión hacia abajo
            if i < filas - 1:
                nodo_actual = grafo1.lista_nodos[vertice].id
                nodo_abajo = grafo1.lista_nodos[vertice + columnas].id

                if dirigido:
                    # Si es dirigido, permitir aristas en ambas direcciones
                    grafo1.crear_aristas(nodo_actual, nodo_abajo)
                    grafo1.crear_aristas(nodo_abajo, nodo_actual)
                else:
                    # Si no es dirigido, solo agregar la arista si no existe
                    if nodo_actual != nodo_abajo and not grafo1.existe_arista(nodo_actual, nodo_abajo):
                        grafo1.crear_aristas(nodo_actual, nodo_abajo)




    
    grafo1.imprimir_lista_aristas()  # Imprimir aristas del grafo
#    grafo1.guardar_csv("Malla\\Malla.csv")  # Guardar en CSV
    grafo1.guardar_graphviz("Malla\\Malla.gv")  # Guardar en formato GraphViz
    

    return grafo1


