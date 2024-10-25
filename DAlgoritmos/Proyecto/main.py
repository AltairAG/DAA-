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





# Variables para los modelos
n = 500
m = 60
p = .5
r = 2.5
d = 3
filas = 25             #30 = 5x6      100 = 9x12       500 = 25x20   
columnas = 20

# Malla
# grafo = grafoMalla(filas, columnas)
# arbol = grafo.BFS(15)                  #BFS
# arbol = grafo.DFS_R(12)                #DFSR
# arbol = grafo.DFS_I(200)                #DFSI


# Erdos-Renyi
# grafo = grafoErdosRenyi(n, m)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

# Gilbert
# grafo = grafoGilbert(n, p)
# arbol = grafo.BFS(15)                  #BFS
# arbol = grafo.DFS_R(29)                #DFSR
# arbol = grafo.DFS_I(15)                #DFSI

# Geográfico
# grafo = grafoGeografico(n, r)
# arbol = grafo.BFS(15)                  #BFS
# arbol = grafo.DFS_I(15)                #DFSI
# arbol = grafo.DFS_R(29)                #DFSR

# Barabasi-Albert
# grafo = grafoBarabasiAlbert(n, d)
# arbol = grafo.BFS(15)                  #BFS
# arbol = grafo.DFS_I(15)                #DFSI
# arbol = grafo.DFS_R(15)                #DFSR

# Dorogovtsev-Mendes
grafo = grafoDorogovtsevMendes(n)
# arbol = grafo.BFS(15)                  #BFS
# arbol = grafo.DFS_I(250)                #DFSI
arbol = grafo.DFS_R(50)                #DFSR

