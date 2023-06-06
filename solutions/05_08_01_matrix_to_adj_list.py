# -*- coding: utf-8 -*-


# convert undirected graph from adjacency matrix
# to adjacency list

# runtime O(n^2) where n is the number of vertices


class Graph:
    def __init__(self):
        self.edges = {}

    def insert(self, x, y):
        self.edges[x] = self.edges.get(x, [])
        self.edges[x].append(y)


def matrix_to_adj_list(matrix, dim):
    graph = Graph()
    for row in range(dim):
        for col in range(dim):
            if matrix[row * dim + col] > 0:
                graph.insert(row+1, col+1)  # +1 for 1-index based
    return graph



# 1 for edge, 2 for loop
# undirected
matrix = [
    2,1,0,0,1,0,
    1,0,1,0,1,0,
    0,1,0,1,0,0,
    0,0,1,0,1,1,
    1,1,0,1,0,0,
    0,0,0,1,0,0,
]

print(matrix_to_adj_list(matrix, dim=6).edges)
