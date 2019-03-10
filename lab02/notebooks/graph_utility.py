import networkx as nx
import numpy as npy

def histogram(data):
    return sorted(list(set([(d, data.count(d)) for d in data])), key=lambda x : x[0])


def numberOfNodesHops(start, r, G):
    neighbors = set([start])
    for i in range(r):
        neighbors = set([neighbor for node in neighbors \
                     for neighbor in G[node]])
    return neighbors
