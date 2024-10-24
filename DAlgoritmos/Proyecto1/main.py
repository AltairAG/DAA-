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
r = 1
d = 3
filas = 3
columnas = 4

# Malla
grafo = grafoMalla(filas, columnas)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI


# Erdos-Renyi
# grafo = grafoErdosRenyi(n, m)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

# Gilbert
# grafo = grafoGilbert(n, p)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

# Geográfico
#grafo = grafoGeografico(n, r)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

# Barabasi-Albert
# grafo = grafoBarabasiAlbert(n, d)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

# Dorogovtsev-Mendes
# grafo = grafoDorogovtsevMendes(n)
# arbol = grafo.BFS(4)                  #BFS
# arbol = grafo.DFS_R(4)                #DFSR
# arbol = grafo.DFS_I(4)                #DFSI

