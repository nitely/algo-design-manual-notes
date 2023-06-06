# -*- coding: utf-8 -*-

# Beware, Skiena does not use the same definition as in
# Wikipedia, where it must contain a *unique*
# directed path, be a DAG, and
# all edges must point away from root.
# That'd seem to have a simple solution:
# find a vertex with only
# outgoing-edges, then check with
# BFS if all edges are reached
# just once

# The question is whether we allow a random
# vertex in a loop to be the root, as any
# vertex in a loop could as well be the root.
# If we want to allow this, then we need
# to remove all loops, by replacing loops
# by single edges. Each time we find a
# visited vertex v, we remove v and add
# all edges from v to the current vertex
# and so on until just one vertex of the
# loop is left. Repeat this for unvisited vertex
# then check if there is a vertex with only
# outgoing edges, if there are many, then
# they can't be reached from one to another,
# so there's no arborescence. If there's one
# that's the root.

# This solution assumes the first definition
# which is the same as wikipedia's, and so the
# more likely to be correct


# runtime O(V + E)
# space O(V + E)


from collections import deque


# DFS on DAG
# untested
def has_arborescence(graph):
    # Find vertex with no incoming
    # edges (root)
    all_edges = set()
    for v in graph.vertices:
        for y in graph.edges[v]:
            all_edges.add(y)
    roots = set(graph.vertices) - all_edges
    if len(roots) != 1:
        return False
    root = roots.pop()
    # Check graph is a DAG
    # and it's connected
    # i.e: all vertices can be reached from root
    queue = deque()
    queue.appendleft(root)
    discovered = set()
    discovered.add(root)
    while queue:
        v = queue.pop()
        for y in graph.edges[v]:
            if y in discovered:  # loop or multiple paths to the same vertex
                return False
            discovered.add(y)
            queue.appendleft(y)
    return len(graph.vertices) == len(discovered)

