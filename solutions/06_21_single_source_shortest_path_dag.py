# -*- coding: utf-8 -*-

# Runtime O(V+E)
# Iterate each vertex in topological order
# (flat/linear graph order)
# and calculate accumulated distance to every
# adjacent vertex, no backtracking required since
# the order is topological

# Changing sign on each edge (ie: multiply by -1)
# will find the longest path (DAG is the only graph
# in which the problem is *not* NP-hard)

# Calculating weight instead of total distance
# would find the MST

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges):
        for y, weight in edges:
            self.edges[v].add((y, weight))


# DFS, topological order
def find_topological_order(graph):
    discovered = set()
    processed = set()
    topological_order = []
    def _traverse(graph, v):
        discovered.add(v)
        for y, _weight in graph.edges[v]:
            if y not in discovered:  # tree-edge
                _traverse(graph, y)
            elif y not in processed:  # cycle
                assert False, 'back-edge found, not a DAG'
        processed.add(v)
        topological_order.append(v)
    for v in graph.vertices:
        if v in discovered:
            continue
        _traverse(graph, v)
    topological_order.reverse()
    return topological_order


# return SPT
def find_shortest_path(graph, start):
    topological_order = find_topological_order(graph)
    print('topological order', topological_order)
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    parent = {}
    for v in topological_order:
        for y, weight in graph.edges[v]:
            #dist[y] = min(dist[y], dist[v] + weight)
            if dist[y] > dist[v] + weight:
                dist[y] = dist[v] + weight
                parent[y] = (weight, v)
    print('distances to %r' % start, dict(dist))
    print('path', parent)
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


# Figure 6.3, but custom directed version
g1 = Graph('abcdefg')
g1.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g1.insert('b', [('e', 7), ('c', 9)])
g1.insert('c', [('d', 4), ('e', 4), ('f', 3)])
g1.insert('d', [('f', 7)])
g1.insert('e', [('f', 2), ('g', 5)])
g1.insert('f', [('g', 2)])
p1 = find_shortest_path(g1, 'a')
print(path_to(p1, 'g'))
print(path_to(p1, 'b'))
