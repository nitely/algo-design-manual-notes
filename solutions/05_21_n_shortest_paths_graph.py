# -*- coding: utf-8 -*-

# note: "Vertex disjoint" path means a path with no common internal vertex
# ie: vertex disjoint
# s -> a -> b -> c -> d
# s -> x -> y -> z -> d
# not vertex disjoint (a is common)
# s -> a -> b -> c -> d
# s -> x -> a -> z -> d

# We can assume the (sub-)graph from
# v to w is connected since there should
# be a path. If there is not, then we
# don't care if it's disconnected or
# just missing


# directed graph
# runtime O(V + E)

from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.edges = defaultdict(list)

    def insert(self, x, edges):
        self.edges[x] = self.edges[x]
        for y in edges:
            self.edges[x].append(y)


# As soon as we reach w, we check
# what other paths in the queue have reached
# w as well.
# A given vertex can be visited multiple
# times since it's allowed to appear in multiple paths
#
# XXX We must avoid loops and visiting an edge multiple times,
# which would make this O(V² + E²). This solution does a poor
# job at that, it only avoids self-loops and loops that lead to longer paths.
# We should add a counter to the queue items of repeated vertices per
# level, i.e: pop all items of a level and then go through all the
# edges and count repeated ones to avoid adding them to the queue.
# It seems hard to come up with a quadratic example that does not involve
# self-loops or loops with longer paths, though.
#
# BFS
def shortest_paths(graph, v, w):
    queue = deque()
    queue.appendleft((v, 0))
    discovered = {v: 0}  # to excluded unneeded loops
    while queue:
        v, level = queue.pop()
        if v == w:  # found, check for other vertex in the queue with w and same level
            count = 1
            while queue:
                v, level2 = queue.pop()
                if level2 > level:
                    break
                if v == w:
                    count += 1
            return count
        y_level = level+1
        for y in graph.edges[v]:
            # allow re-discover on the same level,
            # otherwise this is a loop with a longer path
            if y in discovered and discovered[y] != y_level:
                print('loop v=%r' % y)
                continue
            discovered[y] = y_level
            queue.appendleft((y, y_level))
    # no path
    return 0


# path from 0 to 2 = {(0,1,2), (0,3,2), (0,1,2)} = 3 paths (one repeats the vertices)
# notice there is a loop in 0 that would make a path (0,0,1,2), (0,0,0,1,2), ...
# which with a naive solution would make runtime quadratic, imaging a graph
# that's similar to a linked list and adds one unneeded edge at each step:
# 1, 2, 3, 4, 5, 6, ..., n-1; similar to insertion-sort
#
#                 /-------->6
#            /-->3---v
#         <>0-->1-->2----->4-->5
#            \--^   ^----/
#

g1 = Graph()
g1.insert(0, [0,1,1,3])
g1.insert(1, [2])
g1.insert(2, [4,5])
g1.insert(3, [2,6])
g1.insert(4, [2,5])
g1.insert(5, [])

print(shortest_paths(g1, 0, 2))
# 3
