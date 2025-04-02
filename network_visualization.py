import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network

G = nx.read_edgelist("combined_network.txt")
g = Network(height=1000, width=2000)
g.toggle_hide_edges_on_drag(False)
g.barnes_hut()
g.from_nx(G)
g.show("graph.html", notebook=False)
