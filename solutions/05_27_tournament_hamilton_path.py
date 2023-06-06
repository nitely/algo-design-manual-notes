# -*- coding: utf-8 -*-

"""
From http://www.algorist.com/algowiki/index.php/TADM2E_5.27

Proof by induction.

A tournament with 2 vertices (1,2) has a Hamiltonian path. 1 -> 2 or vice versa

Now suppose our tournament with n vertices has a Hamiltonian path 1,..,n.
Now add a vertex (n+1) that is connected to every other node. 3 cases may occur:

case1) If the first node of the n Hamiltonian path can be reached by
vertex (n+1), add (n+1) to the beginning of the path. New Hamiltonian
path: n+1,1,...,n

case2) If the last node of the n Hamiltonian path can reach the vertex
(n+1), add (n+1) to the end of the path. New Hamiltonian path: 1,...,n,n+1

case3) Take the first node of the n Hamiltonian path that can be reached
by (n+1). This must exist, because we are not in case 2. Call this node k.
By definition of this node, (k-1) can reach (n+1). Form the new Hamiltonian
path as: 1,...,k-1,n+1,k,...,n.
"""

# ^ seems correct. So, to find a hamilton path, we'd just find
# a path from a vertex that can reach every other vertex once?
# that can be done in quadratic time, doing a tree traversal
# for every vertex.
# Bonus: To find a hamilton cycle, the last vertex of a hamilton path
#        must be connected to the first.
