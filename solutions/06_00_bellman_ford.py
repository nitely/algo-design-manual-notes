# -*- coding: utf-8 -*-

# Similar to dijkstra except it supports
# negative weights (not negative cycles),
# but slower

# This algorithm is not mentioned in this chapter

# runtime O(V * E)

from collections import defaultdict


def bellman_ford(graph, source):
    parent = {}
    dist = defaultdict(lambda: float('inf'))
    dist[source] = 0
    # max path can have V - 1 edges
    for _ in range(len(graph.vertices) - 1):
        # all edges
        for v in graph.edges:
            for y, weight in graph.edges[v]:
                alt = dist[v] + weight
                if alt < dist[y]:
                    dist[y] = alt
                    parent[y] = (weight, v)
    # final scan of edges, if there is an update
    # there is a negative cycle (path of length V edges)
    for v in graph.edges:
        for y, weight in graph.edges[v]:
            if dist[v] + weight < dist[y]:
                assert False, "negative weighted cycle"
    return parent
