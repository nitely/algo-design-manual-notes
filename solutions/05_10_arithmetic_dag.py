# -*- coding: utf-8 -*-


class Vertex:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        # cache sub-tree calculation.
        # kinda gross, we could keep a dict
        # of {vertex.id: result} instead and
        # pass it to the evaluation function
        self.result = None


ops = {
    '+': lambda x: x[0] + x[1],
    '/': lambda x: x[0] / x[1],
    '*': lambda x: x[0] * x[1],
}

# runtime O(n+m) avoids recalculating sub-trees

# Traversing in DFS order
def evaluate_arithmetic_dag(v):
    if v.result is not None:  # avoid sub-tree recalculation
        print('re-calculation saved for result = %r' % v.result)
        return v.result
    if v.left is None or v.right is None:
        return v.value
    left = evaluate_arithmetic_dag(v.left)
    right = evaluate_arithmetic_dag(v.right)
    v.result = ops[v.value]([left, right])  # cache result
    return v.result

v1 = Vertex('*', Vertex(3), Vertex(4))
t1 = (
    Vertex('+',
           Vertex('+',
                  Vertex(2),
                  v1),
           Vertex('/',
                  v1,
                  Vertex(5)))
)

print(evaluate_arithmetic_dag(t1))
