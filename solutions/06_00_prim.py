# -*- coding: utf-8 -*-

from collections import defaultdict

# Prim's algorithm (from the book)
# runtime O(n²)
# space O(n)
#
# Same as dijkstra, there is a O(E+V*log(V))
# runtime version, but needs heap.decrease_priority()

# Same as dijkstra, except it adds
# the vertex of min weight each time,
# instead of min distance


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges, directed=False):
        for y, weight in edges:
            self.edges[v].add((y, weight))
            if not directed:
                self.insert(y, [(v, weight)], directed=True)

#
# Prim-MST(G)
#  Select an arbitrary vertex s to start the tree from.
#  While (there are still nontree vertices)
#   Select the edge of minimum weight between a tree and nontree vertex
#   Add the selected edge and vertex to the tree T prim .
#

# from book
def prim(graph, start):
    # is in MST
    in_tree = defaultdict(lambda: False)
    # cost of adding to tree
    distance = defaultdict(lambda: float('inf'))
    # to construct the MST
    parent = defaultdict(lambda: None)

    distance[start] = 0
    v = start
    while not in_tree[v]:
        print('Inserted vertex=%r' % v)
        in_tree[v] = True
        for y, weight in graph.edges[v]:
            if distance[y] > weight and not in_tree[y]:
                distance[y] = weight
                parent[y] = v
        # select edge of min weight
        v = start
        dist = float('inf')
        for y in graph.vertices:
            if not in_tree[y] and dist > distance[y]:
                dist = distance[y]
                v = y

    return dict(parent)


# runtime (V²)
def prim2(graph, start):
    parent = {}
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    queue = set(graph.vertices)
    while queue:
        _, v = min((dist[v], v) for v in queue)
        queue.remove(v)
        for y, weight in graph.edges[v]:
            if y not in queue:
                continue
            if weight < dist[y]:
                dist[y] = weight
                parent[y] = v
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

print(prim2(g1, start='a'))
