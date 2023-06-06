# -*- coding: utf-8 -*-

from collections import defaultdict


# http://www.algorist.com/algowiki/index.php/TADM2E_5.13
# algorist solution does no makes sense to me.
# A vertex cover allows picking alternated and
# adjacent vertex, but it does not allow to
# skip two adjacent vertex, because then we
# miss an edge.
# however, the solution says to "reverse the coloring"
# at some point, but the complement of a vertex cover
# may not be a vertex cover in case adjacent vertex
# were picked, because then you're skipping two vertex,
# it's a very hand-wavy explanation.

# A cover vertex must include all of the edges.
# It does no allow to skip two adjacent vertices.
# It does allow to pick alternated or adjacent vertices.

class Vertex:
    def __init__(self, label, weight, left=None, right=None):
        self.label = label
        self.weight = weight
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Vertex<%r>' % self.label


# XXX this needs a refactor :P
score = defaultdict(lambda: {False: 0, True: 0})
cover = set()

def reset():
    global score, cover
    score = defaultdict(lambda: {False: 0, True: 0})
    cover = set()

def minimum_weight_vertex_cover_tree2(v):
    if v is None:
        return
    minimum_weight_vertex_cover_tree2(v.left)
    minimum_weight_vertex_cover_tree2(v.right)
    # for leafs this is 0
    # The cost of not including this vertex
    # is the cost of including its children
    score[v][False] = sum(
        score[c][True]
        for c in (v.left, v.right)
        if c is not None)
    # for leafs this is v.weight
    # The cost of including this vertex
    # is whatever is less costly, include
    # or not to include its children, because
    # both things are allowed
    score[v][True] = v.weight + sum(
        min(score[c][True], score[c][False])
        for c in (v.left, v.right)
        if c is not None)
    if score[v][True] < score[v][False]:
        cover.add(v)
    else:
        if v.left is not None:
            cover.add(v.left)
        if v.right is not None:
            cover.add(v.right)


# Alternated case = {B, E}
# A(9)---B(3)---C(2)
#  \      \
#   E(1)   D(4)

t1 = Vertex('a', 9,
            Vertex('e', 1),
            Vertex('b', 3,
                   Vertex('d', 4),
                   Vertex('c', 2)))

reset()
minimum_weight_vertex_cover_tree2(t1)
print('t1')
print(cover)
print(dict(score))

# adjacent case = {A, B}
# A(9)---B(3)---C(2)
#  \      \
#   E(1000)   D(4)

t2 = Vertex('a', 9,
            Vertex('e', 1000),
            Vertex('b', 3,
                   Vertex('d', 4),
                   Vertex('c', 2)))

reset()
minimum_weight_vertex_cover_tree2(t2)
print('t2')
print(cover)
print(dict(score))

# mixed case = {A, B, F}
# A(9)---B(3)---C(2)
#  \      \
#   E(1000)   D(4)
#    \
#     F(1)

t3 = Vertex('a', 9,
            Vertex('e', 1000,
                   Vertex('f', 1)),
            Vertex('b', 3,
                   Vertex('d', 4),
                   Vertex('c', 2)))

reset()
minimum_weight_vertex_cover_tree2(t3)
print('t3')
print(cover)
print(dict(score))
