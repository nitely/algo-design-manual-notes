# -*- coding: utf-8 -*-

# Runtime O(n * log(k)) where k are te edges
# Prim, but it uses a heap to select the edge
# of min weight

from collections import defaultdict
import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges, directed=False):
        for y, weight in edges:
            self.edges[v].add((y, weight))
            if not directed:
                self.insert(y, [(v, weight)], directed=True)


def prim(graph, start):
    heap = []
    in_tree = defaultdict(lambda: False)
    parent = defaultdict(lambda: None)
    distance = defaultdict(lambda: float('inf'))
    distance[start] = 0
    v = start
    while not in_tree[v]:
        in_tree[v] = True
        for y, weight in graph.edges[v]:
            if distance[y] > weight and not in_tree[y]:
                heapq.heappush(heap, (weight, y))
                distance[y] = weight
                parent[y] = v
        v = start
        while heap:
            w, y = heapq.heappop(heap)
            if not in_tree[y]:
                v = y
                break
    return dict(parent)


# Figure 6.3
g1 = Graph('abcdefg')
g1.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g1.insert('b', [('e', 7), ('c', 9)])
g1.insert('c', [('d', 4), ('e', 4), ('f', 3)])
g1.insert('d', [('f', 7)])
g1.insert('e', [('f', 2), ('g', 5)])
g1.insert('f', [('g', 2)])
print(prim(g1, start='a'))

