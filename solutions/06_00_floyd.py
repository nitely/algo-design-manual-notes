# -*- coding: utf-8 -*-

# Floyd finds all-pairs shortest path
# ie: the shortest path from any vertex
# to any vertex.
# However, the returned matrix here, can
# only be used to know the distance between
# any pair of vertices, not the path.
#
# Notice the diagonal of the matrix is 0
# since distance from a given vertex to the same
# vertex is 0. If it's less than 0, then there's
# at least one negative weight cycle in that vertex, if this
# happen then we can't get distance between vertices
# in the cycle. Floyd can detect there is at least one
# negative cycle, but it can't list them all.

# runtime O(n³)


# adjacent matrix
class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.weight = [
            [0 if x == y else float('inf')
             for y in range(nvertices)]
            for x in range(nvertices)]

    def insert(self, x, y, weight):
        self.weight[x][y] = weight


# return shortest distance matrix
# for all pairs of vertices
def floyd(graph: Graph):
    for k in range(graph.nvertices):  # intermediate vertex counter
        for i in range(graph.nvertices):  # dimension x
            for j in range(graph.nvertices):  # dimension y
                graph.weight[i][j] = min(
                    graph.weight[i][j],
                    graph.weight[i][k] + graph.weight[k][j])


#     0-10->3
#     |    ^
#     |    |
#     5    1
#     |    |
#     v    |
#     1-3->2

g1 = Graph(4)
g1.insert(0, 1, 5)
g1.insert(0, 3, 10)
g1.insert(1, 2, 3)
g1.insert(2, 3, 1)
print('IN', g1.weight)
floyd(g1)
print('OUT', g1.weight)
