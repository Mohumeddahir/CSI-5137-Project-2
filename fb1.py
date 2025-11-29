import networkx as nx
import matplotlib.pyplot as plt
import community  # Python Louvain community detection library

G_fb = nx.read_edgelist("facebook_combined.txt", create_using=nx.Graph(), nodetype=int)

# Detect communities
partition = community.best_partition(G_fb)

# Set up colors for each community
colors = [partition[n] for n in G_fb.nodes()]

# Layout the graph
spring_pos = nx.spring_layout(G_fb)
plt.axis("off")

# Draw the network with node colors based on communities
nx.draw_networkx(G_fb, pos=spring_pos, with_labels=False, node_size=35,
                 node_color=colors, cmap=plt.cm.get_cmap('viridis', max(colors) + 1))

plt.show()
