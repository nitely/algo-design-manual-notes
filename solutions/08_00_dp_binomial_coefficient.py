# -*- coding: utf-8 -*-

# Time: O(n^2)
# Space: O(n^2)
# Each number is the sum of the numbers directly above it
# Recurrence relation:
# (n) = (n-1) + (n-1)
#  k    k-1       k
# Base case:
# (n-k) = 1
#   0

def binomial_coefficient(n, m):
    assert n >= 0 and m >= 0
    if m > n:
        return 0
    bc = [[1] * (n+1) for _ in range(n+1)]  # table of binomial coefficients
    for i in range(1, n+1):
        for j in range(1, i):
            bc[i][j] = bc[i-1][j-1] + bc[i-1][j]  # sum above-left and above
    return bc[n][m]


# m/n 0  1  2  3  4  5
# 0   1
# 1   1  1
# 2   1  1  1
# 3   1  3  3  1
# 4   1  4  6  4  1
# 5   1  5  10 10 5  1
assert binomial_coefficient(5, 4) == 5
assert binomial_coefficient(5, 3) == 10

assert binomial_coefficient(1, 9999) == 0
assert binomial_coefficient(1, 1) == 1
assert binomial_coefficient(1, 0) == 1
assert binomial_coefficient(0, 0) == 1
#assert binomial_coefficient(0, -1) == 0
