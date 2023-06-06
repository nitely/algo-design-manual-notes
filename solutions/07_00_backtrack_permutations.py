# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# Implementation from the book
# runtime O(n!) factorial (very slow, similar to exponential)


# backtrack-DFS
def backtrack_permutations(input):
    solution = [0] * input
    def _backtrack(k):
        #print(k, solution)
        # test first K elements of solution form a complete solution
        if k == input:
            # do something with a complete solution
            print([s+1 for s in solution])
        else:
            # possible candidates for the Kth position of solution
            # implicit tree of all possibilities
            in_perm = set(solution[:k])
            for i in range(input):
                if i not in in_perm:
                    solution[k] = i
                    _backtrack(k + 1)
    _backtrack(0)


# Avoids allocating a set O(n),
# but does not change the complexity
def backtrack_permutations_v2(input):
    solution = {}  # treat as ordered set
    def _backtrack(k):
        if k == input:
            print([s+1 for s in solution])
        else:
            for i in range(input):
                if i not in solution:
                    solution[i] = None
                    _backtrack(k + 1)
                    del solution[i]
    _backtrack(0)


# set {1, 2, 3}
backtrack_permutations(3)
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
