# -*- coding: utf-8 -*-

# runtime O(V+E²)
# meh

# I don't think we can do better,
# This is very much like a BFS,
# visit all vertex, for each one
# visit their edges, for each one
# visit their edges. Using BFS directly
# would take doing BFS for each vertex
# (they may all be disconnected),
# BFS is O(V+E) but only if we avoid
# visiting the vertices and edges multiple times,
# which can't be done here


class Graph:
    def __init__(self):
        self.edge = {}

    def insert(self, x, y):
        pass


def square_adj_list(graph):
    g = Graph()
    for v in graph.edge:
        for edge in graph.edge[v]:
            for edge2 in graph.edge.get(edge, []):
                g.insert(v, edge2)
    return g
