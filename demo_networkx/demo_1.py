#!/usr/bin/env python
# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt

nodes = ["BJ", "SH", "GZ", "HZ", "NJ", "WH", "XA"]
G = nx.Graph()

for node in nodes:
    G.add_node(node)

edges = [("BJ", "SH"),
         ("BJ", "GZ"),
         ("SH", "GZ"),
         ("HZ", "SH"),
         ("HZ", "GZ"),
         ("NJ", "SH"),
         ("NJ", "BJ"),
         ("WH", "SH"),
         ("WH", "BJ"),
         ("XA", "GZ"),
         ("XA", "BJ")
         ]

G.add_edges_from(edges)

# F = nx.petersen_graph()
# subax1 = plt.subplot(121)
# nx.draw(F, with_labels=True, font_weight='bold')
# subax2 = plt.subplot(122)
# nx.draw_shell(F, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
# plt.show()


subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G,  with_labels=True, font_weight='bold')
plt.show()