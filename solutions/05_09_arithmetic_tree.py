# -*- coding: utf-8 -*-


class Vertex:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


ops = {
    '+': lambda x: x[0] + x[1],
    '/': lambda x: x[0] / x[1],
    '*': lambda x: x[0] * x[1],
}

# runtime O(n)
# Traversing in DFS order
def evaluate_arithmetic_tree(v):
    if v.left is None or v.right is None:
        return v.value
    left = evaluate_arithmetic_tree(v.left)
    right = evaluate_arithmetic_tree(v.right)
    return ops[v.value]([left, right])


t1 = (
    Vertex('+',
           Vertex('/',
                  Vertex('*',
                         Vertex(3),
                         Vertex(4)),
                  Vertex(5)),
           Vertex('+',
                  Vertex(2),
                  Vertex('*',
                         Vertex(3),
                         Vertex(4))))
)

print(evaluate_arithmetic_tree(t1))
