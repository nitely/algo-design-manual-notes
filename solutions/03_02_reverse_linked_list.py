# -*- coding: utf-8 -*-

"""
3.2 reverse singly linked list. Make pointers point backwards.
    In linear time
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # def insert
    # def remove
    # def search

    # Notes: never do look-ahead, I tried it, it was shit
    #   look-behind is aways better
    def reverse(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    # Manual test, write up of the states on each iteration (start;end)
    # curr = a, prev = None, curr.next = b; curr.next = None, prev = a, curr = b
    # curr = b, prev = a, curr.next = c; curr.next = a, prev = b, curr = c
    # ...

    def print(self):
        print('printing')
        n = self.head
        while n is not None:
            print(n.value)
            n = n.next
        print('head %s' % self.head.value)


input = LinkedList()
d = Node('d')
c = Node('c', d)
b = Node('b', c)
a = Node('a', b)
input.head = a

input.print()
input.reverse()
input.print()
