# -*- coding: utf-8 -*-

# This is just a topological sort
# of a directed graph. It says
# it's not possible if there is
# a cycle, otherwise it returns
# the line order

# runtime O(n + m)
# space O(n)

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(list)

    def insert(self, x, y):
        self.edges[x].append(y)


# DFS
class TopologicalSort():
    def __init__(self):
        self.discovered = set()
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
                assert False, 'back-edge found, not a DAG. Not possible'
        self.processed.append(v)

    def sort(self, graph):
        self.discovered = set()
        self.processed = []
        for v in graph.vertices:
            if v not in self.discovered:
                self._sort(graph, v)
        return list(reversed(self.processed))


students = 'abcdef'
haters = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('f', 'e')]
g1 = Graph(students)
for i, j in haters:
    g1.insert(i, j)

print(TopologicalSort().sort(g1))
# ['f', 'e', 'd', 'a', 'b', 'c']
# first is f, then e, etc

