from Clases.Grafo import Grafo
from Clases.Arista import Arista
from Clases.Nodo import Nodo
from Funciones.barabasi_albert import grafoBarabasiAlbert
from Funciones.malla import grafoMalla
from Funciones.erdos_renyi import grafoErdosRenyi
from Funciones.gilbert import grafoGilbert
from Funciones.geografico_simple import grafoGeografico
from Funciones.barabasi_albert import grafoBarabasiAlbert
from Funciones.dorogovtsev_mendes import grafoDorogovtsevMendes
import random





# Variables para los modelos
n = 100
m = 60
p = 1
r = 10
d = 3
filas = 5            #30 = 5x6      100 = 9x12       500 = 25x20
columnas = 6




# Malla
# grafo = grafoMalla(filas, columnas)
# arbol = grafo.BFS(15)                   #BFS
# arbol = grafo.DFS_R(12)                 #DFSR
# arbol = grafo.DFS_I(200)                #DFSI
# arbol = grafo.dijkstra(4)               #Dijkstra
# arbol = grafo.kruskal()                 #Kruskal 
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim
# sprincito = grafo.spring()                #Spring


# Erdos-Renyi
# grafo = grafoErdosRenyi(n, m)
# arbol = grafo.BFS(4)                    #BFS
# arbol = grafo.DFS_R(4)                  #DFSR
# arbol = grafo.DFS_I(4)                  #DFSI
# arbol = grafo.dijkstra(50)              #Dijkstra
# arbol = grafo.kruskal()                 #Kruskal
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim


# Gilbert
# grafo = grafoGilbert(n, p)
# arbol = grafo.BFS(15)                   #BFS
# arbol = grafo.DFS_R(29)                 #DFSR
# arbol = grafo.DFS_I(15)                 #DFSI
# arbol = grafo.dijkstra(4)               #Dijkstra
# arbol = grafo.kruskal()                 #Kruskal #AUMENTAR LA PROBABILIDAD DE CONECCION!!
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim


# Geográfico
# grafo = grafoGeografico(n, r)
# arbol = grafo.BFS(15)                   #BFS
# arbol = grafo.DFS_I(15)                 #DFSI
# arbol = grafo.DFS_R(29)                 #DFSR
# arbol = grafo.dijkstra(4)               #Dijkstra
# arbol = grafo.kruskal()                 #Kruskal AUMENTAR LA DISTANCIA R PARA QUE SIEMPRE SE CONECTE EL GRAFO
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim



# Barabasi-Albert
# grafo = grafoBarabasiAlbert(n, d)
# arbol = grafo.BFSChidito(15)            #BFS especial para barabasi por que maneja tipo de datos string
# arbol = grafo.DFS_I(15)                 #DFSI
# arbol = grafo.DFS_R(15)                 #DFSR
# arbol = grafo.dijkstra(4)               #Dijkstra
# arbol = grafo.kruskal()                 #Kruskal
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim


# Dorogovtsev-Mendes
grafo = grafoDorogovtsevMendes(500)
# grafo.imprimir_lista_nodos()
# arbol = grafo.BFS(15)                   #BFS
# arbol = grafo.DFS_I(250)                #DFSI
# arbol = grafo.DFS_R(50)                 #DFSR
# arbol = grafo.dijkstra(4)               #Dijkstra
# arbol = grafo.kruskalD()                #Kruskal
# arbol = grafo.kruskalI()                #Kruskal
# arbol = grafo.prim()                    #Prim


