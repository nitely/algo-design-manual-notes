# -*- coding: utf-8 -*-

# Note: In bipartite graphs -such as trees-, maximum matching,
# minimum vertex cover, and max independent set, they
# all reduce to the same problem (one solution can be
# used to solve any other of these problems)
# See https://en.wikipedia.org/wiki/K%C5%91nig%27s_theorem_(graph_theory)
# and https://en.wikipedia.org/wiki/Vertex_cover
#

# This solution is as described in the book:
# 1. divide the bipartite graph in two sets L and R
# 2. create source vertex connected to L
# 3. create sink vertex connected to R
# 4. Make all edges flow from source to sink
# 5. The maximum flow from source to sink defines
#    the largest matching

# runtime O(m * F)
# where m is the time to find a path using BFS
# and compute the residual graph, and F is the value of
# the maximum flow. On bipartite matching F <= n, where
# n is the number of edges.

# There is a linear time solution using dynamic programming (only for trees),
# no idea about a linear time solution using
# network flow / augmenting paths, which we are supposed to use here

# bipartite maximum matching == matching of maximum cardinality
# in bipartite graphs

from collections import defaultdict, deque


class Edge:
    def __init__(self, capacity=0, flow=0):
        self.capacity = capacity
        self.flow = flow


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = defaultdict(dict)

    def insert(self, v, y, capacity=0):
        self.edges[v][y] = Edge(capacity=capacity)


# Split tree/bipartite-graph into
# two sets, using two coloring
def two_coloring(graph: Graph):
    independent_set_red = set()
    independent_set_black = set()
    colors = [independent_set_red, independent_set_black]
    color = 0
    v = graph.vertices[0]
    queue = deque([(v, color)])
    colors[color].add(v)
    while queue:
        v, color = queue.pop()
        color_complement = (color+1) % len(colors)
        for c in graph.edges[v]:
            assert c not in colors[color], 'odd-length cycle found, not bipartite'
            assert c not in colors[color_complement], 'cycle found, not a tree'
            queue.appendleft((c, color_complement))
            colors[color_complement].add(c)
    return colors


# Make network flow graph by
# adding directed edges that flow
# from source to sink:
# source -> left set -> right set -> sink
# and the reversed edges
def network_flow_graph(graph: Graph, left_set, right_set):
    g = Graph(graph.vertices + 's' + 't')
    # source -> left set
    for v in left_set:
        g.insert('s', v, capacity=1)
        g.insert(v, 's', capacity=0)
    # left set -> right set
    for v in left_set:
        for y in graph.edges[v]:
            assert y in right_set, 'not bipartite'
            g.insert(v, y, capacity=1)
            g.insert(y, v, capacity=0)
    # left set -> right set (using right-set edges)
    for v in right_set:
        for y in graph.edges[v]:
            assert y in left_set, 'not bipartite'
            g.insert(y, v, capacity=1)
            g.insert(v, y, capacity=0)
    # right set -> sink
    for v in right_set:
        g.insert(v, 't', capacity=1)
        g.insert('t', v, capacity=0)
    return g


# find min augmenting path
def bfs(graph: Graph, source, sink):
    queue = deque()
    queue.appendleft(source)
    parent = {source: None}
    while queue:
        v = queue.pop()
        for y, edge in graph.edges[v].items():
            if y not in parent and edge.capacity > edge.flow:
                parent[y] = v
                queue.appendleft(y)
                if y == sink:
                    return parent
    return parent


def edmonds_karp(graph: Graph):
    left_set, right_set = two_coloring(graph)
    print('L', left_set, 'R', right_set)
    graph = network_flow_graph(graph, left_set, right_set)
    source = 's'
    sink = 't'
    edges = graph.edges
    flow = 0
    while True:
        parent = bfs(graph, source, sink)
        if sink not in parent:
            break
        delta_flow = float('inf')
        v, y = parent[sink], sink
        while v:
            delta_flow = min(delta_flow, edges[v][y].capacity - edges[v][y].flow)
            v, y = parent[v], v
        v, y = parent[sink], sink
        while v:
            edges[v][y].flow += delta_flow
            edges[y][v].flow -= delta_flow
            v, y = parent[v], v
        flow += delta_flow
    return flow, graph


def matching(graph: Graph):
    edges = set()
    for v in graph.edges:
        for y, edge in graph.edges[v].items():
            if y in ('s', 't') or v in ('s', 't'):
                continue
            if edge.flow > 0:
                edges.add((v, y, edge.flow))
    return edges


g1 = Graph('abcdefghi')
g1.insert('a', 'b')
g1.insert('a', 'e')
g1.insert('b', 'c')
g1.insert('b', 'd')
g1.insert('e', 'f')
g1.insert('e', 'g')
g1.insert('g', 'h')
g1.insert('g', 'i')

_flow, _graph = edmonds_karp(g1)
print(_flow)
print(matching(_graph))
# L {'c', 'd', 'f', 'a', 'g'} R {'i', 'e', 'b', 'h'}
# 3
# {('g', 'h', 1), ('f', 'e', 1), ('c', 'b', 1)}
#
# ^matching is un-deterministic (sets are unordered),
# it changes on each run, but it's always a max matching
