# -*- coding: utf-8 -*-

# This is not in the book

# it is easy to find a single strongly
# connected component [x]. Simply use
# BFS, DFS, or any other similar algorithm
# to find a set S of all vertices reachable
# from x by a path. Do the same thing in
# the graph formed by reversing all the
# edges of our original graph, to find
# a set T of all vertices that can reach x
# by a path. According to the definition above,
# [x] is just the intersection of S and T.


from collections import deque


def get_bfs_vertices(graph, v):
    queue = deque()
    queue.appendleft(v)
    discovered = set()
    discovered.add(v)
    while queue:
        v = queue.pop()
        for y in graph.edges[v]:
            if y in discovered:
                continue
            discovered.add(y)
            queue.appendleft(y)
    return discovered


def compute_single_component(graph, v):
    bfs_set_a = get_bfs_vertices(graph, v)  # vertices reachable from v
    graph.transpose()  # reverse all edges
    bfs_set_b = get_bfs_vertices(graph, v)  # vertices that can reach v
    return bfs_set_a & bfs_set_b  # intersection, vertices that can reach v and be reachable from v

