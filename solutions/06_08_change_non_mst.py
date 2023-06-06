# -*- coding: utf-8 -*-

# The only way to change some edge weight that
# could affect a MST is if changing the cost
# creates a unique MST, so the original MST
# is no longer a MST.
#
# We can use Prim to do this.
# Modify the step: "Select the edge
# of minimum weight between a tree and nontree vertex"
# Check how much cost we must subtract to select
# an edge not in the MST, store the edge as the
# one to be removed and replace it if a less costly
# edge is found.
# Prim runtime is quadratic.
#
# ^ XXX: proof :P
