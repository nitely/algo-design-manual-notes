# -*- coding: utf-8 -*-

# 1. Find maximum matching: this is the maximum
# set of edges with no vertex in common, so not all
# vertex may be included. When all vertex are included
# (i.e: some lucky graph), it's called a perfect matching, and hence
# it's a min-size edge cover.
# 2. Include an arbitrary edge for each uncovered vertex (greedy)
