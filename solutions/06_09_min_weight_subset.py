# -*- coding: utf-8 -*-

# 1. We must find the MST, but if there are extra
# edges with negative cost, we must add them all
# since they help to decrease the total weight
# 2. Use kruskal, then add all edges with negative
# weight to the MST.
