# -*- coding: utf-8 -*-

from collections import defaultdict


# Graph of adjacency-list uses a
# linked-list to store the edges
# for each vertex

# I've my doubts Skiena's implementation
# is correct. The linked list should insert
# to tail instead of head, otherwise the
# list is in reverse order. In the book
# it says it does this because the order
# does not matter (?)


# Linked-list node
class EdgeNode:
    def __init__(self, *, y: int, weight=0, next=None):
        self.y = y
        self.weight = weight
        self.next = next  # EdgeNode


class Graph:
    def __init__(
        self, *,
        nvertices,
        directed=False
    ):
        self.edges = defaultdict(lambda: None)  # dict[EdgeNode]
        self.degree = defaultdict(lambda: 0)  # dict[int]
        self.nvertices = nvertices  # list[string|int]
        self.nedges = 0
        self.directed = directed

    @classmethod
    def create(
        cls, *,
        nvertices,  # list[string|int]
        edges,  # list[tuple[string|int, string|int]]
        directed=False
    ):
        graph = cls(
            nvertices=nvertices,
            directed=directed)
        for x, y in edges:
            graph.insert(x, y, directed)
        return graph


    def insert(self, x: int, y: int, directed=False):
        edge_node = EdgeNode(y=y, next=self.edges[x])

        self.edges[x] = edge_node  # head
        self.degree[x] += 1

        # Create back-edge if undirected
        if not directed:
            self.insert(x=y, y=x, directed=True)
        else:
            self.nedges += 1


from collections import deque


# Beware this is a general implementation,
# processed and parent may not be needed for
# every problem
class BFS:
    def __init__(self):
        self.discovered = set()
        self.processed = set()
        self.parent = {}

    def traverse(self, graph, start):
        queue = deque()
        queue.appendleft(start)
        self.discovered = {start}
        self.processed = set()
        self.parent = {}
        while queue:
            v = queue.pop()
            self.process_vertex_early(v)
            self.processed.add(v)
            edge = graph.edges[v]
            while edge:
                y = edge.y
                if y not in self.processed or graph.directed:
                    self.process_edge(v, y)
                if y not in self.discovered:
                    queue.appendleft(y)
                    self.discovered.add(y)
                    self.parent[y] = v
                edge = edge.next
            self.process_vertex_late(v)

    def process_edge(self, x, y):
        pass

    def process_vertex_early(self, v):
        print(v)

    def process_vertex_late(self, v):
        pass


class DFS:
    def __init__(self):
        self.discovered = set()
        self.processed = set()
        self.parent = {}

    def traverse(self, graph, start):
        self.discovered = {start}
        self.processed = set()
        self.parent = {}
        self._traverse(graph, start)

    def _traverse(self, graph, v):
        self.process_vertex_early(v)
        edge = graph.edges[v]
        while edge:
            y = edge.y
            if y not in self.discovered:
                self.discovered.add(y)
                self.parent[y] = v
                self.process_edge(v, y)
                self._traverse(graph, y)
            elif y not in self.processed or graph.directed:
                self.process_edge(v, y)
            edge = edge.next
        self.process_vertex_late(v)
        self.processed.add(v)

    def process_edge(self, x, y):
        pass

    def process_vertex_early(self, v):
        print(v)

    def process_vertex_late(self, v):
        pass


# Alphabetical order
# to construct the graph seems to work
# but needs reversing since linked list of edges
# inserts at head instead of tail
g1 = Graph.create(
    nvertices=list('abcdefghij'),
    edges=list(reversed([
        ('a', 'b'),
        ('a', 'd'),
        ('a', 'i'),
        ('b', 'c'),
        ('b', 'e'),
        ('b', 'd'),
        ('c', 'e'),
        ('c', 'f'),
        ('d', 'e'),
        ('d', 'g'),
        ('e', 'f'),
        ('e', 'g'),
        ('e', 'h'),
        ('f', 'h'),
        ('g', 'h'),
        ('g', 'i'),
        ('g', 'j'),
        ('h', 'j'),
        ('i', 'j'),
    ])),
    directed=False
)

print('BFS graph1')
# A, B, D, I, C, E, G, J, F, H
BFS().traverse(g1, start='a')

print('DFS graph1')
# A, B, C, E, D, G, H, F, J, I
DFS().traverse(g1, start='a')

g2 = Graph.create(
    nvertices=list('abcdefghijklmnop'),
    edges=list(reversed([
        ('a', 'b'),
        ('a', 'e'),
        ('b', 'c'),
        ('b', 'f'),
        ('c', 'd'),
        ('c', 'g'),
        ('d', 'h'),
        ('e', 'f'),
        ('e', 'i'),
        ('f', 'g'),
        ('f', 'j'),
        ('g', 'h'),
        ('g', 'k'),
        ('h', 'l'),
        ('i', 'j'),
        ('i', 'm'),
        ('j', 'k'),
        ('j', 'n'),
        ('k', 'l'),
        ('k', 'o'),
        ('l', 'p'),
        ('m', 'n'),
        ('n', 'o'),
        ('o', 'p')
    ])),
    directed=False
)

print('BFS graph2')
# A, B, E, C, F, I, D, G, J, M, H, K, N, L, O, P
BFS().traverse(g2, start='a')

print('DFS graph2')
# A, B, C, D, H, G, F, E, I, J, K, L, P, O, N, M
DFS().traverse(g2, start='a')
