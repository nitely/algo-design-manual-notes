# -*- coding: utf-8 -*-

from collections import defaultdict


# class Edge ... if weight is needed
# class Vertex ... if metadata other than label is needed


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(lambda: [])

    @classmethod
    def create(cls, vertices, edges, directed=False):
        graph = cls(vertices)
        for x, ys in edges:
            for y in ys:
                graph.edges[x].append(y)
                #if not directed:
                #    graph.edges[y].append(x)
        return graph


class TopologicalSort():
    def __init__(self):
        self.discovered = set()
        # XXX make it an ordered set or make it a set, and add a toposort list
        self.processed = []

    def _sort(self, graph, v):
        self.discovered.add(v)
        for y in graph.edges[v]:
            if y not in self.discovered:
                self._sort(graph, y)
            elif y not in self.processed:
                # Discovered but not processed would
                # mean we found our current vertex again
                # before we are done with it, hence it's
                # a cycle
                assert False, 'back-edge found, not a DAG'
        self.processed.append(v)

    def sort(self, graph):
        self.discovered = set()
        self.processed = []
        for v in graph.vertices:
            if v not in self.discovered:
                self._sort(graph, v)
        return list(reversed(self.processed))


g1 = Graph.create(
    vertices=list('abcdefghij'),
    edges=[
        ('a', ['b', 'd']),
        ('b', ['c', 'd', 'e']),
        ('c', ['f']),
        ('d', ['e', 'g']),
        ('e', ['c', 'f', 'g']),
        # ('f', ['h']),  # book errata, this created a cycle.
        # Now "h" is a another connected component
        ('g', ['f', 'i']),
        ('h', ['f', 'g', 'j']),
        ('i', ['j']),
    ],
    directed=True)

# H, A, B, D, E, G, I, J, C, F
print(TopologicalSort().sort(g1))
