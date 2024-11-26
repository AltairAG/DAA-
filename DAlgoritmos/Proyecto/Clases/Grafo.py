import csv
import pandas as pd
from Clases.Nodo import Nodo
from Clases.Arista import Arista
from collections import deque
import random
from heapq import heappop, heappush
from collections import defaultdict
import heapq


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
    
    def agregarNodo(self,n):
        self.lista_nodos.append(Nodo(n))
    

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
            # Genera un peso aleatorio usando una distribución exponencial

            peso = random.random()*100  # 0.1 ajusta la variación; 2 decimales
            arista_Selec.peso = peso 
            
        #self.imprimir_lista_pesos()
            
        
        
        
        
        
        
        
           
    
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

        # Inicialización de distancias y estructuras auxiliares
        distancias = {nodo.id: float('inf') for nodo in self.lista_nodos}
        distancias[s] = 0
        predecesores = {nodo.id: None for nodo in self.lista_nodos}
        cola_prioridad = [(0, s)]
        arbol_dijkstra = []
        
        while cola_prioridad:
            distancia_actual, nodo_actual = heappop(cola_prioridad)
            
            if distancia_actual > distancias[nodo_actual]:
                continue
            
            for arista in self.lista_aristas:
                if arista.nodo_origen == nodo_actual:
                    vecino = arista.nodo_destino
                    peso = arista.peso
                elif arista.nodo_destino == nodo_actual:
                    vecino = arista.nodo_origen
                    peso = arista.peso
                else:
                    continue
                
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = nodo_actual
                    heappush(cola_prioridad, (nueva_distancia, vecino))
                    arbol_dijkstra.append((nodo_actual, vecino, nueva_distancia))
        
        # Encontrar el nodo con el menor costo total distinto de s
        nodo_destino = min((nodo for nodo in distancias if nodo != s), key=distancias.get)
        
        # Construir el camino de menor costo hacia el nodo_destino
        camino_menor_costo = []
        nodo = nodo_destino
        while nodo is not None:
            padre = predecesores[nodo]
            if padre is not None:
                camino_menor_costo.append((padre, nodo))
            nodo = padre
        camino_menor_costo.reverse()
        
        print(camino_menor_costo)

        # Llamar a guardar_dijkstra con el nodo de menor costo distinto de s
        self.guardar_dijkstra("Dijkstra_resultado.gv", camino_menor_costo, s, nodo_destino, distancias)
        
        return arbol_dijkstra, camino_menor_costo

        








        
        








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

    def imprimir_lista_pesos(self):
        for i in self.lista_aristas:
            print("Arista: (" + str(i.nodo_origen) + "," + str(i.nodo_destino) + ") Peso:", i.peso) #Imprimir pesos
    
    def imprimir_grados(self):
        for i in self.lista_nodos:
            nd = int(i.id)
            print("N" + str(self.lista_nodos[nd]), "Grado:", self.lista_nodos[nd].grado)










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
        
    
    def guardar_dijkstra(self, nombre_archivo, camino_menor_costo, nodo_inicio, nodo_fin, distancias):
        # Ruta del archivo
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombre_archivo
        with open(nombre_archivo, 'w') as f:
            f.write("graph G {\n")
            
            # Escribe el nodo de inicio con su color, id y distancia como etiqueta
            distancia_inicio = distancias.get(nodo_inicio, float('inf'))  # Distancia al nodo de inicio
            f.write(f"{nodo_inicio} [label=\"n{nodo_inicio} ({distancia_inicio:.2f})\" color=blue, style=filled];\n")
            
            # Escribe el nodo de fin con su color, id y distancia como etiqueta
            distancia_fin = distancias.get(nodo_fin, float('inf'))  # Distancia al nodo de fin
            f.write(f"{nodo_fin} [label=\"n{nodo_fin} ({distancia_fin:.2f})\" color=red, style=filled];\n")
            
            # Escribe los demás nodos con su id y la distancia al nodo de inicio
            for nodo in self.lista_nodos:
                if nodo.id != nodo_inicio and nodo.id != nodo_fin:
                    distancia = distancias.get(nodo.id, float('inf'))  # Obtiene la distancia del nodo o inf si no está
                    f.write(f"{nodo.id} [label=\"n{nodo.id} ({distancia:.2f})\"];\n")
            
            # Escribe las aristas con colores según el camino de menor costo
            for arista in self.lista_aristas:
                if (arista.nodo_origen, arista.nodo_destino) in camino_menor_costo or \
                (arista.nodo_destino, arista.nodo_origen) in camino_menor_costo:
                    f.write(f"{arista.nodo_origen} -- {arista.nodo_destino} [color=green, penwidth=2, weight=1];\n")
                else:
                    f.write(f"{arista.nodo_origen} -- {arista.nodo_destino} [color=black, penwidth=1, weight=1];\n")
            
            f.write("}\n")

        print(f"Archivo Graphviz guardado como {nombre_archivo}")



