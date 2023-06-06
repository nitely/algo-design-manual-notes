# -*- coding: utf-8 -*-

# A stripe follows the red vertex through the dotted red edges,
# each red vertex has a triangle. Two adjacent triangles
# (sharing two black vertex) are related by the red edge.
# This forms a dual-graph.
# We know the number of red vertices (it's the same as num of
# triangles) and the triangles black vertices. We must check
# if two of the black vertices are in the dual-graph,
# if they are, then add an edge between that triangle/red-vertex
# and the new triangle/red-vertex, we add 3 edges at most (since
# there are at most 3 adjacent triangles)

# We must avoid checking each red vertex each time
# we add a new triangle, otherwise the time is quadratic
# in the number of triangles/red-vertices


from collections import defaultdict


# runtime O(n) in the number of triangles/red-vertices


class RedVertex:
    def __init__(self, label, triangle):
        self.label = label
        self.triangle = triangle

    def __repr__(self):
        return 'RedVertex<label(%r); triangle(%r)>' % (self.label, self.triangle)


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = defaultdict(lambda: [])
        self.triangles = {}
        self.fragments = {}  # extra O(3m) (num of triangles) space

    def _create_red_vertex(self, triangle):
        v = RedVertex(
            label=len(self.vertices) + 1,
            triangle=triangle)
        self.vertices.append(v)
        return v.label

    def insert_edge(self, x, y, directed=False):
        self.edges[x].append(y)
        if not directed:
            self.insert_edge(y, x, directed=True)

    # self.fragments[pair] at any given time
    # may have nothing, a triangle/red-vertex, or
    # the next triangle/red-vertex in the strip
    def insert(self, triangle):
        v = self._create_red_vertex(triangle)
        a, b, c = sorted(triangle)  # O(3log3) is a constant
        # Make sure *each* pair is in asc order "a < b < c"
        for pair in ((a, b), (b, c), (a, c)):
            if pair in self.fragments:
                assert len(self.edges[v]) < 3, (
                    'Triangle connections maxed-out (max is 3)')
                assert v != self.fragments[pair], (
                    'Duplicated or overlapped triangle')
                self.insert_edge(v, self.fragments[pair])
            else:
                self.fragments[pair] = v


triangles = [
    (0, 1, 3), # next to prev and next
    (1, 2, 3), # next to prev and next
    (2, 3, 4), # next to prev and next
    (3, 4, 5), # next to prev

    (0, 3, 6),  # next to 0
    (0, 1, 7)  # next to 0
]

g = Graph()
for triangle in triangles:
    g.insert(triangle)

print(dict(g.edges))
# {0: [1, 4, 5], 1: [0, 2], 2: [1, 3], 3: [2], 4: [0], 5: [0]}
print(len(g.vertices))

assert len(g.edges) == len(triangles)
