# -*- coding: utf-8 -*-

# Assumes all weights are 1, or
# the vertex degree, which does not
# make a difference

# Similar to minimum size,
# but keep the leaf. Leaf have
# a degree of 1 (edge to parent), while other vertices
# have at least 2 and at most 3.
# In some cases keeping leaf or parent
# leads to the same weight, i.e: if the
# tree has just 2 vertices
# or it's like a link-list,
# or it has just one sub-tree


# 1. start from leafs, add them to new graph
# 2. skip their parents, but make
#    those parent's parents the leafs
# 3. recurse

# runtime O(V)
# untested

def minimum_weight_vertex_cover_tree(tree):
    covered = Tree()
    leafs = set()
    for v in tree.children:
        if tree.children[v] == [None, None]:
            leafs.add(v)
    while leafs:
        parents = set()
        for v in leafs:
            if v in tree.parent:
                covered.insert(v, *tree.children[v])
                parents.add(tree.parent[v])
        leafs = set()
        for v in parents:
            if v in tree.parent:
                leafs.add(tree.parent[v])
    return covered

