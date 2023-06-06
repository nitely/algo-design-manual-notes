# -*- coding: utf-8 -*-

# Runtime is O(V + E) linear in the number of vertex + edges
# Space is O(V + E) to add all edges and the alternated vertices

# Problem 02 and 03 have the same solution,
# but the return value is based on the
# weight instead of the number of vertices,
# since independent-set only allows alternated
# vertices to be picked

# This is a two-color solution,
# we color the tree of alternated
# colors per tree level
# and pick the color with the greatest
# number of vertices

from collections import deque


class Vertex:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Vertex<%r>' % self.label

    def children(self):
        if self.left is not None:
            yield self.left
        if self.right is not None:
            yield self.right


# BFS, two-color
def maximum_size_independent_set(v: Vertex):
    independent_set_red = set()
    independent_set_black = set()
    colors = [independent_set_red, independent_set_black]
    queue = deque([(v, 0)])
    colors[0].add(v)
    while queue:
        v, color = queue.pop()
        color_complement = (color+1) % len(colors)
        for c in v.children():
            queue.appendleft((c, color_complement))
            colors[color_complement].add(c)
    return max(*colors, key=lambda x: len(x))


t1 = Vertex('a',
            Vertex('b',
                   Vertex('c'),
                   Vertex('d')),
            Vertex('e',
                   Vertex('f',
                          Vertex('g'))))

print(maximum_size_independent_set(t1))
# {Vertex<'f'>, Vertex<'c'>, Vertex<'d'>, Vertex<'a'>}

t2 = Vertex('a',
            Vertex('b',
                   #Vertex('c'),
                   Vertex('d')),
            Vertex('e',
                   Vertex('f',
                          Vertex('g'),
                          Vertex('h'))))

print(maximum_size_independent_set(t2))
# {Vertex<'e'>, Vertex<'g'>, Vertex<'b'>, Vertex<'h'>}
