# -*- coding: utf-8 -*-

# Chapter 8.4
# Integer partition without rearrangement
# (rearrangement would make this NP-complete,
#  exponential time O(2^n) solution)

# Time O(K*N^2)
# Space O(K*N)

# The book version seems 1-indexed,
# this one is 0-indexed

#def print_books(s, start, end):
#    print(s[start:end])

def reconstruct_partitions(s, d, n, k, result):
    if k == 0:
        result.append(s[0:n+1])
    else:
        reconstruct_partitions(s, d, d[n][k], k-1, result)
        result.append(s[d[n][k]+1:n+1])

def partition(s, k):
    n = len(s)
    m = [[0] * k for _ in range(n)]  # values
    d = [[0] * k for _ in range(n)]  # dividers
    p = [0] * n  # prefix sums
    p[0] = s[0]
    for i in range(1, n):
        p[i] = p[i-1] + s[i]  # set next based on curr
    #print(p)
    for i in range(n):
        m[i][0] = p[i]
    for j in range(k):
        m[0][j] = s[0]
    #print(m)
    # recurrence
    for i in range(1, n):
        for j in range(1, k):
            m[i][j] = float('inf')
            for x in range(i):
                cost = max(m[x][j-1], p[i]-p[x])  # split cost
                if m[i][j] > cost:
                    m[i][j] = cost
                    d[i][j] = x
    #print(m)
    #print(d)
    result = []
    reconstruct_partitions(s, d, n-1, k-1, result)
    return result

assert partition([1,1,1,1,1,1,1,1,1], 3) == [
    [1,1,1], [1,1,1], [1,1,1]]
assert partition([1,2,3,4,5,6,7,8,9], 3) == [
    [1,2,3,4,5], [6,7], [8,9]]
print('ok')
