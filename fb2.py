import networkx as nx
import matplotlib.pyplot as plt
import community # this matches the blog
G_fb = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph(), nodetype=int)
# 1. Find communities (Louvain)
parts = community.best_partition(G_fb) # dict: node -> community id
values = [parts[node] for node in G_fb.nodes()] # list of community ids
# 2. Choose a layout (spring layout like in the article)
pos = nx.spring_layout(G_fb, k=0.1, iterations=100, seed=7)
# 3. Draw the graph
plt.figure(figsize=(8, 6))
nx.draw_networkx_edges(
G_fb,
pos,
alpha=0.3,
width=0.5
)
nx.draw_networkx_nodes(
G_fb,
pos,
node_size=20,
node_color=values,
cmap=plt.cm.jet, # multicolour like the screenshot
linewidths=0
)

plt.axis("off")
plt.tight_layout()
plt.show()