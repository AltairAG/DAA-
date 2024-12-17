class Arista:
    def __init__(self, nodo_origen, nodo_destino, peso=None):
        self.nodo_origen = nodo_origen
        self.nodo_destino = nodo_destino
        self.peso = peso
        self.conjunto_o = 0
        self.conjunto_d = 0
        
        #Atributos proyecto 5
        self.fuerza_origen = 0
        self.fuerza_destino = 0