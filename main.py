import graph_tool.all as gt
import pandas as pd
import numpy as np

# Carregue os dados (substitua pelo caminho do seu arquivo CSV)
df = pd.read_csv('data/C34-1522.csv', sep=',')

# Crie um grafo bipartido
g = gt.Graph(directed=False)

# Adicione as camadas de municípios, procedimentos e hospitais
municipios = g.add_edge_list(df[['MUNIC_RES', 'PROC_REA']].values, hashed=True, eprops=[('weight', g.new_edge_property('int'))])
procedimentos = g.add_edge_list(df[['PROC_REA', 'CNES']].values, hashed=True, eprops=[('weight', g.new_edge_property('int'))])

# Ajuste os tamanhos dos vértices de acordo com o grau
municipio_size = g.new_vertex_property('int')
procedimento_size = g.new_vertex_property('int')
hospital_size = g.new_vertex_property('int')

municipio_size.a = np.array([v.in_degree() for v in municipios[0]])
procedimento_size.a = np.array([v.out_degree() for v in procedimentos[0]])
hospital_size.a = np.array([v.in_degree() for v in procedimentos[1]])

# Ajuste os rótulos dos vértices
municipio_label = g.vp['label'] = g.new_vertex_property('string')
procedimento_label = g.vp['label'] = g.new_vertex_property('string')
hospital_label = g.vp['label'] = g.new_vertex_property('string')

municipio_label.a = df['MUNIC_RES'].values
procedimento_label.a = df['PROC_REA'].values
hospital_label.a = df['CNES'].values

# Posicione os vértices em um layout bipartido
pos = gt.radial_tree_layout(g, procedimentos[0], weighted=True)

# Desenhe o grafo
gt.graph_draw(
    g,
    pos=pos,
    vertex_text=g.vp['label'],
    vertex_size=gt.prop_to_size(municipio_size, mi=5, ma=15),
    vertex_fill_color='blue',
    vertex_font_size=10,
    edge_pen_width=gt.prop_to_size(g.ep['weight'], mi=0.1, ma=2),
    output_size=(800, 800),
    output='graph.png'
)
