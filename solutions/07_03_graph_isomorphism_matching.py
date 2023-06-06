# -*- coding: utf-8 -*-

# Chapter 16.9 contains a description
# of the input, problem, and solution

# The book explains some enhancements
# like splitting vertices by degree, etc
# that allow for better pruning.
# But complexity remains the same.

# This solution backtracks through n!
# possible re-labeling of G1 with
# the name of vertices in G2, and then checks
# all edges are the same.
#
# We can prune partial solutions where the edges for current
# labels are not the same

# See 07_05 for sub-graph isomorphism matching
# which needs a few line changes

# Backtrack, exhaustive search
# runtime O(n!) factorial
# we go through all label permutations

from collections import defaultdict


class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.edges = defaultdict(set)

    def insert(self, v, y):
        self.edges[v].add(y)
        self.edges[y].add(v)

    # Return sub-graph if labels contains
    # less vertices, which is needed
    # for pruning (partial solution check)
    def relabel(self, labels):
        edges = set()
        for v in range(len(labels)):
            for y in self.edges[v]:
                if v < len(labels) and y < len(labels):
                    edges.add((labels[v], labels[y]))
        return edges

    # Return sub-graph if labels contains
    # less vertices, which is needed
    # for pruning (partial solution check)
    def edges_for(self, labels):
        in_labels = set(labels)
        edges = set()
        for v in labels:
            for y in self.edges[v]:
                if y in in_labels:
                    edges.add((v, y))
        return edges


# backtrack-DFS
def backtrack_isomorphism(input_a: Graph, input_b: Graph):
    if input_a.nvertices != input_b.nvertices:
        return False
    is_isomorphic = False  # early finish
    solution = [0] * input_b.nvertices  # labels map
    def _backtrack(k):
        nonlocal is_isomorphic
        if k == input_b.nvertices and input_a.relabel(solution) == input_b.edges_for(solution):
            is_isomorphic = True
        else:
            in_sol = set(solution[:k])
            for v in range(input_b.nvertices):
                if v in in_sol:
                    continue
                # prune
                if input_a.relabel(solution[:k]) != input_b.edges_for(solution[:k]):
                    continue
                solution[k] = v
                _backtrack(k + 1)
                if is_isomorphic:
                    return
    _backtrack(0)
    return is_isomorphic


# Same graphs
g1 = Graph(3)
g1.insert(0, 1)
g1.insert(1, 2)
g2 = Graph(3)
g2.insert(0, 1)
g2.insert(1, 2)
assert backtrack_isomorphism(g1, g2)

# Same graphs, different labels
g1 = Graph(3)
g1.insert(0, 1)
g1.insert(0, 2)
g2 = Graph(3)
g2.insert(1, 0)
g2.insert(1, 2)
assert backtrack_isomorphism(g1, g2)

# g1 has an extra edge
g1 = Graph(3)
g1.insert(0, 1)
g1.insert(1, 2)
g1.insert(0, 2)
g2 = Graph(3)
g2.insert(0, 1)
g2.insert(1, 2)
assert not backtrack_isomorphism(g1, g2)

# g2 has an extra edge
g1 = Graph(3)
g1.insert(0, 1)
g1.insert(1, 2)
g2 = Graph(3)
g2.insert(0, 1)
g2.insert(1, 2)
g2.insert(0, 2)
assert not backtrack_isomorphism(g1, g2)

g1 = Graph(2)
g1.insert(0, 1)
g2 = Graph(3)
g2.insert(0, 1)
g2.insert(1, 2)
assert not backtrack_isomorphism(g1, g2)

# g2 is a sub-graph of g1
g1 = Graph(3)
g1.insert(0, 1)
g1.insert(1, 2)
g2 = Graph(2)
g2.insert(0, 1)
assert not backtrack_isomorphism(g1, g2)

print('ok')
