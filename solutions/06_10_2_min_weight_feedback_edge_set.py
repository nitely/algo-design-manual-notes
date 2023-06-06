# -*- coding: utf-8 -*-

# This uses kruskal to find the *maximum*
# spanning tree. Then it takes the
# difference of the M(ax)ST and the
# graph edges to obtain the min-weight
# feedback edge set.
# Why this works? because creating a MST
# leaves out all the edges that complete a cycle
# ie: adding any of the non-tree vertex to the MST
#     form a cycle
# We find the Max-ST to leave out all edges of
# minimal weight.
#
# If we were asked to find the max-weight feedback edge set
# then we would do the same, but finding the Min-ST instead
# of the Max-ST


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


class SetUnion:
    def __init__(self):
        self.parent = {}
        self.size = defaultdict(lambda: 1)

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
        if self.size[root1] >= self.size[root2]:
            self.size[root1] += self.size[root2]
            self.parent[root2] = root1
        else:
            self.size[root2] += self.size[root1]
            self.parent[root1] = root2

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)


def kruskal_max_spanning_tree(graph):
    queue = graph.all_edges()
    queue.sort()
    #queue.reverse()  # minimum
    #print(queue)
    set_union = SetUnion()
    mst = []
    while queue:
        w, x, y = queue.pop()
        if not set_union.same_component(x, y):
            #print('Inserted (%r, %r)' % (x, y))
            mst.append((w, x, y))
            set_union.union_sets(
                set_union.find(x), set_union.find(y))
    return mst


def find_feedback_edge_set(graph):
    mst = kruskal_max_spanning_tree(graph)
    mst_edges = set(
        tuple(sorted((x, y)))
        for w, x, y in mst)
    edges = set(
        tuple(sorted((x, y)))
        for w, x, y in graph.all_edges())
    return edges - mst_edges


# Figure 6.3
g1 = Graph('abcdefg')
g1.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g1.insert('b', [('e', 7), ('c', 9)])
g1.insert('c', [('d', 4), ('e', 4), ('f', 3)])
g1.insert('d', [('f', 7)])
g1.insert('e', [('f', 2), ('g', 5)])
g1.insert('f', [('g', 2)])
print(find_feedback_edge_set(g1))
# {('f', 'g'), ('c', 'e'), ('c', 'd'), ('c', 'f'), ('a', 'b'), ('e', 'f')}


#         a
#      5/ | \12
#      b 7|  d
#      9\ | /4
#        c

g2 = Graph('abcd')
g2.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g2.insert('b', [('c', 9)])
g2.insert('c', [('d', 4)])
print(find_feedback_edge_set(g2))
# {('a', 'b'), ('c', 'd')}


# Loop
#
#   3
#  â
#

g3 = Graph('a')
g3.insert('a', [('a', 3)])
print(find_feedback_edge_set(g3))
# {('a', 'a')}


# Disconnected graph
# Notice no changes were required to the algorithm
#
#         a            e
#      5/ | \12      1/ \2
#      b 7|  d       g - f
#      9\ | /4         3
#        c

g3 = Graph('abcdefg')
g3.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g3.insert('b', [('c', 9)])
g3.insert('c', [('d', 4)])
g3.insert('e', [('g', 1), ('f', 2)])
g3.insert('g', [('f', 3)])
print(find_feedback_edge_set(g3))
# {('e', 'g'), ('a', 'b'), ('c', 'd')}
