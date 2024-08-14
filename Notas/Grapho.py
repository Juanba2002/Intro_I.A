import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos con atributos
G.add_node(1, label='A')
G.add_node(2, label='B')
G.add_node(3, label='C')

# Agregar aristas con atributos
G.add_edge(1, 2, weight=4.5)
G.add_edge(1, 3, weight=2.3)
G.add_edge(2, 3, weight=1.7)

# Dibujar el grafo con etiquetas y pesos de aristas
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.show()

#Grafo estado-accion
# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (estados)
G.add_node('A', description='Estado Inicial')
G.add_node('B', description='Estado B')
G.add_node('C', description='Estado C')
G.add_node('D', description='Estado Objetivo')

# Agregar aristas (acciones)
G.add_edge('A', 'B', action='Ir a B', cost=1)
G.add_edge('A', 'C', action='Ir a C', cost=2)
G.add_edge('B', 'D', action='Ir a D', cost=4)
G.add_edge('C', 'D', action='Ir a D', cost=1)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')

# Dibujar etiquetas de aristas
edge_labels = nx.get_edge_attributes(G, 'action')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()

import networkx as nx

# Crear un grafo dirigido
G = nx.DiGraph()

# Agregar nodos (estados)
G.add_node('A', description='Estado Inicial')
G.add_node('B', description='Estado B')
G.add_node('C', description='Estado C')
G.add_node('D', description='Estado Objetivo')
G.add_node('E', description='Estado E')

# Agregar aristas (acciones)
G.add_edge('A', 'B', action='Ir a B', cost=1)
G.add_edge('A', 'C', action='Ir a C', cost=2)
G.add_edge('B', 'D', action='Ir a D', cost=4)
G.add_edge('C', 'D', action='Ir a D', cost=1)
G.add_edge('C', 'E', action='Ir a E', cost=3)

# Función de búsqueda en profundidad (DFS)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        return path
    for next_node in set(graph.neighbors(start)) - set(path):
        new_path = dfs(graph, next_node, goal, path + [next_node])
        if new_path:
            return new_path
    return None

# Buscar un camino de 'A' a 'D'
path = dfs(G, 'A', 'D')
print("Camino de A a D:", path)

# Dibujar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_color='black')

# Dibujar etiquetas de aristas
edge_labels = nx.get_edge_attributes(G, 'action')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()