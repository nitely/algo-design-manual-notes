# -*- coding: utf-8 -*-

# 1. A-5-C; A-1-B-1-C; root A
# The shortest path tree and MST is A-1-B-1-C
#
# 2. A-15->C, A-11->B-11->C; root A
# The shortest path tree is A-11->B; A-15->C (total weight 26)
# The MST is A-11->B-11->C (total weight 22)
#
# 3. Yes, a graph rooted in A with:
# Shortest path A-2->C-2->B; A-6->D; total weight 10
# and
# MST A-5->B; B-2->C; B-2->D; total weight 9
# they are completely disjointed
