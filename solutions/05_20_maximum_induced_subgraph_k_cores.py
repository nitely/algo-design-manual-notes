# -*- coding: utf-8 -*-

# maximum induce sub-graph where vertices
# has at least K edges is known as k-cores
# see: https://en.wikipedia.org/wiki/Degeneracy_(graph_theory)#k-Cores

# Beware of the last sentence of the problem.
# The resulting graph must contain all edges
# that connect to a vertex within the graph,
# So excluding a vertex of less edges than K
# may make a neighbor vertex of degree equal
# to K contain less than K and be excluded as well (and so on)
#
# In other words the degree of a vertex may
# be reduced if some of its neighbors
# are not part of the induced sub-graph


# undirected graph
# runtime O(V + E)
# space O(V + E)


from collections import defaultdict


class Graph:
    def __init__(self):
        # use dict of sets because order of edges and vertices
        # does not matter, and we gain some quick O(1) lookup operations
        self.edges = defaultdict(set)

    def degree(self, v):
        return len(self.edges[v])

    def insert(self, v, edges):
        for y in edges:
            self.edges[v].add(y)
            self.edges[y].add(v)


# O(E)
def exclude_vertex(graph, v, k, degrees, excluded):
    if v in excluded:
        return
    excluded.add(v)
    for v2 in graph.edges[v]:
        if v == v2: continue  # loop
        degrees[v2] -= 1
        if degrees[v2] < k:
            exclude_vertex(graph, v2, k, degrees, excluded)


# O(V + E)
# * calculate degree of each vertex
# * calculate excluded vertices (degree < k) recursively
# * create sub-graph based on degrees >= k and included/excluded vertices
def maximum_induced_sub_graph(graph, k):
    degrees = {}
    for v in graph.edges:
        degrees[v] = graph.degree(v)
    # O(V + E)
    # may visit excluded vertex's edges once.
    excluded = set()
    for v in graph.edges:
        if degrees[v] < k:
            exclude_vertex(graph, v, k, degrees, excluded)
    # O(V + E)
    sub_graph = Graph()
    for v in graph.edges:
        if degrees[v] >= k:
            sub_graph.insert(v, graph.edges[v] - excluded)
    return sub_graph


# Crazy graph (this one is connected, but
#    the solution works for disconnected too)
#                1
#              / |  \
#             0  |   5
#              \ | / | \
#                2   |   \
#              / | \ |    8
#            4 ----- 6 - /
#            \ \ | / /
#             \  3  /
#             \  |  /
#             \  |  /
#             \  | /
#                7

g1 = Graph()
g1.insert(0, [1,2])
g1.insert(1, [0,2,5])
g1.insert(2, [0,1,5,6,3,4])
g1.insert(3, [2,6,4,7])
g1.insert(4, [2,3,6,7])
g1.insert(5, [1,2,6,8])
g1.insert(6, [2,4,5,8,3,7])
g1.insert(7, [6,3,4])
g1.insert(8, [5,6])
#print(g1.edges)

print(maximum_induced_sub_graph(g1, 3).edges)
# {
# 2: {3, 4, 6},
# 3: {2, 4, 6, 7},
# 4: {2, 3, 6, 7},
# 6: {2, 3, 4, 7},
# 7: {3, 4, 6}
# }
