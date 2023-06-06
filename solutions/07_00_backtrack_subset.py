# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# Implementation from the book
# runtime O(2^n) exponential


# backtrack-DFS
def backtrack_subset(input):
    solution = [False] * input
    def _backtrack(k):
        #print(k, solution)
        # test first K elements of solution form a complete solution
        if k == input:
            # do something with a complete solution
            print([i+1 for i in range(k) if solution[i]])
        else:
            # possible candidates for the Kth position of solution
            # implicit tree of all possibilities
            solution[k] = True
            _backtrack(k + 1)
            solution[k] = False
            _backtrack(k + 1)
    _backtrack(0)


# subset {1, 2, 3}
backtrack_subset(3)
# [1, 2, 3]
# [1, 2]
# [1, 3]
# [1]
# [2, 3]
# [2]
# [3]
# []
