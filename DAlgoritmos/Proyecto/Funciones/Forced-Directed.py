import pygame
import math
import random
import re

# Configuración de Pygame
WIDTH, HEIGHT = 1000, 800
BACKGROUND_COLOR = (30, 30, 30)
NODE_COLOR = (100, 200, 255)
EDGE_COLOR = (200, 200, 200)
FPS = 60

# Parámetros del algoritmo de Fruchterman-Reingold
AREA = WIDTH * HEIGHT  # Área total de la ventana
K = math.sqrt(AREA / 50)  # Constante para calcular fuerzas
C = 0.7  # Factor de enfriamiento
TEMP = WIDTH / 10  # Temperatura inicial
ITERATIONS = 500  # Número de iteraciones

class Graph:
    def __init__(self, nodes, edges):
        self.nodes = nodes
        self.edges = edges
        self.positions = {node: [random.randint(50, WIDTH-50), random.randint(50, HEIGHT-50)] for node in nodes}
        self.forces = {node: [0, 0] for node in nodes}
        self.temperature = TEMP  # Temperatura inicial

    def reset_forces(self):
        """Reiniciar las fuerzas de los nodos."""
        for node in self.nodes:
            self.forces[node] = [0, 0]

    def calculate_forces(self):
        """Calcula las fuerzas atractivas y repulsivas en el grafo."""
        self.reset_forces()

        # Fuerzas repulsivas entre todos los nodos
        for u in self.nodes:
            for v in self.nodes:
                if u != v:
                    dx = self.positions[u][0] - self.positions[v][0]
                    dy = self.positions[u][1] - self.positions[v][1]
                    dist = math.sqrt(dx**2 + dy**2) or 0.1  # Evitar división por cero
                    repulsive_force = (K**2) / dist
                    self.forces[u][0] += repulsive_force * (dx / dist)
                    self.forces[u][1] += repulsive_force * (dy / dist)

        # Fuerzas atractivas en las aristas
        for u, v in self.edges:
            dx = self.positions[v][0] - self.positions[u][0]
            dy = self.positions[v][1] - self.positions[u][1]
            dist = math.sqrt(dx**2 + dy**2) or 0.1
            attractive_force = (dist**2) / K
            self.forces[u][0] += attractive_force * (dx / dist)
            self.forces[u][1] += attractive_force * (dy / dist)
            self.forces[v][0] -= attractive_force * (dx / dist)
            self.forces[v][1] -= attractive_force * (dy / dist)

    def update_positions(self):
        """Actualiza la posición de los nodos usando las fuerzas calculadas."""
        for node in self.nodes:
            dx = self.forces[node][0]
            dy = self.forces[node][1]
            dist = math.sqrt(dx**2 + dy**2) or 0.1

            # Limitar el desplazamiento con la temperatura
            self.positions[node][0] += (dx / dist) * min(abs(dx), self.temperature)
            self.positions[node][1] += (dy / dist) * min(abs(dy), self.temperature)

            # Limitar las posiciones al área de la ventana
            self.positions[node][0] = min(WIDTH-50, max(50, self.positions[node][0]))
            self.positions[node][1] = min(HEIGHT-50, max(50, self.positions[node][1]))

        # Reducir la temperatura gradualmente
        self.temperature *= C

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
                nodes.add(u)
                nodes.add(v)
    return list(nodes), edges

def main(file_path):
    # Parsear el archivo .gv
    nodes, edges = parse_gv_file(file_path)
    print(f"Nodos: {len(nodes)}, Aristas: {len(edges)}")

    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Force-directed Layout (Fruchterman-Reingold)")
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

        # Ejecutar el algoritmo Fruchterman-Reingold
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
    file_path = "graph.gv"
    main(file_path)
