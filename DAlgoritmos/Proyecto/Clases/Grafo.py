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
        
    def asignar_conjuntos(self):
            
        
            for i in self.lista_aristas:
                i.conjunto_o = i.nodo_origen
                i.conjunto_d = i.nodo_destino
            #     i.conjunto = i.nodo_origen
                # print("conjunto", i.conjunto_o)
                # print("conjunto", i.conjunto_d)
            
        
    def obtener_Indices(self, lista, valor):
        indice = lista.index(valor)
        return indice

    def limpiar_LN(self, lisN):
        mi_lista_sin_repetidos = []
        
        
        for elementoind in lisN:
            elemento = str(elementoind)
            if elemento not in mi_lista_sin_repetidos:
                mi_lista_sin_repetidos.append(elemento)
            else:
                pass
        lNF = self.convertir_a_int(mi_lista_sin_repetidos)
        
        return lNF

    def convertir_a_int(self, lista):
        nueva_lista = []
        for elemento in lista:
            try:
                nueva_lista.append(int(elemento))  # Intenta convertir el elemento a entero
            except (ValueError, TypeError):       # Si no se puede convertir, lo omite
                pass
        return nueva_lista





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

    def BFSChidito(self, s):
        # Crear un nuevo grafo para almacenar el árbol BFS
        arbol_bfs = Grafo()
        
        # Lista para almacenar las aristas del árbol
        lista_aristas = []
        
        # Estructuras auxiliares
        cola = [s]
        visitados = set()
        
        # Agregar el nodo inicial al árbol
        # print(f"Agregando nodo inicial al árbol BFS: {nodo_inicial}")
        arbol_bfs.agregarNodo(s)
        visitados.add(s)
    
        # Generar lista de adyacencia
        lista_adyacencia = self.generar_lista_adyacencia()
        # print(f"Lista de adyacencia generada: {lista_adyacencia}")
    
        # Recorrido BFS
        while cola:
            nodo_actual = cola.pop(0)
            # print(f"Procesando nodo actual: {nodo_actual}")
    
            # Recorrer los vecinos del nodo actual
            for vecino in map(int, lista_adyacencia.get(str(nodo_actual), [])):
                # print(f"Vecino encontrado: {vecino}")
                if vecino not in visitados:
                    # print(f"Visitando vecino: {vecino}")
                    
                    # Marcar como visitado
                    visitados.add(vecino)
                    
                    # Añadir nodo y arista al árbol BFS
                    arbol_bfs.agregarNodo(vecino)
                    arbol_bfs.crear_aristas(nodo_actual, vecino)
                    # print(f"Creando arista: ({nodo_actual}, {vecino})")
                    
                    # Añadir la arista a la lista
                    lista_aristas.append((nodo_actual, vecino))
                    
                    # Añadir el vecino a la cola
                    cola.append(vecino)
        
        # Retornar el árbol BFS y las aristas
        print(f"Aristas del árbol BFS: {lista_aristas}")
        self.guardarBFS_DFS(lista_aristas, "BFS")
        return arbol_bfs, lista_aristas
            
        
    
    def generar_lista_adyacencia(self):
        # Crear lista de adyacencia desde objetos Arista
        lista_adyacencia = defaultdict(list)
        for arista in self.lista_aristas:
            # Accede a los nodos de la arista
            u = arista.nodo_origen
            v = arista.nodo_destino
            
            lista_adyacencia[u].append(v)
            lista_adyacencia[v].append(u)  # Para grafos no dirigidos
        
        return lista_adyacencia



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

    def kruskal(self):
        t = []                                                       # Crear lista de ¡ARISTAS!  agregados del arbol
        agregados = []                                               # Crear lista de ¡NODOS!    agregados al arbol
        self.asignar_pesos()                                         # Ponemos pesos randoms a nuestras aristas
        self.lista_aristas.sort(key=lambda arista: arista.peso)      # Ordenamos las aristas por peso
        self.asignar_conjuntos()                                     # Se le asigna un conjunto a cada nodo
        print("\nAristas Ordenadas:")
        self.imprimir_lista_aristas()
        print("\n\n")
        
        coninit = self.lista_aristas[0].conjunto_o
                
        for i in self.lista_aristas:
            print("\nArista: (" + str(i.nodo_origen) + "," + str(i.nodo_destino) + ")")     #Borrar!
            print("NO: " + str(i.nodo_origen) + " --- " "ND: " + str(i.nodo_destino))    #Borrar!
            print("CO: " + str(i.conjunto_o) + " --- " "CD: " + str(i.conjunto_d))    #Borrar!
            conant = i.conjunto_d
            
            
            #Posicionar la condicion bien: si el conjunto destino == al conjunto inicial
            if i.conjunto_d != i.conjunto_o:
                    if i.conjunto_d == coninit:
                        i.conjunto_o = i.conjunto_d
                        for j in self.lista_aristas:
                            if j.conjunto_o == conant:
                                j.conjunto_o = i.conjunto_d
                            if j.conjunto_d == conant:
                                j.conjunto_o = i.conjunto_d
                                
                                
                            if j.nodo_origen == i.nodo_origen:
                                j.conjunto_o = i.conjunto_d
                            if j.nodo_destino == i.nodo_origen:
                                j.conjunto_destino = i.conjunto_d
                        t.append(i)
                        print("Se cambia:")
                        print("NO: " + str(i.nodo_origen) + " --- " "ND: " + str(i.nodo_destino))    #Borrar!
                        print("CO: " + str(i.conjunto_o) + " --- " "CD: " + str(i.conjunto_d))    #Borrar!
                    elif i.conjunto_o == coninit:
                        i.conjunto_d = coninit
                        
                        t.append(i)
                    
                    elif i.conjunto_d != coninit:
                        i.conjunto_d = i.conjunto_o
                        for j in self.lista_aristas:
                            if j.conjunto_o == conant:
                                j.conjunto_o = i.conjunto_o
                            if j.conjunto_d == conant:
                                j.conjunto_d = i.conjunto_o
                                
                                
                            if j.nodo_destino == i.nodo_destino:
                                j.conjunto_d = i.conjunto_o
                            if j.nodo_origen == i.nodo_destino:
                                j.conjunto_o = i.conjunto_o
                        t.append(i)
                        print("Se cambia:")
                        print("NO: " + str(i.nodo_origen) + " --- " "ND: " + str(i.nodo_destino))    #Borrar!
                        print("CO: " + str(i.conjunto_o) + " --- " "CD: " + str(i.conjunto_d))    #Borrar!        
                            
            elif i.conjunto_d == i.conjunto_o:
                print("No se agrega!")

        
        
        self.imprimir_arbol(t)
        
        self.guardar_kruskal(t, "KruskalTree") #Guardamos el arbol en archivo .gv
            
        return t    #Retornamos la lista de aristas del arbol Final 
        



    def kruskalrespaldo(self):
        t = []                                                       # Crear lista de ¡ARISTAS!  agregados del arbol
        agregados = []                                               # Crear lista de ¡NODOS!    agregados al arbol
        self.asignar_pesos()                                         # Ponemos pesos randoms a nuestras aristas
        self.lista_aristas.sort(key=lambda arista: arista.peso)      # Ordenamos las aristas por peso
        self.asignar_conjuntos()                                     # Se le asigna un conjunto a cada nodo
        
        
        #Bloque de impresion para validar el orden
        print("\n¡¡Aristas Ordenadas!!")                             #BORRAR!!
        self.imprimir_lista_aristas()                                # Ordenamos las aristas por peso! #BORRAR!!
        print("\n")                                                  #BORRAR!!
        
        
        ind = 0 #Solo inicializa un indice para recorrer la lista de aristas
        for i in self.lista_aristas:
            print("\nArista completa antes de analizar:", i.nodo_origen, ",", i.nodo_destino) #BORRAR!!
            #obtener indices:
            self.imprimir_lista_nodos() # BORRAR!!
            
            print("\nLista de nodos INDEX", i.nodo_origen, type(i.nodo_origen))
            no = self.lista_nodos.index(int(i.nodo_origen))        # Obtenemos el indice en la lista de nodos del nodo origen
            nd = self.lista_nodos.index(int(i.nodo_destino))        # Obtenemos el indice en la lista de nodos del nodo destino
            
            
            
        
            print("Arista a analizar:", str(ind+1) + ".-(" + str(self.lista_nodos[no]) + "," + str(self.lista_nodos[nd]) + ")")        #BORRAR!!!
            #Condiciones:
            if self.lista_nodos[nd].conjunto != self.lista_nodos[no].conjunto and self.lista_nodos[nd] not in agregados: # Si el conjunto de nodo origen es diferente al del destino entonces:   
                conjant = self.lista_nodos[nd].conjunto                           # Guardamos el conjunto anterior del N_Destino
                
                self.lista_nodos[nd].conjunto = self.lista_nodos[no].conjunto     # Metemos al N_Nestino al conjunto del N_Origen
                t.append(self.lista_aristas[ind])                                 # Agrega la ARISTA la Lista de arbol final "T"
                
                agregados.append(self.lista_nodos[nd])                            # Agrega el NODO a la Lista de N_Agregados al arbol

                
                for j in t:
                    ind2 = 0                               # Solo inicializa un indice para recorrer la lista de Nodos
                    for w in self.lista_nodos:             # SOLO Recorre toda la lista de nodos
                        if self.lista_nodos[ind2].conjunto == conjant:  # Encuentra los nodos que estaban en el mismo conjunto anterior del nodo que acabamos de cambiar de conjunto
                            self.lista_nodos[ind2].conjunto = self.lista_nodos[no].conjunto   # Entonces tambien se le asigna al conjunto del nuevo nodo origen que se esta validando (Se los lleva con el al nuevo conjunto)
                        ind2 += 1       # Aumenta 1 en nuestro indice de la Lista de Nodos
        
            else:            # Si los nodos que se estan validando Son del mismo conjunto
                    pass     # Entonces solo la ignora y no la agrega a nuestro arbol final
            
            ind +=1    #aumenta 1 en nuestro indice de la lista de ARISTAS
        
        
        
        
        #Imprimir el Arbol (se puede comentar este bloque es solo para la consola):
        print("\n\nArbol Kruskal")
        kind = 1           # Inicializamos el indice para numerar las aristas finales
        for k in t:        # Recorremos la lista en la que se guarda el arbol
            print(str(kind) + ".-", "(" + str(k.nodo_origen) + "," + str(k.nodo_destino) + ")")  # Imprimimos los N_Origen , N_Destino
            kind +=1       # Aumentamos el indice para pasar a la siguiente arista
        
        
        
        
        
        self.guardar_kruskal(t, "KruskalTree") #Guardamos el arbol en archivo .gv
            
        return t    #Retornamos la lista de aristas del arbol Final
        
        
        
        
        

 
            
















    # Métodos para imprimir las listas
    def imprimir_arbol(self, listarbol):
        cont = 1
        print("\nArbol: ")
        for i in listarbol:
            print(str(cont) + ".- (" + str(i.nodo_origen) + "," + str(i.nodo_destino) + ")")
            cont += 1
        
    def imprimir_lista_nodos(self):
        print("\nLista de Nodos:")
        for i in self.lista_nodos:
            print(i.id, "tipo:", type(i))

    def imprimir_coordenadas(self):
        for i in self.lista_nodos:
            print("(" + str(i.x) + "," + str(i.y) + ")")

    def imprimir_lista_aristas(self):
        print("Aristas:")
        ind = 1
        for i in self.lista_aristas:
            print(str(ind) + ".-","(" + str(i.nodo_origen) + "," + str(i.nodo_destino) + ")")  # Formato de impresión de la arista
            ind += 1

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



    def guardar_kruskal(self, aristas, nombreAlgo):
        # Escribir el árbol BFS en formato Graphviz (.gv)
        nombre_archivo = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\" + nombreAlgo + ".gv"
        with open(nombre_archivo, 'w') as f:
            f.write("digraph KruskalTree {\n")
            for arista in aristas:
                f.write(f'  {arista.nodo_origen} -- {arista.nodo_destino};\n')
            f.write("}\n")
        print("\nArbol Kruskal Guardado!")