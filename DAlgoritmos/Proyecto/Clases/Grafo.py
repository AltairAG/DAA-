import csv
import pandas as pd
from Clases.Nodo import Nodo
from Clases.Arista import Arista
from collections import deque
import random
from heapq import heappop, heappush
import math


# Clase para representar el Grafo
class Grafo:
    def __init__(self):
        self.lista_nodos = []
        self.lista_aristas = []

    def crear_nodos(self, n):
        for i in range(1, n + 1):
            nodo_nuevo = Nodo(i)
            self.lista_nodos.append(nodo_nuevo)
            
    def agregar_nodo(self,n):
        self.lista_nodos.append(n)
    

    def crear_aristas(self, nodo1, nodo2):
        nueva_arista = Arista(nodo1, nodo2)
        self.lista_aristas.append(nueva_arista)

    def asignar_coordenadas(self, id_nodo, x, y):
        self.lista_nodos[id_nodo].x = x
        self.lista_nodos[id_nodo].y = y
        
    def combinaciones_posibles(self, n):     # eliminar los repetidos en la lista de pares posibles!!###
        combinaciones = []             
        
        # Recorremos los elementos con dos bucles anidados
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                combinaciones.append((i, j))
        
        return combinaciones
    def existe_arista(self, nodo1, nodo2):
        # Recorremos la lista de aristas para ver si existe la arista nodo1 -> nodo2 o nodo2 -> nodo1
        for arista in self.lista_aristas:
            if (arista.nodo_origen == nodo1 and arista.nodo_destino == nodo2) or \
               (arista.nodo_origen == nodo2 and arista.nodo_destino == nodo1):
                return True
        return False
    
    def asignar_pesos(self):
        for arista_Selec in self.lista_aristas:
            peso = random.random()
            arista_Selec.peso = peso   
        
        
        
        
        
           
    
    def BFS(self, s):
        # BFS: Utiliza una cola (FIFO) para explorar el grafo en anchura
        visitados = set()
        cola = deque([s])  # Cola para nodos por visitar, comienza con el nodo s
        arbol_bfs = []  # Lista para almacenar el árbol inducido por BFS
        
        visitados.add(s)
        
        while cola:
            nodo_actual = cola.popleft()  # Extraer el nodo actual
            for arista in self.lista_aristas:
                # Si la arista conecta con un nodo aún no visitado
                if arista.nodo_origen == nodo_actual and arista.nodo_destino not in visitados:
                    cola.append(arista.nodo_destino)
                    visitados.add(arista.nodo_destino)
                    arbol_bfs.append((nodo_actual, arista.nodo_destino))
                elif arista.nodo_destino == nodo_actual and arista.nodo_origen not in visitados:
                    cola.append(arista.nodo_origen)
                    visitados.add(arista.nodo_origen)
                    arbol_bfs.append((nodo_actual, arista.nodo_origen))
        
        print("\nÁrbol BFS:\n", arbol_bfs)
        self.guardarBFS_DFS(arbol_bfs, "BFS")
        
        
        return arbol_bfs  # Devuelve el árbol en forma de lista de aristas

    def DFS_R(self, s):
        # DFS recursivo: utiliza recursión para explorar el grafo en profundidad
        visitados = set()
        arbol_dfs = []

        # Función auxiliar recursiva para DFS
        def dfs_recursivo(nodo_actual):
            visitados.add(nodo_actual)
            for arista in self.lista_aristas:
                # Explora desde nodo_actual al nodo destino si no ha sido visitado
                if arista.nodo_origen == nodo_actual and arista.nodo_destino not in visitados:
                    arbol_dfs.append((nodo_actual, arista.nodo_destino))  # Añade la arista al árbol
                    dfs_recursivo(arista.nodo_destino)  # Llamada recursiva al nodo destino
                # Explora desde nodo_actual al nodo origen (en caso de grafo no dirigido)
                elif arista.nodo_destino == nodo_actual and arista.nodo_origen not in visitados:
                    arbol_dfs.append((nodo_actual, arista.nodo_origen))  # Añade la arista al árbol
                    dfs_recursivo(arista.nodo_origen)  # Llamada recursiva al nodo origen

        # Llamada inicial a la función recursiva
        dfs_recursivo(s)

        # Mostrar y guardar el árbol DFS generado
        print("\nÁrbol DFS_R:\n", arbol_dfs)
        self.guardarBFS_DFS(arbol_dfs, "DFS_R")

        return arbol_dfs  # Retorna el árbol DFS

        
    
    def DFS_I(self, s):
        # DFS iterativo: utiliza una pila (LIFO) para explorar el grafo en profundidad
        visitados = set()
        pila = [(s, None)]  # Pila de nodos por visitar, incluyendo el nodo y el nodo anterior (padre)
        arbol_dfs = []  # Para almacenar las aristas del árbol DFS

        while pila:
            nodo_actual, padre = pila.pop()  # Extraer el nodo actual y su nodo padre

            if nodo_actual not in visitados:
                visitados.add(nodo_actual)

                if padre is not None:
                    # Añadir al árbol DFS solo si existe un padre, es decir, no es el nodo raíz
                    arbol_dfs.append((padre, nodo_actual))

                # Explorar las aristas salientes del nodo actual
                for arista in self.lista_aristas:
                    if arista.nodo_origen == nodo_actual and arista.nodo_destino not in visitados:
                        pila.append((arista.nodo_destino, nodo_actual))
                    elif arista.nodo_destino == nodo_actual and arista.nodo_origen not in visitados:
                        pila.append((arista.nodo_origen, nodo_actual))

        # Guardar el árbol DFS en un archivo CSV
        self.guardarBFS_DFS(arbol_dfs, "DFS_I")

        print("\nÁrbol DFS_I:\n", arbol_dfs)
        return arbol_dfs  # Devuelve el árbol en forma de lista de aristas
    
    
    def dijkstra(self, s):
        self.asignar_pesos()
        
        
        # Inicialización
        distancias = {nodo.id: float('inf') for nodo in self.lista_nodos}  # Inicializar las distancias con infinito
        distancias[s] = 0  # La distancia al nodo inicial es 0
        predecesores = {nodo.id: None for nodo in self.lista_nodos}  # Diccionario de predecesores
        nodos_no_visitados = list(self.lista_nodos)  # Lista de nodos por visitar

        while nodos_no_visitados:
            # Encontrar el nodo con la distancia mínima
            nodo_actual = min(nodos_no_visitados, key=lambda nodo: distancias[nodo.id])
            nodos_no_visitados.remove(nodo_actual)

            # Actualizar las distancias de los vecinos
            for arista in self.lista_aristas:
                if arista.nodo_origen == nodo_actual:
                    vecino = arista.nodo_destino
                elif arista.nodo_destino == nodo_actual:
                    vecino = arista.nodo_origen
                else:
                    continue

                nueva_distancia = distancias[nodo_actual.id] + arista.peso
                if nueva_distancia < distancias[vecino.id]:
                    distancias[vecino.id] = nueva_distancia
                    predecesores[vecino.id] = nodo_actual.id

        # Guardar el grafo calculado en un archivo .gv
        self.guardar_grafo_calculado("Dijkstra_Tree", s, predecesores, distancias)

        return distancias, predecesores  # Regresar las distancias y los predecesores


    def guardar_grafo_calculado(self, nombre_archivo, nodo_inicio, predecesores, distancias):
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombre_archivo + ".gv"
        
        # Construir la ruta óptima usando los predecesores
        ruta_optima = set()
        for nodo_id in predecesores:
            nodo_actual = nodo_id
            while nodo_actual is not None and predecesores[nodo_actual] is not None:
                ruta_optima.add((predecesores[nodo_actual], nodo_actual))
                nodo_actual = predecesores[nodo_actual]

        with open(nombre_archivo, 'w') as f:
            f.write("digraph Dijkstra_Tree {\n")
            
            # Colorear los nodos de inicio y destino, y mostrar el ID con la distancia en el label
            for nodo in self.lista_nodos:
                nodo_id = nodo.id  # Aquí accedes directamente al id de cada nodo
                label = f"{nodo_id} ({distancias[nodo_id]:.2f})"  # Mostrar la distancia junto al ID
                
                # Asignar color azul al nodo de inicio y verde a los nodos en la ruta óptima
                color = "blue" if nodo_id == str(nodo_inicio) else "green" if nodo.id in [dest[1] for dest in ruta_optima] else "black"
                f.write(f'  {nodo_id} [label="{label}", color="{color}", style=filled, fontcolor=white];\n')
            
            # Colorear las aristas que pertenecen a la ruta óptima en azul
            for arista in self.lista_aristas:
                origen_id = arista.nodo_origen  # Si es un ID (entero) en lugar de un objeto Nodo
                destino_id = arista.nodo_destino 
                
                # Asignar color azul a las aristas que pertenecen a la ruta óptima
                color = "blue" if (origen_id, destino_id) in ruta_optima or (destino_id, origen_id) in ruta_optima else "black"
                f.write(f'  {origen_id} -> {destino_id} [color="{color}"];\n')
            
            f.write("}\n")






        
        








    # Métodos para imprimir las listas
    def imprimir_lista_nodos(self):
        for i in self.lista_nodos:
            print(i.id)

    def imprimir_coordenadas(self):
        for i in self.lista_nodos:
            print("(" + str(i.x) + "," + str(i.y) + ")")

    def imprimir_lista_aristas(self):
        for i in self.lista_aristas:
            print("(" + str(i.nodo_origen) + "," + str(i.nodo_destino) + ")")  # Formato de impresión de la arista










    # Métodos para guardar los archivos:
    def guardar_csv(self, nombre_archivo):
        
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombre_archivo
        # Crear una lista de conexiones (tuplas de origen y destino)
        conexiones = [(arista.nodo_origen, arista.nodo_destino) for arista in self.lista_aristas]

        # Crear un DataFrame de pandas a partir de las conexiones
        grafo_df = pd.DataFrame(conexiones, columns=["Source", "Target"])
        
        # Guardar el DataFrame en un archivo CSV
        grafo_df.to_csv(nombre_archivo, index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

    def guardar_graphviz(self, nombre_archivo):
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombre_archivo
        with open(nombre_archivo, 'w') as f:
            f.write("graph G {\n")
            
            for nodo in self.lista_nodos:
                f.write (f"{nodo.id};\n")
                
            for arista in self.lista_aristas:
                f.write(f"{arista.nodo_origen} -- {arista.nodo_destino};\n")
            f.write("}\n")
    
    def guardarBFS_DFS(self, aristas, nombreAlgo):
    # Escribir el árbol BFS en formato Graphviz (.gv)
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombreAlgo + ".gv"
        with open(nombre_archivo, 'w') as f:
            f.write("digraph BFS_Tree {\n")
            for arista in aristas:
                f.write(f'  {arista[0]} -- {arista[1]};\n')
            f.write("}\n")
            
