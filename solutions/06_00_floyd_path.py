# -*- coding: utf-8 -*-

# FLoyd version that can reconstruct all
# shortest paths
# Te return matrix has the paths, to get
# a path from A to B, we must traverse
# the matrix to construct it.


# adjacent matrix
class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.weight = [
            [float('inf')] * nvertices
            for _ in range(nvertices)]
        self.path = [
            [None] * nvertices
            for _ in range(nvertices)]
        for v in range(nvertices):
            self.weight[v][v] = 0
            self.path[v][v] = v

    def insert(self, u, v, weight):
        self.weight[u][v] = weight
        self.path[u][v] = v

    def get_path(self, u, v):
        if self.path[u][v] is None:
            return []
        p = [u]
        while u != v:
            u = self.path[u][v]
            p.append(u)
        return p


# return shortest paths matrix
# for all pairs of vertices
def floyd(graph: Graph):
    for k in range(graph.nvertices):  # intermediate vertex counter
        for i in range(graph.nvertices):  # dimension x
            for j in range(graph.nvertices):  # dimension y
                w = graph.weight[i][k] + graph.weight[k][j]
                if graph.weight[i][j] > w:
                    graph.weight[i][j] = w
                    graph.path[i][j] = graph.path[i][k]


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
p1 = floyd(g1)
print('OUT', g1.weight)
print(g1.get_path(0, 0))
print(g1.get_path(0, 1))
print(g1.get_path(0, 2))
print(g1.get_path(0, 3))
# [0, 1, 2, 3]
print(g1.get_path(1, 2))
print(g1.get_path(1, 3))
