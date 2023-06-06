# -*- coding: utf-8 -*-

# See https://www.ics.uci.edu/%7Eeppstein/161/960220.html#sca
# for a good explanation about back-edges, cross-edges, and
# forward-edges. Also, Skiena book 5.10 Figure (one of them).

# Partition graph into strongly connected components.
# This is similar to the arborescence problem, but
# instead of finding a vertex with no incoming edges
# we find a strong component with no incoming edges,
# then all vertices within that component are mother
# vertex (the component may have one or more vertices)

from collections import defaultdict


class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.edges = defaultdict(set)

    def insert(self, x, edges):
        for y in edges:
            self.edges[x].add(y)


# Algorithm described by Skiena in
# the Strongly connected components section.
# There's a more straight-forward algorithm
# that does not requires keeping track of
# oldest vertex in each component and handling
# back and cross edges, but requires 2-passes
class MotherVertex:
    def __init__(self, graph):
        size = graph.nvertices
        self.graph = graph
        self.discovered = [False] * size
        self.processed = [False] * size
        self.parent = [-1] * size
        self.entry_time = [-1] * size
        self.time = 0
        self.active = []
        # oldest vertex surely in component of v
        self.low = [-1] * size
        # strong component number for each vertex
        self.scc = [-1] * size
        self.components_found = 0

    # Chapter 5.10
    # edge_classification(int x, int y)
    # (parent[y] == x) (TREE);
    # (discovered[y] && !processed[y]) (BACK);
    # (processed[y] && (entry_time[y]>entry_time[x])) (FORWARD);
    # (processed[y] && (entry_time[y]<entry_time[x])) (CROSS);
    TREE, BACK, FORWARD, CROSS = range(4)
    def edge_classification(self, x, y):
        # discovered but not processed
        if self.discovered[y] and not self.processed[y]:
            return self.BACK
        # processed before its parent
        if self.processed[y] and self.entry_time[y] < self.entry_time[x]:
            return self.CROSS
        return -1

    # recalculate the root of the component sub-tree
    def process_edge(self, x, y):
        cls = self.edge_classification(x, y)
        if cls == self.BACK:
            if self.entry_time[y] < self.entry_time[self.low[x]]:
                self.low[x] = y
        if cls == self.CROSS:
            if self.scc[y] == -1:  # component not yet assigned
                if self.entry_time[y] < self.entry_time[self.low[x]]:
                    self.low[x] = y

    def process_vertex_early(self, v):
        self.active.append(v)

    def process_vertex_late(self, v):
        # root of the sub-tree (i.e:
        # the sub-tree was processed and
        # it's in active stack)
        if self.low[v] == v:
            # edge (parent[v], v) cuts off scc
            self.pop_component(v)
        if self.entry_time[self.low[v]] < self.entry_time[self.low[self.parent[v]]]:
            self.low[self.parent[v]] = self.low[v]

    def pop_component(self, v):
        self.components_found += 1
        while True:
            t = self.active.pop()
            self.scc[t] = self.components_found
            if t == v:
                break

    def _has_mother_vertex(self, v):
        self.time += 1
        self.entry_time[v] = self.time
        self.process_vertex_early(v)
        for y in self.graph.edges[v]:
            self.process_edge(v, y)
            if self.discovered[y]:
                continue
            self.parent[y] = v
            self.discovered[v] = True
            self._has_mother_vertex(y)
        self.processed[v] = True
        self.process_vertex_late(v)

    # DFS
    def has_mother_vertex(self):
        for v in range(self.graph.nvertices):
            if self.discovered[v]:
                continue
            self.discovered[v] = True
            self._has_mother_vertex(v)
