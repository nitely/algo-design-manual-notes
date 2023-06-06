# -*- coding: utf-8 -*-

# It could be the case that a graph may
# contain more vertices than edges, if there
# are unconnected sub-components, however usually there
# should be at least the same amount of edges and
# vertices, and more likely more edges than vertices.
# However, the problem states that we can assume
# there are at least equal vertices and edges,
# which means VE dominates V²

# Another way of thinking this is as long as
# V < E, going through V + E would just be
# going through all the Edges, so just E.
# If there are less V, then E dominates,
# and if both are equal, then that's just 2E
# which is just E.

# runtime O((V+E)*V) = O(V² + VE) = O(VE)  iff V <= E  (problem hint)

from collections import defaultdict


class Graph:
    def __init__(self):
        # self.vertices is not needed, since even if we
        # allow orphan vertices, they can't be triangles
        self.edges = defaultdict(lambda: set())

    def insert(self, x, edges, directed=False):
        for y in edges:
            self.edges[x].add(y)
            if not directed:
                self.insert(y, [x], directed=True)

    # O(1)
    def has_edge(self, x, y):
        return y in self.edges[x]


# O(3*log3) = O(1)
def canonical_triangle(p1, p2, p3):
    triangle = []
    for p in (p1, p2, p3):
        triangle.append(tuple(sorted(p)))
    return tuple(sorted(triangle))


def find_triangles(graph: Graph):
    triangles = set()
    # O((V+E)*V) = O(V² + VE) = O(VE)  iff V <= E
    for v in graph.edges:
        for y in graph.edges[v]:  # first edge
            for v2 in graph.edges:
                if graph.has_edge(y, v2) and graph.has_edge(v2, v):  # second and third edge
                    triangles.add(canonical_triangle(
                        (v, y), (y, v2), (v2, v)))
    return triangles


# shared edge, edge case
#  a -- b -- c
#  \    |    /
#   \   |   /
#    \  |  /
#       d

g2 = Graph()
g2.insert('a', ['b', 'd'])
g2.insert('b', ['a', 'c'])
g2.insert('c', ['b', 'd'])
g2.insert('d', ['a', 'b', 'c'])

print(find_triangles(g2))
# {
# (('a', 'b'), ('a', 'd'), ('b', 'd')),
# (('b', 'c'), ('b', 'd'), ('c', 'd'))
# }
