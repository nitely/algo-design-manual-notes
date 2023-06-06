# -*- coding: utf-8 -*-

# Time O(n)
# Space O(n)
# Fn = Fn-1 + Fn-2
# F0 = 0, F1 = 1

def fibonacci(n: int) -> int:
    cache = {}
    def fib(n):
        if n == 0: return 0
        if n == 1: return 1
        if n in cache:
            return cache[n]
        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]
    return fib(n)

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
