import networkx as nx
import matplotlib.pyplot as plt

# Crie um grafo direcionado
G = nx.DiGraph()

# Adicione nós e arestas
G.add_nodes_from(['Input1', 'Input2', 'Hidden1', 'Hidden2', 'Output'])

# Adicione arestas conectando as camadas
G.add_edges_from([('Input1', 'Hidden1'), ('Input1', 'Hidden2'),
                  ('Input2', 'Hidden1'), ('Input2', 'Hidden2'),
                  ('Hidden1', 'Output'), ('Hidden2', 'Output')])

# Defina a posição dos nós por camada
pos = {'Input1': (0, 2), 'Input2': (0, 1), 'Hidden1': (1, 2), 'Hidden2': (1, 1), 'Output': (2, 1)}

# Desenhe o grafo
nx.draw_networkx(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=10, font_color="black", font_weight="bold", arrowsize=20)

# Adicione rótulos para as arestas (opcional)
labels = {('Input1', 'Hidden1'): 'Edge 1', ('Input1', 'Hidden2'): 'Edge 2',
          ('Input2', 'Hidden1'): 'Edge 3', ('Input2', 'Hidden2'): 'Edge 4',
          ('Hidden1', 'Output'): 'Edge 5', ('Hidden2', 'Output'): 'Edge 6'}

nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Mostre o gráfico
plt.show()
