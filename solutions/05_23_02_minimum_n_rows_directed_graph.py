# -*- coding: utf-8 -*-

# runtime O(n + m)
# space O(n)

from collections import deque


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = {}

    def insert(self, x, y):
        if x not in self.edges:
            self.edges[x] = []
        self.edges[x].append(y)


def find_minimum_num_rows(graph):
    discovered = {}
    min_levels = 0
    for v in graph.edges:
        if v in discovered:
            continue
        level = 1
        discovered[v] = level
        queue = deque()
        queue.appendleft((v, level))
        last_level = 0
        while queue:
            v, level = queue.pop()
            print(v, level)
            for y in graph.edges.get(v, []):
                if y in discovered:
                    if discovered[y] < level:
                        print(
                            'Loop found! v=%r is in row %r, '
                            'cannot be in row %r' %
                            (y, discovered[y], level+1))
                        return -1
                    continue
                discovered[y] = level+1
                queue.appendleft((y, level+1))
            last_level = level
        min_levels = max(min_levels, last_level)
    return min_levels


students = 'abcdef'
haters = [('a', 'b'), ('a', 'c'), ('b', 'c'), ('f', 'e')]
g1 = Graph(students)
for i, j in haters:
    g1.insert(i, j)

print('Test 1')
print(find_minimum_num_rows(g1))
# a 1
# b 2
# c 2
# f 1
# e 2
# 2

# loop
students = 'ab'
haters = [('a', 'b'), ('b', 'a')]
g2 = Graph(students)
for i, j in haters:
    g2.insert(i, j)
print('Test 2')
print(find_minimum_num_rows(g2))
