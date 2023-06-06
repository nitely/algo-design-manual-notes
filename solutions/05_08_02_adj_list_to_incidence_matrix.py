# -*- coding: utf-8 -*-


# convert undirected graph to
# incidence matrix

# runtime O(n*m) where n are vertices and m are edges


class Graph:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def n_edges(self):
        # assumes undirected graph
        return sum(len(e) for e in self.edges.values()) // 2


def adj_list_to_inc_matrix(graph):
    n_edges = graph.n_edges()
    matrix = [0] * (len(graph.vertices) * graph.n_edges())
    edge_count = 0
    for v in graph.vertices:
        for edge in graph.edges.get(v, []):
            if v > edge:  # assumes undirected graph
                # we could go through half the vertices instead,
                # not sure about loops. For directed graphs
                # we always add a new edge per edge and set
                # 1 for out-edge and -1 for in-edge,
                # so we'd remove this check
                continue
            matrix[v * n_edges + edge_count] = 1
            matrix[edge * n_edges + edge_count] = 1  # back-edge
            edge_count += 1
    return matrix


# undirected
g = Graph(
    [0, 1, 2, 3],
    {
        0: [1, 2],
        1: [0],
        2: [0, 3],
        3: [2]
    }
)

# n*m incidence matrix: n vertices, m edges
# this has 4*3

#     e1  e2  e3
# 1   1   1   0
# 2   1   0   0
# 3   0   1   1
# 4   0   0   1

print(adj_list_to_inc_matrix(g))
# [
# 1, 1, 0,
# 1, 0, 0,
# 0, 1, 1,
# 0, 0, 1
# ]
