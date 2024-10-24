import csv
import pandas as pd
from Clases.Nodo import Nodo
from Clases.Arista import Arista
from collections import deque

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
        # DFS recursivo: Utiliza recursión para explorar el grafo en profundidad
        visitados = set()
        arbol_dfs = []
        
        def dfs_recursivo(nodo_actual):
            visitados.add(nodo_actual)
            for arista in self.lista_aristas:
                if arista.nodo_origen == nodo_actual and arista.nodo_destino not in visitados:
                    arbol_dfs.append((nodo_actual, arista.nodo_destino))
                    dfs_recursivo(arista.nodo_destino)
                elif arista.nodo_destino == nodo_actual and arista.nodo_origen not in visitados:
                    arbol_dfs.append((nodo_actual, arista.nodo_origen))
                    dfs_recursivo(arista.nodo_origen)
        
        dfs_recursivo(s)
        
        print("\nÁrbol DFS_R:\n", arbol_dfs)
        self.guardarBFS_DFS(arbol_dfs, "DFS_R")
        
        return arbol_dfs  # Devuelve el árbol en forma de lista de aristas
    
    def DFS_I(self, s):
        # DFS iterativo: Utiliza una pila (LIFO) para explorar el grafo en profundidad
        visitados = set()
        pila = [s]  # Pila de nodos por visitar
        arbol_dfs = []
        
        while pila:
            nodo_actual = pila.pop()  # Extraer el nodo actual de la pila
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                for arista in self.lista_aristas:
                    if arista.nodo_origen == nodo_actual and arista.nodo_destino not in visitados:
                        pila.append(arista.nodo_destino)
                        arbol_dfs.append((nodo_actual, arista.nodo_destino))
                    elif arista.nodo_destino == nodo_actual and arista.nodo_origen not in visitados:
                        pila.append(arista.nodo_origen)
                        arbol_dfs.append((nodo_actual, arista.nodo_origen))
        
        print("\nÁrbol DFS_I:\n", arbol_dfs)
        self.guardarBFS_DFS(arbol_dfs, "DFS_I")

        return arbol_dfs  # Devuelve el árbol en forma de lista de aristas







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
        
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto1\\Archivos\\" + nombre_archivo
        # Crear una lista de conexiones (tuplas de origen y destino)
        conexiones = [(arista.nodo_origen, arista.nodo_destino) for arista in self.lista_aristas]

        # Crear un DataFrame de pandas a partir de las conexiones
        grafo_df = pd.DataFrame(conexiones, columns=["Source", "Target"])
        
        # Guardar el DataFrame en un archivo CSV
        grafo_df.to_csv(nombre_archivo, index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

    def guardar_graphviz(self, nombre_archivo):
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto1\\Archivos\\" + nombre_archivo
        with open(nombre_archivo, 'w') as f:
            f.write("graph G {\n")
            
            for nodo in self.lista_nodos:
                f.write (f"{nodo.id};\n")
                
            for arista in self.lista_aristas:
                f.write(f"{arista.nodo_origen} -- {arista.nodo_destino};\n")
            f.write("}\n")
    
    def guardarBFS_DFS(self, aristas, nombreAlgo):
    # Escribir el árbol BFS en formato Graphviz (.gv)
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto1\\Archivos\\" + nombreAlgo + ".gv"
        with open(nombre_archivo, 'w') as f:
            f.write("digraph BFS_Tree {\n")
            for arista in aristas:
                f.write(f'  {arista[0]} -- {arista[1]};\n')
            f.write("}\n")
            
