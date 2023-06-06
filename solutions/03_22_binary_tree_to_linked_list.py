# -*- coding: utf-8 -*-


class NodeLL:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # def insert
    # def remove
    # def search

    def print(self):
        print('printing')
        n = self.head
        while n is not None:
            print(n.value)
            n = n.next
        print('head %s' % self.head.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # def add
    # def delete
    # def search

    def traverse(self):
        dummy = NodeLL(-1)
        curr = dummy
        def walk(node):
            nonlocal curr
            if node is None:
                return
            walk(node.left)
            print('tree node %r' % node.value)  # in-order
            # lined_list.insert(node.value)
            curr.next = NodeLL(node.value)
            curr = curr.next
            walk(node.right)
        walk(self.root)
        return LinkedList(dummy.next)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


one = Node(1)
three = Node(3, one)
nine = Node(9)
seven = Node(7)
eight = Node(8, seven, nine)
five = Node(5, three, eight)

tree = BinarySearchTree()
tree.root = five
linked_list = tree.traverse()
print('linked list')
linked_list.print()

# in-order
# 1
# 3
# 5
# 7
# 8
# 9
