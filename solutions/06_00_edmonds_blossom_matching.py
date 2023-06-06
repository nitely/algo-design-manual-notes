# -*- coding: utf-8 -*-

# Note this is not in the book (at least not in chapter 6)

# Useful for max matching in
# general graphs

# The blossom algorithm runs the
# hungarian algorithm (for bipartite graphs matching)
# until it finds a blossom (odd-length cycle), which
# it shrinks down into a single vertex, and repeats the
# same process again until no cycles or augmenting paths are found
