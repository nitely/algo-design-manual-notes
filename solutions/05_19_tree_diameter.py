# -*- coding: utf-8 -*-

# The diameter of a tree is the largest path
# from a leaf to another leaf.
# i.e: the largest path from one node
# to another.
# The common ancestor may not be the root


class Vertex:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right


def _tree_diameter(v, heights):
    if v is None:
        return 0
    left = _tree_diameter(v.left, heights)
    right = _tree_diameter(v.right, heights)
    heights[v] = left + right
    return 1 + max(left, right)  # return one more edge


def tree_diameter(v):
    heights = {}
    _tree_diameter(v, heights)
    print(list(heights.values()))
    return max(heights.values())


# Longest path is from i to m with b as common ancestor,
# 8 edges
t1 = Vertex('a',
            Vertex('b',
                   Vertex('d',
                          Vertex('f'),
                          Vertex('g',
                                 Vertex('h',
                                        None,
                                        Vertex('i')))),
                   Vertex('e',
                          None,
                          Vertex('j',
                                 Vertex('k'),
                                 Vertex('l',
                                        Vertex('m'))))),
            Vertex('c'))


print(tree_diameter(t1))
