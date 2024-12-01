class Arista:
    def _init_(self, nodo_origen, nodo_destino, peso=None):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso
        self.conjunto_o = 0
        self.conjunto_d = 0