# -*- coding: utf-8 -*-

# runtime O(m*log(m)) where m is the number of edges
#
# See 06_13 for a faster version of SetUnion,
# however, runtime of kruskal remains the same
# due to sorting the edges

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges, directed=False):
        for y, weight in edges:
            self.edges[v].add((y, weight))
            if not directed:
                self.insert(y, [(v, weight)], directed=True)

    def all_edges(self):
        return [
            (w, x, y)
            for x in self.edges
            for y, w in self.edges[x]]


# This does max log(n) finds and unions,
# because it limits the height of the tree
# by merging smallest sub-trees into larger
# sub-trees. Only when merging two trees of equal
# height the total height increments by 1, so we need to
# double the size of the tree to get a new level,
# hence log(n) operations
#
# See 06_13 for a faster version
class SetUnion:
    def __init__(self, size=0):
        #self.parent = list(range(size))  # parent element
        #self.size = [1] * size  # number of elements in subtree i
        #self.n = size  # number of elements in set
        self.parent = {}
        self.size = defaultdict(lambda: 1)

    # Slow log(n) find
    # find root of x's sub-tree
    def find(self, x):
        if self.parent.get(x, x) == x:
            return x
        return self.find(self.parent[x])

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


def kruskal_mst(graph):
    queue = graph.all_edges()
    queue.sort()
    # uncomment to get the same MST than the book
    #queue.sort(key=lambda s: (s[0], -ord(s[1])))
    queue.reverse()
    #print(queue)
    set_union = SetUnion()
    mst = []
    while queue:
        w, x, y = queue.pop()
        if not set_union.same_component(x, y):
            print('Inserted (%r, %r)' % (x, y))
            mst.append((w, x, y))
            set_union.union_sets(
                set_union.find(x), set_union.find(y))
    return mst


# Figure 6.3
g1 = Graph('abcdefg')
g1.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g1.insert('b', [('e', 7), ('c', 9)])
g1.insert('c', [('d', 4), ('e', 4), ('f', 3)])
g1.insert('d', [('f', 7)])
g1.insert('e', [('f', 2), ('g', 5)])
g1.insert('f', [('g', 2)])
# This constructs a different MST than in the book,
# because of how tie is solved (i.e: how edges are ordered),
# MST must be of 23 total weight. It's the same as
# prism coincidentally
mst1 = kruskal_mst(g1)
print(mst1)
print(sum(w for w, x, y in mst1))
#Inserted ('e', 'f')
#Inserted ('f', 'g')
#Inserted ('c', 'f')
#Inserted ('c', 'd')
#Inserted ('a', 'b')
#Inserted ('a', 'c')
#[(2, 'e', 'f'), (2, 'f', 'g'), (3, 'c', 'f'), (4, 'c', 'd'), (5, 'a', 'b'), (7, 'a', 'c')]
#23
