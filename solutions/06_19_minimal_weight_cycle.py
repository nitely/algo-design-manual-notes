# -*- coding: utf-8 -*-

# runtime O(n³)
# Floyd


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


def find_min_cycle(graph: Graph):
    for i in range(graph.nvertices):
        graph.weight[i][i] = float('inf')
    for k in range(graph.nvertices):
        for i in range(graph.nvertices):
            for j in range(graph.nvertices):
                graph.weight[i][j] = min(
                    graph.weight[i][j],
                    graph.weight[i][k] + graph.weight[k][j])
    # assumes all edges have positive weight
    # diagonal contains the cycles
    return min(
        graph.weight[i][i]
        for i in range(graph.nvertices)
        if graph.weight[i][i] > 0)


#     /----10----\
#    /            v
#   0--1-->1--3-->2
#    ^     ^     /
#     \    |    2
#      8   0   /
#       \  |  v
#          3

g1 = Graph(4)
g1.insert(0, 2, 10)
g1.insert(0, 1, 1)
g1.insert(1, 2, 3)
g1.insert(2, 3, 2)
g1.insert(3, 0, 8)
g1.insert(3, 1, 0)
print(find_min_cycle(g1))
