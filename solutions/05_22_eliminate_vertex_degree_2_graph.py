# -*- coding: utf-8 -*-

# Remove all edges of degree 2.
# The brute force
# solution would check and remove all vertices
# of degree 2, then repeat this again and again
# until there are no more vertex of degree 2,
# we may do this for all vertex
# taking quadratic time

# This solution works the same way, but
# in linear time. There are other ways
# to solve this that produce different
# outputs, look at the bottom for some
# fun edge-cases


# runtime O(V + E)
# space O(V)


from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.edges = defaultdict(set)

    def degree(self, v):
        return len(self.edges[v])

    def insert_edge(self, u, w):
        self.edges[u].add(w)
        self.edges[w].add(u)

    def remove(self, v):
        # up to 2 edges
        for u in self.edges[v]:
            self.edges[u].remove(v)
        del self.edges[v]

    def insert(self, v, edges):
        for y in edges:
            self.edges[v].add(y)
            self.edges[y].add(v)


# destroys the graph, but we could
# copy it (in O(V + E) time) to avoid that.
# BFS
def remove_degree_2_vertex(graph):
    queue = deque()
    discovered = set()
    for v in graph.edges:
        if graph.degree(v) == 2:
            queue.appendleft((v, 0))
            discovered.add(v)
    last_level = 0
    while queue:
        v, level = queue.pop()
        if graph.degree(v) < 2:  # unspecified edge-case
            if level == last_level:  # remove in passes/BFS levels
                graph.remove(v)
            continue
        u, w = graph.edges[v]
        graph.insert_edge(u, w)
        graph.remove(v)
        if graph.degree(u) == 2 and u not in discovered:
            queue.appendleft((u, level+1))
            discovered.add(u)
        if graph.degree(w) == 2 and w not in discovered:
            queue.appendleft((w, level+1))
            discovered.add(w)
        last_level = level


# only c is of degree 2
#           b
#         /
#       a -- c -- e
#        \
#          d

g1 = Graph()
g1.insert('a', ['b', 'c', 'd'])
g1.insert('c', ['a', 'e'])
g1.insert('b', ['a'])
g1.insert('d', ['a'])

remove_degree_2_vertex(g1)
print(g1.edges)
# {
# 'a': {'e', 'b', 'd'},
# 'b': {'a'},
# 'd': {'a'},
# 'e': {'a'}
# }


# edge case. In theory c and d must be removed.
# if we remove c, then b has now degree 2, should
# we remove it? d now has degree 1 instead of 2,
# should we leave it? if we remove d instead at first
# then c may now have degree 1, what now? This
# would be non-deterministic.
# Removing in passes (remove c and d) is an option,
# but removing b, c, and d sounds reasonable too,
# since at some point all had degree 2
#
#    a -- b -- d
#          \  /
#           c
#

g2 = Graph()
g2.insert('a', ['b'])
g2.insert('b', ['a', 'd', 'c'])
g2.insert('c', ['b', 'd'])
g2.insert('d', ['b', 'c'])

remove_degree_2_vertex(g2)
print(g2.edges)
# {
# 'a': {'b'},
# 'b': {'a'}
# }
