# -*- coding: utf-8 -*-

# Time O(n * m) -> O(n^2)
# Space O(n * m) -> O(n^2)
# quadratic since m is just n

# There is a better solution that takes
# O(n) space and does not requires the
# second sorted string. And there is
# a even better solution that takes O(N*logN) time
# and does DP with binary search

# AKA maximum_monotone_subsequence

# Longest scattered increasing sequence
# same as approx longest common sequence
# except second string is the first string
# sorted in increasing order.
# To get the minimum/decreasing sequence,
# sort second string in decreasing order

MATCH, INSERT, DELETE = range(3)

def match_out(s1, s2, i, j):
    if s1[i-1] == s2[j-1]:
        print('M', end='')
    else:
        print('S', end='')  # substituted

def insert_out(s2, j):
    print('I', end='')

def delete_out(s1, i):
    print('D', end='')

def reconstruct_path(s1, s2, m, i, j, result):
    if m[i][j].parent == -1:
        return
    if m[i][j].parent == MATCH:
        reconstruct_path(s1, s2, m, i-1, j-1, result)
        result.append(i)
        #match_out(s1, s2, i, j)
    if m[i][j].parent == INSERT:
        reconstruct_path(s1, s2, m, i, j-1, result)
        #insert_out(s2, j)
    if m[i][j].parent == DELETE:
        reconstruct_path(s1, s2, m, i-1, j, result)
        #delete_out(s1, i)

# row 0
def row_init(m, i):
    m[0][i].cost = i
    if i > 0:
        m[0][i].parent = INSERT
    else:
        m[0][i].parent = -1

def col_init(m, i):
    m[i][0].cost = i
    if i > 0:
        m[i][0].parent = DELETE
    else:
        m[i][0].parent = -1

class Cost:
    def __init__(self):
        self.cost = 0
        self.parent = 0
    def __repr__(self):
        return "{} {}".format(self.cost, self.parent)

def max_monotone_subsequence(s1):
    s2 = ''.join(sorted(s1))  # changed
    size = max(len(s1)+1, len(s2)+1)
    costs = [0] * 3
    m = [[Cost() for _ in range(size)] for _ in range(size)]
    for i in range(size):
        row_init(m, i)
        col_init(m, i)
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            # match = 0; substitute = 1
            costs[MATCH] = m[i-1][j-1].cost + 0 if s1[i-1] == s2[j-1] else float('inf')
            costs[INSERT] = m[i][j-1].cost + 1
            costs[DELETE] = m[i-1][j].cost + 1
            m[i][j].cost = costs[MATCH]
            m[i][j].parent = MATCH
            for k in range(len(costs)):
                if costs[k] < m[i][j].cost:
                    m[i][j].cost = costs[k]
                    m[i][j].parent = k
    i = len(s1)
    j = 0
    for k in range(1, len(s2)):
        if m[i][k].cost < m[i][j].cost:
            j = k
    result = []
    reconstruct_path(s1, s2, m, len(s1), len(s2), result)
    #print('')
    return result

# 1-indexed
assert max_monotone_subsequence('243517698') == [
    1, 3, 4, 7, 9]  # 23568
print('ok')
