# Clase para representar un Nodo
class Nodo:
    def __init__(self, id):
        self.id = id
        self.grado = 0
        self.x = 0
        self.y = 0
        self.conjunto = 0
        self.fuerzax = 0
        self.fuerzay = 0
    
    def __repr__(self):
        return f"{self.id}"