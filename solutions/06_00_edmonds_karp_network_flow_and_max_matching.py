# -*- coding: utf-8 -*-

# Useful for
# * max-flow, min-cut (as shown below)
# * bipartite matching (see 06_24)
#   (max matching in bipartite graphs)

# Note for matching in general graphs
# (i.e: a non-bipartite graph with
# one or more odd-length cycles)
# we need Edmonds blossom algorithm, this
# one can't find the max matching in such graph


# runtime O(V * E²)


from collections import defaultdict, deque


class Edge:
    def __init__(self, capacity=0, flow=0):
        self.capacity = capacity
        self.flow = flow


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(dict)

    def insert(self, v, y, weight):
        self.edges[v][y] = Edge(capacity=weight)
        self.edges[y][v] = Edge()


def bfs(graph: Graph, source, sink):
    queue = deque()
    queue.appendleft(source)
    parent = {source: None}
    while queue:
        v = queue.pop()
        for y, edge in graph.edges[v].items():
            if y not in parent and edge.capacity > edge.flow:
                parent[y] = v
                queue.appendleft(y)
                if y == sink:
                    return parent
    return parent


def edmonds_karp(graph: Graph, source, sink):
    edges = graph.edges
    flow = 0
    # At least one edge becomes saturated on each iteration
    while True:
        # Find augmentation path (shortest path with available capacity)
        # O(E) time
        parent = bfs(graph, source, sink)
        if sink not in parent:
            s = set(parent)
            t = set(graph.vertices) - set(parent)
            print('S', s)
            print('T', t)
            print('cut', min_cut(graph, s, t))
            break
        print('path', path(parent, sink))
        # Backtrack search
        # Calculate how much can be sent
        delta_flow = float('inf')
        v, y = parent[sink], sink
        while v:
            delta_flow = min(delta_flow, edges[v][y].capacity - edges[v][y].flow)
            v, y = parent[v], v
        # Update edges by that amount
        v, y = parent[sink], sink
        while v:
            edges[v][y].flow += delta_flow
            edges[y][v].flow -= delta_flow
            v, y = parent[v], v
        flow += delta_flow
    return flow


def path(parent, v):
    p = []
    while v:
        p.append(v)
        v = parent[v]
    p.reverse()
    return p


def min_cut(graph, s, t):
    cut = set()
    for v in graph.edges:
        for y in graph.edges[v]:
            # I used to check S-T or T-S, but since we added
            # back edges, checking just one suffices
            if v in s and y in t:
                #if graph.edges[v][y].flow > 0:  # see note at the bottom
                cut.add((v, y))
    return cut



# Beware the output paths rely on
# the edge order, ie: a, d, f, g as first
# path would also be valid, and end with
# a total flow of 5 all the same
g1 = Graph('abcdefg')
g1.insert('a', 'b', 3)
g1.insert('a', 'd', 3)
g1.insert('b', 'c', 4)
g1.insert('c', 'a', 3)
g1.insert('c', 'd', 1)
g1.insert('c', 'e', 2)
g1.insert('d', 'e', 2)
g1.insert('d', 'f', 6)
g1.insert('e', 'b', 1)
g1.insert('e', 'g', 1)
g1.insert('f', 'g', 9)
print(edmonds_karp(g1, 'a', 'g'))
# path ['a', 'd', 'e', 'g']
# path ['a', 'd', 'f', 'g']
# path ['a', 'b', 'c', 'd', 'f', 'g']
# path ['a', 'b', 'c', 'e', 'd', 'f', 'g']
# S {'a', 'e', 'b', 'c'}
# T {'g', 'f', 'd'}
# cut {('c', 'd'), ('a', 'd'), ('d', 'e'), ('e', 'g')}
# 5

# ^note according to wikipedia (d, e) should not be in the cut (as it's not saturated?)
#  however, the min-cut theorem does say the cut must disconnect source from sink
#  but maybe on the residual graph
