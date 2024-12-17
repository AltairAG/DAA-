import pygame
import math
import random
import re

# Configuración de Pygame
WIDTH, HEIGHT = 1000, 800
BACKGROUND_COLOR = (30, 30, 30)
NODE_COLOR = (100, 200, 255)
EDGE_COLOR = (200, 200, 200)
FPS = 144

# Parámetros del algoritmo Spring
C1 = 1      # Constante de atracción
C2 = 200      # Constante de repulsión
C3 = 1   # Factor de movimiento
ITERATIONS = 500  # Número de iteraciones

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.positions = {node: [random.randint(100, WIDTH-100), random.randint(100, HEIGHT-100)] for node in nodes}
        self.forces = {node: [0, 0] for node in nodes}

    def reset_forces(self):
        """Reiniciar las fuerzas de los nodos."""
        for node in self.nodes:
            self.forces[node] = [0, 0]

    def calculate_forces(self):
        """Calcula las fuerzas de atracción y repulsión entre nodos."""
        self.reset_forces()

        # Fuerzas de repulsión entre todos los nodos
        for u in self.nodes:
            for v in self.nodes:
                if u != v:
                    dx = self.positions[u][0] - self.positions[v][0]
                    dy = self.positions[u][1] - self.positions[v][1]
                    dist = max(math.sqrt(dx**2 + dy**2), 0.1)
                    repulsion = C2 / dist**2
                    self.forces[u][0] += repulsion * (dx / dist)
                    self.forces[u][1] += repulsion * (dy / dist)

        # Fuerzas de atracción en las aristas
        for u, v in self.edges:
            dx = self.positions[v][0] - self.positions[u][0]
            dy = self.positions[v][1] - self.positions[u][1]
            dist = max(math.sqrt(dx**2 + dy**2), 0.1)
            attraction = C1 * math.log(dist)
            self.forces[u][0] += attraction * (dx / dist)
            self.forces[u][1] += attraction * (dy / dist)
            self.forces[v][0] -= attraction * (dx / dist)
            self.forces[v][1] -= attraction * (dy / dist)

    def update_positions(self):
        """Actualiza la posición de los nodos usando las fuerzas calculadas."""
        for node in self.nodes:
            self.positions[node][0] += C3 * self.forces[node][0]
            self.positions[node][1] += C3 * self.forces[node][1]

            # Limitar las posiciones al área de la ventana
            self.positions[node][0] = min(WIDTH-50, max(50, self.positions[node][0]))
            self.positions[node][1] = min(HEIGHT-50, max(50, self.positions[node][1]))

    def draw(self, screen):
        """Dibuja el grafo en la pantalla."""
        # Dibujar aristas
        for u, v in self.edges:
            pygame.draw.line(screen, EDGE_COLOR, self.positions[u], self.positions[v], 1)
        # Dibujar nodos
        for node in self.nodes:
            pygame.draw.circle(screen, NODE_COLOR, (int(self.positions[node][0]), int(self.positions[node][1])), 8)

def parse_gv_file(file_path):
    """Parsea un archivo .gv y extrae nodos y aristas."""
    nodes = set()
    edges = []
    with open(file_path, 'r') as file:
        for line in file:
            # Buscar nodos
            node_match = re.match(r'^\s*(\d+);', line)
            if node_match:
                nodes.add(int(node_match.group(1)))

            # Buscar aristas
            edge_match = re.match(r'^\s*(\d+)\s*--\s*(\d+);', line)
            if edge_match:
                u, v = int(edge_match.group(1)), int(edge_match.group(2))
                edges.append((u, v))
    return list(nodes), edges

def main(file_path):
    # Parsear el archivo .gv
    nodes, edges = parse_gv_file(file_path)
    print(f"Nodos: {len(nodes)}, Aristas: {len(edges)}")

    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Spring Layout desde archivo .gv")
    clock = pygame.time.Clock()

    # Crear el grafo
    graph = Graph(nodes, edges)

    # Bucle principal
    running = True
    iterations = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Ejecutar el algoritmo Spring
        if iterations < ITERATIONS:
            graph.calculate_forces()
            graph.update_positions()
            iterations += 1

        # Dibujar el grafo
        screen.fill(BACKGROUND_COLOR)
        graph.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    # Ruta del archivo .gv
    file_path = "C:\\Users\\Personal\\Desktop\\Repositorio\\DAlgoritmos\\Proyecto\\Archivos\\Proyecto5\\BarabasiAlbert\\Spring\\500Nodos\\BarabasiAlbert.gv"  # Reemplazar con la ruta del archivo .gv
    main(file_path)


