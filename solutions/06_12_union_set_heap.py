# -*- coding: utf-8 -*-

from collections import defaultdict


# Operations 1, 2 and 3 are log(n)
# due to find. But there is a faster find
# in constant time, see 06_13


class SetUnion:
    def __init__(self, edges):
        self.parent = {}
        self.size = defaultdict(lambda: 1)
        self.edges = list(edges)
        self.min_edges = defaultdict(
            lambda: (float('inf'), '', ''))

    # find root of x's sub-tree
    def find(self, x):
        if self.parent.get(x, x) == x:
            return x
        return self.find(self.parent[x])

    # merge smaller set/subtree into larger set/subtree
    def union_sets(self, s1, s2, weight):
        root1 = self.find(s1)  # root of set
        root2 = self.find(s2)
        if root1 == root2:
            return  # already in same set
        # merge smaller set into root of larger set
        # to keep the same total height of the sub-tree
        if self.size[root1] >= self.size[root2]:
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
            w, x, y = self.min_edges[root1]
            if weight < w:
                self.min_edges[root1] = (weight, s1, s2)
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2
            w, x, y = self.min_edges[root2]
            if weight < w:
                self.min_edges[root2] = (weight, s1, s2)

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)

    # 1
    def merge(self, component1, component2):
        self.union_sets(component1, component2)

    # 2
    def get_component_for(self, v):
        return self.find(v)

    # 3
    def get_min_edge_for(self, component):
        v = self.find(component)
        weight, x, y = self.min_edges[v]
        assert x and y, 'Not a component'
        return x, y
