# -*- coding: utf-8 -*-

# Backtrack, exhaustive search
# runtime O(n!) factorial
# I suspect it's closer to quadratic in most cases


def find_n(d):
    n = 1
    while True:
        x = n * (n - 1) / 2
        if x >= d:
            assert x == d
            return n
        n += 1
    raise ValueError


def dist(x, input, solution):
    try:
        i = input.index(x)
        while i in solution:
            i = input.index(x, i+1)
        return i
    except ValueError:
        return -1


# backtrack-DFS
def backtrack_turnpike(input):
    solution = [0] * (find_n(len(input)) - 1)  # minus first position, it's always 0
    distances = set()
    def _backtrack(k):
        #print('it')
        nonlocal distances
        if k == len(solution):
            print([0] + [input[i] for i in solution])
        else:
            seen = set()
            for i, n in enumerate(input):
                # Prune any other order but increasing order
                if k > 0 and n < input[solution[k-1]]:
                    continue
                if i in distances:
                    continue
                # Prune duplicated input numbers
                if n in seen:
                    continue
                seen.add(n)
                # Prune not available distances to other points
                new_dists = set()
                for j in range(k):
                    d = input[i] - input[solution[j]]
                    assert d >= 0
                    new_dists.add(dist(d, input, distances | new_dists | {i}))
                if -1 in new_dists:
                    continue
                distances = distances | new_dists | {i}
                solution[k] = i
                _backtrack(k + 1)
                distances = distances - new_dists - {i}
    _backtrack(0)


# n = 4
backtrack_turnpike([1,2,3,4,5,6])
# [0, 1, 4, 6]
# [0, 2, 5, 6]

# n = 6
backtrack_turnpike([1,2,2,2,3,3,3,4,5,5,5,6,7,8,10])
# [0, 2, 4, 5, 7, 10]
# [0, 3, 5, 6, 8, 10]
