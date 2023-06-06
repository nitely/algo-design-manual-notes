# -*- coding: utf-8 -*-

# A. Yes. Adding weight to all edges
# increments every sub-tree
# total weight equally. So, MSTs remain MSTs

# B. No. Counter example:
# A --1--> B
# B --1--> C
# A --3--> C
# Min path from A to C is A->B->C (weight=2)
# Add k = 2 weight
# A --3--> B
# B --3--> C
# A --5--> C
# Min path from A to C is A->C (weight=5)
