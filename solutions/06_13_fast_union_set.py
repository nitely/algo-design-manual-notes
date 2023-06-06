# -*- coding: utf-8 -*-

from collections import defaultdict


# Complexity of Path compression + Halved union by size
# makes the algorithm run in constant time.
# Well, in O(A(n)) where A is the
# inverse Ackermann function, which is less
# than the constant 5.


# This will allow "m" unions on a set of n elements
# and "m" finds in constant time. Making a total
# runtime of O(m)
#
# But where is the O(n) time? union-set usually needs
# O(n) time to initialize it, however this one requires
# no initialization. With initialization, this would take
# O(n+m)


class SetUnion:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(lambda: 1)

    # Path compression
    # function Find(x)
    #  if x.parent != x
    #    x.parent := Find(x.parent)
    #  return x.parent

    # Path compression
    # find root of x's sub-tree
    def find(self, x):
        if self.parent.get(x, x) != x:
            self.parent = self.find(self.parent[x])
        return self.parent.get(x, x)

    # Halved union by size
    # merge smaller set/subtree into larger set/subtree
    def union_sets(self, s1, s2):
        root1 = self.find(s1)  # root of set
        root2 = self.find(s2)
        if root1 == root2:
            return  # already in same set
        # merge smaller set into root of larger set
        # to keep the same total height of the sub-tree
        if self.size[root1] >= self.size[root2]:
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)

