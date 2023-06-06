# -*- coding: utf-8 -*-

# Skiena defines the square of a graph
# as the square of the adjacency matrix
# (instead of the square of the graph itself),
# where for each two-edges path (a->b->c) an
# edge from origin to destiny is added (a->c)
# an that's it.

# The CLRS corrected that in a following edition
# to mean at most a two-edges paths, meaning also
# single-edges paths are added to the squared graph
# i.e: a -> b -> c
#       \
#        > c

# Cube of a graph would be at most 3-edge path

# This solution is for the Skiena problem.
# To solve CLRS's just add the edge to the original
# matrix, or add all edges to the square graph as well.
# Beware, the CLRS has the correct definition.

# runtime O(V³)
# space O(V²)

def square_adj_matrix(matrix, dim):
    matrix_2 = [0] * len(matrix)
    for row in range(dim):
        for col in range(dim):
            # first edge
            if matrix[row * dim + col] > 0:
                # there's an edge, check
                # all vertex2 edges, and
                # create an edge from vertex1 to
                # vertices that vertex2 connects to
                row2 = col
                for col2 in range(dim):
                    # second edge
                    if matrix[row2 * dim + col2] > 0:
                        matrix_2[row * dim + col2] = 1
    return matrix_2


m1 = [
    0, 1, 0, 1,
    0, 0, 1, 0,
    0, 0, 0, 1,
    0, 1, 0, 0,
]

print(square_adj_matrix(m1, 4))
# [
# 0, 1, 1, 0,
# 0, 0, 0, 1,
# 0, 1, 0, 0,
# 0, 0, 1, 0
# ]
