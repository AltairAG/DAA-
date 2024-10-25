from Clases.Grafo import Grafo
import random

# Función para Modelo Gn de Dorogovtsev-Mendes
def grafoDorogovtsevMendes(n, dirigido=False):
    if n < 3:
        raise ValueError("El número de nodos debe ser al menos 3 para aplicar el modelo Dorogovtsev-Mendes.")
    
    grafo = Grafo()
    grafo.crear_nodos(3)
    
    # Crear un triángulo inicial entre los primeros 3 nodos
    grafo.crear_aristas(1, 2)
    grafo.crear_aristas(2, 3)
    grafo.crear_aristas(3, 1)
    
    # Agregar nodos adicionales según el modelo Dorogovtsev-Mendes
    for nuevo_nodo in range(4, n + 1):
        # Agregar el nuevo nodo a la lista de nodos
        grafo.crear_nodos(1)

        # Seleccionar una arista existente al azar
        arista_seleccionada = random.choice(grafo.lista_aristas)
        n1, n2 = arista_seleccionada.nodo_origen, arista_seleccionada.nodo_destino

        # Conectar el nuevo nodo a los extremos de la arista seleccionada
        grafo.crear_aristas(nuevo_nodo, n1)
        grafo.crear_aristas(nuevo_nodo, n2)
    
    grafo.imprimir_lista_aristas()  # Imprimir las aristas del grafo
    grafo.guardar_graphviz("DorogovtsevMendes.gv")  # Guardar en formato GraphViz
    return grafo
