# -*- coding: utf-8 -*-

# This requires reversing every edge
# and then find the shortest path to
# every vertex
# For a weighed graph it's Dijkstra's SP algo,
# for unweighted graphs it's just a BFS (Dijkstra
# using a priority queue is a BFS on
# unweighted graphs)

# This assumes an unweighted graph

from collections import deque, defaultdict


class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def insert(self, v, edges):
        for y in edges:
            self.edges[v].append(y)

    def reversed(self):
        g = Graph()
        edges = defaultdict(list)
        for v in self.edges:
            for y in self.edges[v]:
                edges[y].append(v)
        g.edges = edges
        return g


# BFS
def single_destination_shortest_path(graph: Graph, v: str):
    graph = graph.reversed()
    queue = deque()
    discovered = set()
    parent = {}
    queue.appendleft(v)
    discovered.add(v)
    while queue:
        v = queue.pop()
        for y in graph.edges[v]:
            if y in discovered:
                continue
            discovered.add(y)
            queue.appendleft(y)
            parent[y] = v
    return parent


# Figure 6.3
g1 = Graph()
g1.insert('a', ['b', 'c', 'd'])
g1.insert('b', ['e', 'c'])
g1.insert('c', ['d', 'e', 'f'])
g1.insert('d', ['f'])
g1.insert('e', ['f', 'g'])
g1.insert('f', ['g'])
print(single_destination_shortest_path(g1, 'g'))
# {'e': 'g', 'f': 'g', 'b': 'e', 'c': 'e', 'd': 'f', 'a': 'b'}
# ^ This is a MST, there may be multiple MST for a given graph.
