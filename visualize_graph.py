from pycsp3 import *
import matplotlib as mpl
import networkx as nx
import matplotlib.pyplot as plt

n, e = data

#print(e, n)
G = nx.DiGraph()

seed = 10  # Seed random number generators for reproducibility
G.add_edges_from(e)
pos = nx.spring_layout(G, seed=seed)

node_sizes = [20 + 10 * i for i in range(len(G))]
M = G.number_of_edges()
edge_colors = range(2, M + 2)
edge_alphas = [(5 + i) / (M + 4) for i in range(M)]
cmap = plt.cm.plasma

nodes = nx.draw_networkx_nodes(G, pos, node_size=400, node_color="indigo")
edges = nx.draw_networkx_edges(
    G,
    pos,
    node_size=node_sizes,
    arrowstyle="->",
    arrowsize=10,
    edge_color=edge_colors,
    edge_cmap=cmap,
    width=2,
)
labels = nx.draw_networkx_labels(G,pos, font_size=12, font_color="white")

# set alpha value for each edge
for i in range(M):
    edges[i].set_alpha(edge_alphas[i])

#pc = mpl.collections.PatchCollection(edges, cmap=cmap)
#pc.set_array(edge_colors)

ax = plt.gca()
ax.set_axis_off()
#plt.colorbar(pc, ax=ax)
plt.show()