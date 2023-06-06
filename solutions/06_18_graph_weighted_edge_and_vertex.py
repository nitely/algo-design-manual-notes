# -*- coding: utf-8 -*-

# 1. Since all edges and vertices have the same
# weight, we can use BFS to find the shortest
# past from vertex A to vertex B. Keep track of
# parents to construct the path later. BFS is O(V + E)
#
# 2. Add the cost of the *target* vertex cost to each
# *outgoing* edge cost, and use Dijkstra to find the shortest
# path from U to V. ie: A(12)--B(15) becomes A-15->B; B-12->A
# Dijkstra is O(n²) or O(E + V*log(V)) (heap version)
#
# 3. Same as 2. I guess in 2 we can replace the edge weight,
# since it's always 0, while here we must *add* to it.
# i.e: A(12)-5-B(15) becomes A-20->B; B-17->A

# This solution is given in the book section 6.6
