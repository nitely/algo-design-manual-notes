# -*- coding: utf-8 -*-


# Assume undirected tree
# 1. traverse leafs and mark them removed
# 2. traverse their parent, add them to new graph
# and mark them removed, their parents are
# now leafs, repeat


# Apparently there's a DP solution that
# starts from the root instead of the leafs,
# since Skiena has not explained that yet,
# I assume that's not the way this should be solved


# runtime O(V)
# untested


class Tree:
    def __init__(self):
        self.children = {}
        self.parent = {}

    def insert(self, v, x=None, y=None):
        self.children[v] = [x, y]
        if x is not None:
            self.parent[x] = v
        if y is not None:
            self.parent[y] = v


def minimum_vertex_cover_tree(tree):
    covered = Tree()
    leafs = set()
    for v in tree.children:
        if tree.children[v] == [None, None]:
            leafs.add(v)
    while leafs:
        parents = set()
        for v in leafs:
            if v in tree.parent:  # root has no parent
                parent = tree.parent[v]
                # XXX parent back-edge is not added,
                #     is it needed?
                covered.insert(parent, *tree.children[parent])
                parents.add(parent)
        leafs = set()
        for v in parents:
            if v in tree.parent:  # root has no parent
                leafs.add(tree.parent[v])
    return covered
