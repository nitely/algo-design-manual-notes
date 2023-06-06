# -*- coding: utf-8 -*-

# No. While all MSTs remain MSTs,
# ie: all trees total weight increase
# the same.
# The shortest path may no longer remain
# shortest:
# ie: A-5-C, A-1-B-1-C
# A to C is 5 in first path
# A to C is 2 in second path (short-path MST)
# Add k=10: A-15-C, A-11-B-11-C
# A to C is 15 in first path
# A to C is 22 in second path (MST, no longer short-path)

# The *triangular inequality* of a graph
# implies that the distance from
# U to V is no greater that the
# distance from U to Y plus the
# distance from Y to V
#
# Any graph that does not has
# triangular inequality suffers
# from the above problem.
