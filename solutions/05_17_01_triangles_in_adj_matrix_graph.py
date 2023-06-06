# -*- coding: utf-8 -*-

# Can be solved by square of matrix in O(V³) time
# i.e: edges of two-path size
# and for each neighbor, check
# if it has another neighbor
# that connects to the first vertex

# This solution does a square matrix
# without actually storing it

# Also, this not necessarily have to
# be solved with a matrix. I think I could
# have used an adjacent list and brute-force

# runtime O(V³)  (runtime required by the problem)
# space O(V)


# O(3*log3)
def canonical_triangle(p1, p2, p3):
    triangle = []
    for p in (p1, p2, p3):
        triangle.append(tuple(sorted(p)))
    return tuple(sorted(triangle))


def find_triangles(matrix, dim):
    triangles = set()
    for row in range(dim):
        for col in range(dim):
            if row == col:  # avoid loop in first vertex (edge case)
                continue
            if matrix[row * dim + col] > 0:  # first edge
                # row2 = col
                for col2 in range(dim):
                    if col == col2 or col2 == row:  # avoid loop in second and
                        # third vertex (edge case)
                        continue
                    is_triangle = (
                        matrix[col * dim + col2] > 0  # second edge
                        and matrix[col2 * dim + row] > 0  # third edge
                    )
                    if is_triangle:
                        triangles.add(canonical_triangle(
                            (row, col), (col, col2), (col2, row))) # O(3*log3)
    return triangles


#       A
#     / | \
#    /  |  \
#   B   C   D
#   |   |   |
#   |   |   |
#   E---F---G
#   |       |
#   ---------
#    (E, G) is also an edge
m1 = [
    1,1,1,1,0,0,0,
    1,0,0,0,1,0,0,
    1,0,0,0,0,1,0,
    1,0,0,0,0,0,1,
    0,1,0,0,0,1,1,
    0,0,1,0,1,0,1,
    0,0,0,1,1,1,0,
]

print(find_triangles(m1, 7))
# {((4, 5), (4, 6), (5, 6))}

# shared edge, edge case
#  a -- b -- c
#  \    |    /
#   \   |   /
#    \  |  /
#       d

m2 = [
    0,1,0,1,
    1,0,1,1,
    0,1,0,1,
    1,1,1,0,
]

print(find_triangles(m2, 4))
# {
#  ((0, 1), (0, 3), (1, 3)),
#  ((1, 2), (1, 3), (2, 3))
# }
