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
filas = 24
columnas = 21

# Malla
#grafo = grafoMalla(filas, columnas)

# Erdos-Renyi
#grafoErdosRenyi(n, m)

# Gilbert
#grafoGilbert(n, p)

# Geográfico
#grafoGeografico(n, r)

# Barabasi-Albert
#grafoBarabasiAlbert(n, d)

# Dorogovtsev-Mendes
#grafoDorogovtsevMendes(n)