# -*- coding: utf-8 -*-

# Time O(n)
# Space O(1)
# Fn = Fn-1 + Fn-2
# F0 = 0, F1 = 1

def fibonacci(n: int) -> int:
    if n == 0: return 0
    f0 = 0
    f1 = 1
    fn = 1
    for _ in range(n-1):
        # fn = 1; f0 = 1; f1 = 1
        # fn = 2; f0 = 1; f1 = 2
        # fn = 3; f0 = 2; f1 = 3
        # fn = 5; f0 = 3; f1 = 5
        fn = f0 + f1
        f0 = f1
        f1 = fn
    return fn

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13
assert fibonacci(8) == 21
assert fibonacci(9) == 34
print(fibonacci(100))
