# -*- coding: utf-8 -*-

# Note the algorithm in the book states
# it adds some padding to the input, and I
# don't do that here.
# btw the algorithm is called "Levenshtein distance"

# Time O(n * m)
# Space O(n * m)
# where n and m are the strings len


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

def reconstruct_path(s1, s2, m, i, j):
    if m[i][j].parent == -1:
        return
    if m[i][j].parent == MATCH:
        reconstruct_path(s1, s2, m, i-1, j-1)
        match_out(s1, s2, i, j)
        return
    if m[i][j].parent == INSERT:
        reconstruct_path(s1, s2, m, i, j-1)
        insert_out(s2, j)
        return
    if m[i][j].parent == DELETE:
        reconstruct_path(s1, s2, m, i-1, j)
        delete_out(s1, i)
        return

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

def string_compare(s1, s2, rec=False):
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
    if rec:
        #for x in m:
        #    print(x)
        reconstruct_path(s1, s2, m, len(s1), len(s2))
        print('')
    return m[len(s1)][len(s2)].cost

assert string_compare('shot', 'spot') == 1
assert string_compare('ago', 'agog') == 1
assert string_compare('hour', 'our') == 1
assert string_compare('hours', 'our') == 2
assert string_compare('our', 'hours') == 2
assert string_compare('same', 'same') == 0
assert string_compare('thou-shalt-not', 'you-should-not', rec=True) == 5
assert string_compare('', 'same') == 4
assert string_compare('same', '') == 4
print('ok')
