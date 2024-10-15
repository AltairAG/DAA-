# Clase para representar una Arista
class Arista:
    def __init__(self, nodo_origen, nodo_destino, peso=None):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso