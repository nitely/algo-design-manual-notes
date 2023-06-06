# -*- coding: utf-8 -*-

"""
A common problem for compilers and text editors is determining whether the
parentheses in a string are balanced and properly nested. For example, the string
((())())() contains properly nested pairs of parentheses, which the strings )()( and
()) do not. Give an algorithm that returns true if a string contains properly nested
and balanced parentheses, and false if otherwise. For full credit, identify the position
of the first offending parenthesis if the string is not properly nested and balanced.
"""

def is_parentheses_balance(text):
    # needs stack to track position
    # of first unbalanced paren
    stack = []
    for i, c in enumerate(text):
        if c == ')':
            if not stack:
                return (i, False)
            stack.pop()
        if c == '(':
            stack.append(i)
    if stack:
        return stack[0], False
    return True

assert is_parentheses_balance('()')
assert is_parentheses_balance('())') == (2, False)
assert is_parentheses_balance('(())')
assert is_parentheses_balance('(()') == (0, False)
assert is_parentheses_balance('((())())()')
