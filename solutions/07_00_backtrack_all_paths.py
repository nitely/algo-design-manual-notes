# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# Implementation from the book
# runtime O(2^n) exponential

from collections import defaultdict


class Graph:
    def __init__(self, nvertices):
        self.nvertices = nvertices
        self.edges = defaultdict(set)

    def insert(self, v, y):
        self.edges[v].add(y)
        self.edges[y].add(v)


# backtrack-DFS
def backtrack_all_paths(input: Graph, source, target):
    solution = [source] * input.nvertices
    def _backtrack(k):
        #print(k, solution)
        # test first K elements of solution form a complete solution
        if solution[k-1] == target:
            # do something with a complete solution
            print(solution[:k])
        else:
            # possible candidates for the Kth position of solution
            # implicit tree of all possibilities
            in_sol = set(solution[:k])
            for v in input.edges[solution[k-1]]:
                if v not in in_sol:
                    solution[k] = v
                    _backtrack(k + 1)
    _backtrack(1)  # start from source (solution[0])


# Fig 7.1
#             1
#           / | \
#         /  / \  \
#       /  /    \  \
#      2  3 ---- 4  5
#       \  \    /  /
#        \  \  / /
#          \ | /
#            6

g1 = Graph(6)
g1.insert(1, 2)
g1.insert(1, 3)
g1.insert(1, 4)
g1.insert(1, 5)
g1.insert(2, 6)
g1.insert(3, 4)
g1.insert(3, 6)
g1.insert(4, 6)
g1.insert(5, 6)

backtrack_all_paths(g1, source=1, target=3)
# [1, 2, 6, 3]
# [1, 2, 6, 4, 3]
# [1, 3]
# [1, 4, 3]
# [1, 4, 6, 3]
# [1, 5, 6, 3]
# [1, 5, 6, 4, 3]
