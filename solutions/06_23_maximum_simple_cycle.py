# -*- coding: utf-8 -*-

# This is asking to find the Longest Simple Cycle (LSC)
# on a directed weighted (complete?) graph. There is a
# reduction from Longest Simple Path (LSP) to LSC,
# so this would be NP-hard.
#
# Finding the *Shortest* Simple Cycle is called the *girth* (or width) of a graph [0] and
# can be found with floyd (and dijkstra?)
#
# We can find *a* cycle with positive returns (not necessarily simple, since
# nothing prevents the algorithm from selecting a vertex multiple times),
# by negating the logarithms of the weights and checking for negative cycles.
# To get the returns, do the inverse of log(x) (which is e^x) and negate again
# the distance of each negative cycle.
#
# See https://cs.stackexchange.com/questions/117649/maximum-value-of-arbitrage

# [0] https://en.wikipedia.org/wiki/Girth_(graph_theory)
