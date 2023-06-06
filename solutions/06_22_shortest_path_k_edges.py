# -*- coding: utf-8 -*-

# Notice if we were not allowed to include cycles
# in the path (i.e: the path must be simple),
# then the problem would be NP-complete
# as there is a Hamiltonian path reduction to this
# problem

# We can create a tree of possibilities of depth
# K, however the tree grows exponentially O(E^K)
# (thanks to cycles), then find the shortest path.

# There is a simple solution using Bellman–Ford algorithm.
#
# Notice all weights are negative, so we don't worry about
# negative cycles. Otherwise, we would have to run a full
# bellman-ford, store the path when we reach K+1, and keep
# going to complete it and check if there is a (negative) cycle in the
# last iteration
#
# ^ this finds a path of *at most* K edges, not *exactly* K edges,
# that can only be done by pruning the tree, instead of storing
# every possible path, which requires dynamic programming (next chapter)

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, y, weight):
        self.edges[v].add((y, weight))


# runtime O(K*E) *at most* k edges
def find_shortest_path_k_edges(graph, source, destination, k):
    parent = {}
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    for i in range(k+1):  # k edges must include k+1 vertices
        # all edges
        for v in graph.edges:
            for y, weight in graph.edges[v]:
                alt = dist[v] + weight
                if alt < dist[y]:
                    dist[y] = alt
                    parent[y] = (weight, v)
    return parent


# return path to v
def path_to(spt, v):
    if v not in spt:
        return []
    path = []
    while v in spt:
        weight, y = spt[v]
        path.append((weight, v))
        v = y
    path.append((0, v))
    path.reverse()
    return path


#  A--10-->B--
#  | \        |
#  2  3       |
#  |   \      |
#  v     v    7
#  D<--6--C   |
#  ^          |
#  |          |
#   ----------

g1 = Graph('abcd')
g1.insert('a', 'b', 10)
g1.insert('a', 'c', 3)
g1.insert('a', 'd', 2)
g1.insert('b', 'd', 7)
g1.insert('c', 'd', 6)
# k = 2, source=a, destination=d, paths {a, c, d}=9 and {a, b, d}=17
p1 = find_shortest_path_k_edges(g1, 'a', 'd', k=2)
#print(p1)
print(path_to(p1, 'd'))
#[(0, 'a'), (3, 'c'), (6, 'd')]
# ^wrong, because the algo return *at most* k edges.


p1 = find_shortest_path_k_edges(g1, 'a', 'd', k=1)
#print(p1)
print(path_to(p1, 'd'))
# [(0, 'a'), (2, 'd')]
