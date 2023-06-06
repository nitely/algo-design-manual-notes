# -*- coding: utf-8 -*-

# To find a vertex that does not disconnect
# the graph, we can create a DFS tree and
# remove any of its leaves, i.e:
# the first one. We can also
# kill two birds with one stone (5.29)
# and create the topological sorting
# removing one by one in reverse of the
# sorting will remove vertices without
# disconnecting the graph, i.e: always removes
# leaves

# runtime O(V + E)


from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges):
        for y in edges:
            self.edges[v].add(y)
            self.edges[y].add(v)


def _find_deletion_order(graph, v, discovered, topo_stack):
    for y in graph.edges[v]:
        if y in discovered:
            continue
        discovered.add(y)
        _find_deletion_order(graph, y, discovered, topo_stack)
    topo_stack.append(v)


# DFS tree in reversed topological order
# assumes connected graph
def find_deletion_order(graph):
    discovered = set()
    topo_stack = []
    for v in graph.vertices:
        if v in discovered:
            continue
        discovered.add(v)
        _find_deletion_order(graph, v, discovered, topo_stack)
    # we keep the topological sort in reverse,
    # so leaves come first
    #topo_stack.reverse()
    return topo_stack


def find_some_non_articulation_vertex(graph):
    topological_sort = find_deletion_order(graph)
    return topological_sort[0]


# only c is of degree 2
#           b
#         /
#       a -- c -- e
#        \
#          d

g1 = Graph('bcdae')
g1.insert('a', ['b', 'c', 'd'])
g1.insert('c', ['a', 'e'])
g1.insert('b', ['a'])
g1.insert('d', ['a'])

print(find_deletion_order(g1))


#    a -- b -- d
#          \  /
#           c
#
g2 = Graph('bdca')
g2.insert('a', ['b'])
g2.insert('b', ['a', 'd', 'c'])
g2.insert('c', ['b', 'd'])
g2.insert('d', ['b', 'c'])

print(find_deletion_order(g2))
