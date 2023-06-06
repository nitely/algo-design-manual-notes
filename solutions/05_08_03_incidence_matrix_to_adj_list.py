# -*- coding: utf-8 -*-

# convert incidence matrix to
# adjacency list

# runtime O(n*m)
# needs extra O(m) space,
# but it's already O(m) since it construct the graph
# and extra space could be avoided but making runtime
# O(n*(m**2))

class Graph:
    def __init__(self):
        self.edges = {}

    def insert(self, x, y, directed=False):
        self.edges[x] = self.edges.get(x, [])
        self.edges[x].append(y)
        if not directed:
            self.insert(y, x, directed=True)


def inc_matrix_to_adj_list(matrix, v_num, e_num):
    graph = Graph()
    edges = [[] for _ in range(e_num)]
    for row in range(v_num):
        for col in range(e_num):
            if matrix[row * e_num + col] > 0:
                edges[col].append(row)
    for xy in edges:
        assert len(xy) == 2
        graph.insert(xy[0], xy[1])
    return graph


matrix = [
    1, 1, 0,
    1, 0, 0,
    0, 1, 1,
    0, 0, 1
]

print(inc_matrix_to_adj_list(matrix, 4, 3).edges)
# {0: [1, 2], 1: [0], 2: [0, 3], 3: [2]}
