# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# runtime O(n!) factorial

# backtrack-DFS
def backtrack_permutations(input):
    solution = [0] * input
    def _backtrack(k):
        if k == input:
            print([s+1 for s in solution])
        else:
            in_perm = set(solution[:k])
            for i in range(input):
                if i == k:
                    continue
                if i not in in_perm:
                    solution[k] = i
                    _backtrack(k + 1)
    _backtrack(0)


# set {1, 2, 3}
backtrack_permutations(3)
# [2, 3, 1]
# [3, 1, 2]
