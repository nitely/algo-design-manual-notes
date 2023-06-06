# -*- coding: utf-8 -*-


class Tree:
    def __init__(self):
        self.edges = {}
        self.root = None
        self.pre_index = 0

    def _traverse(self, v):
        if v is None:
            return
        left, right = self.edges.get(v, (None, None))
        # pre-order
        #print(v)
        self._traverse(left)
        # in-order
        #print(v)
        self._traverse(right)
        # post-order

    def traverse(self):
        self._traverse(self.root)

    def create(self, tree):
        self.edges = {}
        self.root = tree[0][0]
        for v, children in tree:
            assert len(children) == 2
            self.edges[v] = tuple(children)
        return self

    # use in_order to get the root of the sub-tree
    # use pre_order to get the left side and right
    # side of the sub-tree, recurse until there
    # is no left or right side (or has no children),
    # return the root of each sub-tree to construct the
    # tree in DFS order
    def create_from(self, pre_order, in_order, start, end):
        if start > end:
            return None
        v = pre_order[self.pre_index]
        # this is kinda gross, but left
        # keeps incr, and right needs
        # to know how much to skip, right also
        # incr and left needs to know and so on
        self.pre_index += 1
        if start == end:  # leaf, not needed really
            return v
        index = in_order.index(v, start, end+1)
        self.edges[v] = (
            self.create_from(
                pre_order,
                in_order,
                start,
                index-1
            ),
            self.create_from(
                pre_order,
                in_order,
                index+1,
                end
            )
        )
        return v


#          a
#      /       \
#     b         c
#      \      /  \
#       d    f    e
#           /     / \
#          i     h   g
#
#
#
t1 = Tree().create([
    ('a', ['b', 'c']),
    ('b', [None, 'd']),
    ('c', ['f', 'e']),
    ('f', ['i', None]),
    ('e', ['h', 'g'])
])

t1.traverse()

pre_order = [
    'a',
    'b',
    'd',
    'c',
    'f',
    'i',
    'e',
    'h',
    'g',
]
in_order=[
    'b',
    'd',
    'a',
    'i',
    'f',
    'c',
    'h',
    'e',
    'g',
]
t2 = Tree()
t2.create_from(
    pre_order,
    in_order,
    start=0,
    end=len(pre_order)-1
)
print(t2.edges)
