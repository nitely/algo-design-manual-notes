# -*- coding: utf-8 -*-


# Yes. Unless all edge weights are distinct, in which
# case there is only one MST.
# The reason they may yield different MSTs is because
# they break edge weight ties differently. In fact,
# kruskal does not define how to break those ties,
# in 06_00 I show how it returns the same MST
# as prism's, but can easily return other MST.
# Prism does not order the edges, just processed
# them in whatever order they are, and graphs
# don't have a specific edge order, so the MST
# is arbitrary. It also takes the starting node,
# depending on which it may create different MSTs.
