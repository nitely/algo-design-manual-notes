# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# runtime O(n!) factorial

# backtrack-DFS
def backtrack_permutations(input):
    solution = [0] * len(input)
    def _backtrack(k):
        if k == len(input):
            print([input[i] for i in solution])
        else:
            in_perm = set(solution[:k])
            seen = set()
            for i, n in enumerate(input):
                if i in in_perm:
                    continue
                # only fix unique numbers in current branch,
                # prune duplicates fixed in K position
                if n in seen:
                    continue
                seen.add(n)
                solution[k] = i
                _backtrack(k + 1)
    _backtrack(0)


backtrack_permutations([2, 2, 2])
# [2, 2, 2]

backtrack_permutations([1, 1, 2, 2])
# [1, 1, 2, 2]
# [1, 2, 1, 2]
# [1, 2, 2, 1]
# [2, 1, 1, 2]
# [2, 1, 2, 1]
# [2, 2, 1, 1]
