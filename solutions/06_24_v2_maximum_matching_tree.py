# -*- coding: utf-8 -*-

# Dynamic programming solution

# runtime O(n)


from collections import defaultdict


class Vertex:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Vertex<%r>' % self.label


def max_matching(v: Vertex):
    # edge cost
    score = defaultdict(lambda: {False: 0, True: 0})
    matching = set()
    def _max_matching(v: Vertex):
        if v is None:
            return
        _max_matching(v.left)
        _max_matching(v.right)
        # cost of not including edges to children
        score[v][False] = sum(
            max(score[y][False], score[y][True])
            for y in (v.left, v.right))
        # max of: 1 edge to y + cost of y without edges + max cost of remaining children
        score[v][True] = max(
            (1 + score[y][False] + sum(
                max(score[x][False], score[x][True])
                for x in (v.left, v.right)
                if x != y)
             for y in (v.left, v.right)
             if y is not None), default=0)
        # add matching vertex from score[v][True] to maximum matching
        if score[v][True] > score[v][False]:
            total_cost = float('-inf')
            edge = ''
            for y in (v.left, v.right):
                cost = score[y][False] + sum(
                    max(score[x][False], score[x][True])
                    for x in (v.left, v.right)
                    if x != y)
                if cost > total_cost:
                    total_cost = cost
                    edge = y
            matching.add((v, edge))
    _max_matching(v)
    print(matching)
    return max(score[v][True], score[v][False])


# A---B---C
#  \   \
#   E   D

t1 = Vertex('a',
            Vertex('e'),
            Vertex('b',
                   Vertex('d'),
                   Vertex('c')))
print(max_matching(t1))
# {(a, e), (b, d)}
# 2

t2 = Vertex('a',
            Vertex('b',
                   Vertex('c'),
                   Vertex('d')),
            Vertex('e',
                   Vertex('f'),
                   Vertex('g',
                          Vertex('h'),
                          Vertex('i'))))
print(max_matching(t2))
# {(g, h), (b, c), (e, f)}
# 3

t3 = Vertex('a',
            Vertex('b'))
print(max_matching(t3))
# 1

t4 = Vertex('a',
            Vertex('b',
                   Vertex('c')))
print(max_matching(t4))
# 1

t5 = Vertex('a',
            Vertex('b',
                   Vertex('c',
                          Vertex('d'))))
print(max_matching(t5))
# 2
