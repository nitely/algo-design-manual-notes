# -*- coding: utf-8 -*-

# No. The longest path problem is NP-hard.
# If we find a way to solve
# single-source longest path in polynomial
# time, then we could do the operation for
# every vertex and find the longest one.
# Dijkstra being polynomial can't solve this
#
# Also, the obvious way would be to multiply
# each weight by -1, but Dijkstra does not
# work with negative weight edges. Floyd can do it,
# but only for DAGs, since it does not support
# negative cycles (i.e: if the graph has a
# cycle and all edges are positive, then making
# the edges negative will certainly create a negative
# cycle).
# Also, the solution for 06_21 (+ multiplying
# weights by -1) can do it in linear time (for DAGs only).
#
# The general case is NP-hard.

# As an aside, there is usually a connection
# between what known polynomial algorithms support
# and NP-completeness (i.e: no negative cycles)
