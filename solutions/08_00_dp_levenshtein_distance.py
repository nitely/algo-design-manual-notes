# -*- coding: utf-8 -*-

# Same as "approximate string matching"
# but without recording parent. It's easier
# to understand this way

def levenshtein_distance(s, t):
    m = len(s)
    n = len(t)
    # There can only possibly be S*T distinct pairs (s[i], t[j])
    # so we create a matrix of S*T size to store the intermediate values
    d = [[0] * (n+1) for _ in range(m+1)]
    # source prefixes can be transformed into empty string by
    # dropping all characters
    for i in range(1, m+1):
        d[i][0] = i
    # target prefixes can be reached from empty source prefix
    # by inserting every character
    # see the book table if this is not clear enough
    for j in range(1, n+1):
        d[0][j] = j
    for j in range(1, n+1):
        for i in range(1, m+1):
            subst_cost = int(s[i-1] != t[j-1])
            d[i][j] = min(
                d[i-1][j] + 1,  # deletion
                d[i][j-1] + 1,  # insertion
                d[i-1][j-1] + subst_cost)  # substitution or match
    return d[m][n]

assert levenshtein_distance('shot', 'spot') == 1
assert levenshtein_distance('ago', 'agog') == 1
assert levenshtein_distance('hour', 'our') == 1
assert levenshtein_distance('hours', 'our') == 2
assert levenshtein_distance('our', 'hours') == 2
assert levenshtein_distance('same', 'same') == 0
assert levenshtein_distance('thou-shalt-not', 'you-should-not') == 5
assert levenshtein_distance('', 'same') == 4
assert levenshtein_distance('same', '') == 4
print('ok')
