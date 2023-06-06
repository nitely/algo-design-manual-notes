# -*- coding: utf-8 -*-

# If all edges are negative, then yes,
# that's how a maximum spanning tree
# can be found.
#
# Otherwise, yes :P.
# They will certainly work with mixed
# negative/positive weights as they don't
# care are about sign. There is no
# arithmetic done on the weights, so it
# should not matter.
#
# In kruskal the weight just defines the processing
# order. In Prism the weight is used to compare
# distances between neighbors of a node, it does
# not change the selection order
#
