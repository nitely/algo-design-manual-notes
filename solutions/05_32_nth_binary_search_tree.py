# -*- coding: utf-8 -*-

# Find ith node in sorted order

# Runtime O(V + E)


class Vertex:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    def __init__(self, root):
        self.root = root
        self.count = 0
        self.ith_value = None

    def _find_nth(self, v, ith):
        if v is None:
            return
        self._find_nth(v.left, ith)
        self.count += 1
        if self.count == ith:
            self.ith_value = v.value
        self._find_nth(v.right, ith)

    def find_nth(self, ith):
        self.count = 0
        self.ith_value = None
        self._find_nth(self.root, ith)
        return self.ith_value


#
#               15
#             /    \
#            8     20
#           /  \
#         7     11
#              /  \
#             9    12
#
# order: 8, 9, 10, 11, 12, 15, 20
#        1, 2, 3 ,  4,  5, 6 , 7

g1 = BinarySearchTree(
    Vertex(15,
           Vertex(8,
                  Vertex(7),
                  Vertex(11,
                         Vertex(9),
                         Vertex(12))),
           Vertex(20)))

print(g1.find_nth(1))
print(g1.find_nth(2))
print(g1.find_nth(3))
print(g1.find_nth(4))
print(g1.find_nth(5))
print(g1.find_nth(6))
print(g1.find_nth(7))
