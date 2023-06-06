# -*- coding: utf-8 -*-

# A DFS finds the MST in an undirected graph.
# we can count the cycles and store the edge
# that completes the cycle for each one
#
# While this is supposed to work (at least I think so),
# a better/simpler way is to find the MST and obtain
# the difference of MST edges and the graph edges.
# Similar to 06_10_2

# Assumes the graph is connected for simplicity

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges):
        for y in edges:
            self.edges[v].add(y)
            self.edges[y].add(v)


# DFS - similar to finding cycles in a DAG (see topological order)
def find_feedback_edge_set(graph):
    feedback_edge_set = set()
    discovered = set()
    processed = set()
    def _traverse(graph, v, parent):
        discovered.add(v)
        for y in graph.edges[v]:
            if y not in discovered:  # tree-edge
                _traverse(graph, y, v)
            elif parent == y:  # back-edge
                continue
            elif y not in processed:  # cycle
                # if we find the vertex a second time
                # before it's done processing
                # then it must be a cycle
                feedback_edge_set.add((y, v))
        processed.add(v)
    v = graph.vertices[0]
    _traverse(graph, v, '')
    return feedback_edge_set

# This has 3 cycles. The third one
# is the cycle without the shared edge,
# so the min-size set is always 2
# 1. a->b->c->d->a
# 2. a->b->c->a
# 3. a->d->c->a
#
#         a
#       / | \
#      b  |  d
#       \ | /
#        c

g1 = Graph(vertices='abcd')
g1.insert('a', ['b', 'c', 'd'])
g1.insert('b', ['a', 'c'])
g1.insert('c', ['b', 'a', 'd'])
g1.insert('d', ['a', 'c'])
print(find_feedback_edge_set(g1))
assert len(find_feedback_edge_set(g1)) == 2


# Loop
#
#  â
#
g2 = Graph(vertices='a')
g2.insert('a', ['a'])
assert len(find_feedback_edge_set(g2)) == 1
