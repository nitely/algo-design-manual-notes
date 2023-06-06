# -*- coding: utf-8 -*-

# Movies must be screened once, either Sat or Sun

# Set of movies {m1, m2, m3, ..., mk}
# Set of customer {c1, c2, c3, ..., ck}
# for each customer add an edge to the two movies
# use two-color technique to check if graph is bipartite,
# each color is a weekend day

# Runtime O(V + E)

from collections import defaultdict, deque


class Graph:
    def __init__(self):
        self.edges = defaultdict(lambda: set())

    def insert(self, m1, m2):
        self.edges[m1].add(m2)
        self.edges[m2].add(m1)


# Two-color, BFS
def movie_schedule(graph):
    sat_set = set()
    sun_set = set()
    days = [sat_set, sun_set]
    discovered = set()
    for v in graph.edges:
        if v in discovered:
            continue
        discovered.add(v)
        color = 0
        queue = deque([(v, color)])
        days[color].add(v)
        while queue:
            (v, color) = queue.pop()
            next_color = (color + 1) % len(days)
            for v2 in graph.edges[v]:
                if v2 in days[color]:
                    raise ValueError(
                        'Movies already schedule for '
                        'the same day (%r, %r)' % (v, v2))
                if v2 not in discovered:
                    discovered.add(v2)
                    queue.appendleft((v2, next_color))
                    days[next_color].add(v2)
    return days


g1 = Graph()
g1.insert('m1', 'm2')  # customer 1
g1.insert('m1', 'm3')  # customer 2
#g1.insert('m2', 'm3')
g1.insert('m2', 'm1')
g1.insert('mx', 'my')  # disconnected (possibly connected to some other nodes)

print(movie_schedule(g1))
# [{'mx', 'm1'}, {'m3', 'my', 'm2'}]
