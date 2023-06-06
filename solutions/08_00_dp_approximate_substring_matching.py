# -*- coding: utf-8 -*-

# Time O(n * m)
# Space O(n * m)
# where n and m are the strings len

# similar to approximate matching,
# except it *does not* penalizes
# matches not starting at index 0


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
    m[0][i].cost = 0  # changed
    m[0][i].parent = -1  # changed

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

def find_approx_substring(s1, s2):
    size = max(len(s1)+1, len(s2)+1)
    costs = [0] * 3
    m = [[Cost() for _ in range(size)] for _ in range(size)]
    for i in range(size):
        row_init(m, i)
        col_init(m, i)
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            # match = 0; substitute = 1
            costs[MATCH] = m[i-1][j-1].cost + int(s1[i-1] != s2[j-1])
            costs[INSERT] = m[i][j-1].cost + 1
            costs[DELETE] = m[i-1][j].cost + 1
            m[i][j].cost = costs[MATCH]
            m[i][j].parent = MATCH
            for k in range(len(costs)):
                if costs[k] < m[i][j].cost:
                    m[i][j].cost = costs[k]
                    m[i][j].parent = k
    # changed
    i = len(s1)
    j = 0
    for k in range(1, len(s2)):
        if m[i][k].cost < m[i][j].cost:
            j = k
    result = []
    reconstruct_path(s1, s2, m, len(s1), len(s2), result)
    #print('')
    return result

assert find_approx_substring('..s..k..i..ena', 'skiena') == [
    3, 6, 9, 12, 13, 14]
assert find_approx_substring('..skienna', 'skiena') == [
    3, 4, 5, 6, 8, 9]
assert find_approx_substring('..skena', 'skiena') == [
    3, 4, 5, 6, 7]
assert find_approx_substring('..skina', 'skiena') == [
    3, 4, 5, 6, 7]
assert find_approx_substring('..skiena..', 'skiena') == [
    3, 4, 5, 6, 7, 8]
print('ok')
