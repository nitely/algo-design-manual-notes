# -*- coding: utf-8 -*-

# Notice it's almost identical to prim.
# In Prim (MSP) we add the next vertex of
# min weight. In SP we add the closest
# to s, the new edge weight plus the distance
# from s to the tree vertex it connects to

# There is a Dijkstra version with runtime
# O(E+V*log(V)) but requires heap.decrease_priority()

from collections import defaultdict
import heapq


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(set)

    def insert(self, v, edges, directed=False):
        for y, weight in edges:
            self.edges[v].add((y, weight))
            if not directed:
                self.insert(y, [(v, weight)], directed=True)


# from book
def dijkstra(graph, start):
    # is in SPT
    in_tree = defaultdict(lambda: False)
    # cost of adding to tree
    distance = defaultdict(lambda: float('inf'))
    # to construct the SPT
    parent = defaultdict(lambda: None)

    distance[start] = 0
    v = start
    while not in_tree[v]:
        print('Inserted vertex=%r' % v)
        in_tree[v] = True
        for y, weight in graph.edges[v]:
            if distance[y] > distance[v]+weight and not in_tree[y]:
                distance[y] = distance[v]+weight
                parent[y] = v
        # select edge of min weight
        v = start
        dist = float('inf')
        for y in graph.vertices:
            if not in_tree[y] and dist > distance[y]:
                dist = distance[y]
                v = y

    return dict(distance), dict(parent)


# runtime (V²)
def dijkstra2(graph, start):
    parent = {}
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    queue = set(graph.vertices)
    while queue:
        _, v = min((dist[v], v) for v in queue)
        queue.remove(v)
        for y, weight in graph.edges[v]:
            if y not in queue:
                continue
            alt = dist[v] + weight
            if alt < dist[y]:
                dist[y] = alt
                parent[y] = (weight, v)
    return parent


# faster dijkstra. Broken since decrease_priority
# does not exist in heapq
def dijkstra3(graph, start):
    def decrease_priority_or_insert(q, weight, v):
        pass
    parent = {}
    dist = defaultdict(lambda: float('inf'))
    dist[start] = 0
    queue = [(0, start)]
    while queue:
        _, v = heapq.heappop(queue)
        for y, weight in graph.edges[v]:
            alt = dist[v] + weight
            if alt < dist[y]:
                dist[y] = alt
                parent[y] = (weight, v)
                decrease_priority_or_insert(queue, alt, y)
    return dict(parent)


# Figure 6.3
g1 = Graph('abcdefg')
g1.insert('a', [('b', 5), ('c', 7), ('d', 12)])
g1.insert('b', [('e', 7), ('c', 9)])
g1.insert('c', [('d', 4), ('e', 4), ('f', 3)])
g1.insert('d', [('f', 7)])
g1.insert('e', [('f', 2), ('g', 5)])
g1.insert('f', [('g', 2)])
print(dijkstra(g1, start='a'))
# Inserted vertex='a'
# Inserted vertex='b'
# Inserted vertex='c'
# Inserted vertex='f'
# Inserted vertex='d'
# Inserted vertex='e'
# Inserted vertex='g'
# {'b': 'a', 'c': 'a', 'd': 'c', 'e': 'c', 'f': 'c', 'g': 'f'}

print(dijkstra2(g1, start='a'))
# {'d': 'c', 'b': 'a', 'c': 'a', 'e': 'c', 'f': 'c', 'g': 'f'}
