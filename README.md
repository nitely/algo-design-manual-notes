# The Algorithm Design Manual notes

Transcription from my old notebook.

### Algorithm runtime usefulness

They all take the same time for small n = 10

```text
- n!    -> n<20
- 2^n   -> n<=30
- n^2   -> n<=10_000
- nlogn -> n<=1_000_000
- n     -> n<=10_000_000
- logn  -> any
```

### Bit ops

- Bit array (bit-set, bit-vector, bit-map): use bits as true/false
- OR: set bit to 1
- AND: set bit to 0, if result is not 0 bit is set to 1
- XOR: invert bits (only set bits on right side)
- NOT: invert all bits (not 0000=1111)

n: size, len, nbits  
w: bits per item (int8, int16, etc)

```text
for i in range(n/w-1):
  complement[i]=not a[i]
  union[i]=a[i] or b[i]
  intersection[i]=a[i] and b[i]
  difference[i]=a[i] and (not b[i])
```

### Logarithms

#### Fast Exponentiation

Linear would just do `a*a*a...` however note `{n=n/2+n/2}`, so:

```text
aⁿ=(aⁿ⁄²)²    if n is even
aⁿ=a*(aⁿ⁄²)²  if n is odd
```

Recursion, divide and conquer by halving (n/2)

```text
func power(a,n):
  if (n==0) return 1
  x = power(a,a/2)
  if (n%2==0) return x^2
  else return a*(x^2)
```

#### Binary

logx:

- Repeated halving, i.e: binary search
- Repeated doubling, i.e: tree nodes search

### Tree traversal

in-order:

```text
traverse(node)
  traverse(node->left)
  process(node)
  traverse(node->right)
```

pre-order:

```text
process(node)
traverse(node->left)
traverse(node->right)
```

post-order:

```text
traverse(node->left)
traverse(node->right)
process(node)
```

### Binary search tree

Search, insert, delete, min (leftmost), max (rightmost)
are O(h) where h is the tree height.

Delete: move leftmost from right subtree of deleted node, take care of right child (put in place of rightmost).

### Graphs

Node=Vertex; Edge=Connection between two nodes (a,b)

- Undirected: (x,y) implies (y,x) 2-way flow
- Directed: one-way flow
- Weighted: value assign to (x,y); used for dijstra shortest path
- Unweighted: all values between nodes are the same; shortest path
  can be found with BFS, i.e: path with lesser number of edges
- Simple: (x,y)
- Non-simple: has cycles (x,y), (x,x); may also have multi-edges
- Sparse: linear edges O(n)
- Dense: O(n^2) edges; all-to-all
- Acyclic: no cycles (i.e: trees)
- - Directed Acyclic Graphs (DAGs) are used in scheduling problems.
    Topological sorting is the first step in any DAG problem, orders nodes/vertices to respect precedense constraints
- Cyclic: has cycles
- Embedded: edges and nodes have geometric position (i.e drawing)
- Topology: defined by position; i.e: a grid of `N*M`
- Implicit: constructed while they are traversed. May not be sorted
- Explicit: pre-constructed
- Labeled: each vertex has an ID, or name
- Unlabeled: not labeled
- Connected: there is a path between any two vertices

- Degree of a vertex is the number of adjacent edges to it (how many edges it has)

#### Data structure

Adjacency matrix: `N*M` matrix of `O(n^2)` size where each value tells if there is an edge between two vertices; i.e: `G[i,j]` is 1 (one) if there is an edge in `i->j` (i to j), first row has each edge for i to each existing vertex. Size is `O(N*M)` usually `n^2` in many problems.

Adjacency lists: graph based on linked-list. Right for most problems, but requires BFS/DFS to find relationships. Space takes `O(n+m)`. It's faster to traverse the whole thing (less space).

#### Breadth first search (BFS)

- Finding paths: shortest path in unweighted graph. From node to root by visiting node parents, until root.
- Connected components: can be found by processing each vertex in the list. When we find an undiscovered vertex we increment the counter of disconnected components. If the graph is connected doing BFS on it will process all vertex from the first list vertex.
- Two-coloring graph (bipartite): a bipartite graph is one that can be colored with only two colors, without connecting two vertices of the same color. It could be disconnected (sub-graphs). So we color a vertex when first discovered, apply BFS on it, and color each vertex while traversing when processing the edges, using the complement color. If the two vertex (parent-child) are of the same color, then it's not bipartite. Useful for some problems.

#### Depth first search (DFS)

- Uses a stack to store discovered (but not processed) vertices. Visiting a new neighbor as it's added to the stack, and backing up when there are no new neighbors.
- Can be used to answer "who is an ancestor" and "how many descendants".
- Can be used to split edges in an undirected graph into tree edges (x,y) and back-edges (y,x). While processing a vertex we only visit its descentdants (all of them), we don't visit that vertex brothers or cousings, we go deep (not broadth).
- DFS is the same idea as backtracking. Exausting search, backing up when there are no more possibilities.
- DFS organizes vertices by entry/exit times, and edges into tree edges and back-edges.
- Finding cycles: if there is a back-edge in an undirected graph, then there's a cycle. Any edge going to an ancestor creates a cycle.
- Articulation vertex: a single vertex whose deletion disconnects a connected component of the graph. Brute force testing to find it consist in temporarily deleting a vertex and do DFS or BFS to test if it's still a connected graph, but requires quadratic time. There's a clever linear time way with DFS.

#### Directed graphs

- Topological sorting: can be done using DFS on a DAG. Labeling the vertices in reverse order of processed finds the topological sort. Useful for tasks that have a scheduled order because of constraints. Also to get shortes and longest path between two vertices of a DAG. Back-edges are forbidden since they would create a cycle. IMplementation may add vertices to a stack after processing and pop them at the end to get the topological order.
- Strongly connected componenets: a DAG is strongly connected if there is a directed path between any two vertex. To test this in linear time, pick any vertex and check with DFS that all vertices are visited. Then create a second graph with the same edges but reversed and do DFS from the same picked vertex, if all vertices are visited then there is a path from vertex to any and from any to vertex.
- Graphs that are not strongly connected can be partitioned into strongly connected chuncks by deleting the weak connection (partition spot) with DFS. It's similar to finding biconnected components.

#### Weighted graphs

- Minimum spanning tree (MST): is a subset of a graph forming a tree whose sum of edges weight is as small as possible. Useful for connecting points of cities, homes, or other locations by smallest amount of roads, etc. A geometry minimum spanning tree use weights as distance between points/vertices. There can be more than one MST in a graph.
- Prim's Algorithm: prim's MST is a greedy algo. It starts from a vertex and selects the edge with lowest weight each time. Runtime is `O(n*m)` where n are iterations over m edges. There is a `O(n^2)` and a `O(n*nlogn)` implementation using a priority queue to find the min cost edge.
- Kruskal's algorithm: a greedy algo more efficient for sparse graphs. It builds connected components (subtrees) and connects them to form the MST. Runtime is `O(n*m)` `V*E`. There is a faster one `O(nlogn)` using union-find.
- Union-Find data structure: it represents connected components as set partitions. Where each vertex is in exactly one connected component/set. It limits the height of the tree by making the smallest subtree the child of the taller subtree root on every merge of two subtrees/sets. Only when merging two subtrees of equal size, the size gets incremented by one. So we need to double the size of the tree to get a new level. So the algo does `O(log)` finds and union worst case. Find is done by going from node x to its component root, and union just assings root of smallest tree to root od taller tree. There is a faster way by making fing faster.
- Variations of MST:
- - Maximum spanning tree: can simply be found by negating (i.e: to negative) the weight of all edges and running prism's on it. Shortes path algos don't work well with this, can't generate longest path.
- - Minimum product spanning tree: to minimize the product of edges, since `log(a*b)=log(a)+log(b)` we can log() each weight and find the MST.
- - Minimum bottleneck ST: minimizes the maximum weight over each subtree. Every MST has this property, the proof is in the correctness od kruskal's algo, since it does just that. Useful when we have costs, capacities, or strenghts instead of just weights.
- The MST is unique if all edges weights in the graphs are distinct, otherwise it depends on how prism/kruskal break ties.
- There are 2 variants that can't be solved by prism/kruskal:
- - Stainer tree: when we can add extra intermediate vertices aas shared juntion. Known as Minimum Stainer Tree.
- - Low-degree ST: the lowest max-degree tree. The MST with lowest high degree possible. It would be a simple path of max-degree 2.

#### Shortest path (SP)

- Dijkstra's algo: uses a dynamic programming strategy and it's similar to prism's algo. In each iteration we add the vertex with the smallest known cost. We keep track of the best path seen for all vertices and insert them in order of increasing cost. It can find more than the path from x to t, it finds the shortest path to all other vertices. This defines a shortest path spanning tree rooted at x. For an unweighted graph that would be the BFS tree. Runtime is `O(n^2)`, but there is an implementation `O(E+VlogV)` that uses a fibonacci heap min-prio as queue, useful for graphs with fewer edges than `V^2` (sparse graphs), for disconnected graphs it's `O(ElogV+VlogV)`. Dijkstra works only for graphs without negative weighted edges, because finding a negative cost may change the way to get from x to some other vertex. Floyd's algo supports this, as long as it's not a negative cost cycle.
- Shortest path with node cost: we can just take each edge and assing the cost to reach the target vertex, then just use dijktra's. For graphs with both edge and vertex cost, we can just add the cost of the target vertex to the cost of the edge.
- Floyd's algo: all-pairs SP, this is to find the vertex that minimizes the longest/average distance to all the other nodes. Useful to find the graph's diameter. Uses an adjacency matrix, so it takes `O(n^2)` space. It takes `O(n^3)` time, same as disjstra would take doing "n" iterations, calling itself for every node. Floyd can detect a negative cycle, can find all cycles of lenght > 1.
- Transitive closure: which vertices are reachable from a given node in a directed graph. It can be done with BFS/DFS, but also with Floyd's, the whole graph can be computed using all-pairs shortest-path, then if there is a distance from x to y then y can be reached from x. We can answer this for any node once we have the resulting distance matrix.

#### Network Flows and Bipartite Matching

In network flow porblems weights are capacity, and we need to find the maximum amount which can be sent from vertices/nodes S to T.

- Bipartite mathing: is finding a subset of edges such that no two edges share a vertex. The largest bipartite matching can be found using network flow. Divide a bipartite graph in sets L and R. Create a source node S connected to every vertex in L by an edge of weight 1. Create a sink node T connected to each vertex in R by an edge of weight 1. Assign each edge in the graph a weight 1. The maximum possible flow from S to T defines the largest matching.
- Computing network flows: network flow algos are based on augmenting paths. Find a path from S to T and adding it to the flow to increase the total flow capacity. A flow id optimal if it has no augmentation path. Through augmenting we eventually find the global maximum. The algo creates a struct called residual flow graph that contains the original graph with its edges called flow plus an extra edge per flow edge called capacity with the flow that can be passed, if it maximizes the flow. The resulting graph has a multi path from T to S with the max capacity, it may not be a single path but multiple paths of a given capacity that add up to the max flow capacity. A set of edges that separates S from T is called S-T cut. Flow algos can be used to solve general edge and vertex connectivity problems. The edmonds-karp algo is one implementation and it uses BFS to find the next augmenting path. Runtime is `O(n^3)` or `O(V*E^2)`

#### Graph problems

- Ordering the sequence: we want to order fragments E from left to right, some fragments must be at left or right of some other fragments. Solution: create a graph where each fragment is a vertex and edges are directed from one to other keeping the constraint left-right or right-left from one vertex/fragment to another. Then use topologicaal order to order the vertices. The graph must be a DAG. If there is a cycle, then ordering is not possible.
- Bucketing rectangles: we have rectangles on a plane that may have some overlap, we want to distribute them into the minimal set of buckets of non-overlapping rectangles. Solution: make each rectangle a vertex, add adges between overlapped rectangles/vertex, paint vertices minimazing the number of colors where two adjacent/connected vertices must not have the same color.
- Names in collision: we have severak hundreds file names and must short them to 8 charactes without collisions. Solution: make every filename a vertex, create a set of possible shortening names for every filename and make them vertices, add an edge between original filename vertex and shortname vertex. Find the set of edges that have no vertices in common. This is called bipartite matching.
- Separate the text: we need to separate lines of text, there is noise in the page that makes it hard. Solution: make each pixel a vertex and add edges between vertex neighbors. Add edge weight proportional to how dark the pixel is. We need to find a path from left to right that is as white as possible. Finding a shortest path will likely find this separation.
- Designing novel graph algos is very hard, so instead we can design graphs that can use classical algos to model the problem. I.e: finding shortest path, etc.

#### Graph cycles

A cycle is a closed path, cycles may share edges. A diamond graph has 3 cycles:

- A->B->C->A
- A->D->C->A
- A->B->C->D->A

```text
   A
  /|\
 B | D
  \|/
   C  
```

A cycle is a circuit in which the only repeated vertices are the first and last vertices.

### Combinatorial search and heuristic methods

#### Backtraking

Backtraking is a way to iterate through all possible configurations of a search space (exponential time).

- Permutations: all arragements of elements
- Subsets: all ways of building a collection of items. At each step we expand a partial solution, then we check if that partial solution is extensible or a dead end. This process does a Depth First traversal of partial solutions. It forms a backtracking tree (implicitly).

- Constructing all subsets: For N elements it means `2^N` possibilities. We make an array of N elements true or false, where the value of `N(i)` tells if `i` is in the subset.
- Constructing all permutations: There are `n!` possible distinct permutations, on each iteration we fix one element of the collection that is not in the permutation yet, we form an implicit tree of all possible permutations in order: 1,2,3;1,3,2;2,1,3;etc.
- Constructing all paths in a graph: Enumerates all paths from S to T. This is exponential. Starts from S, go to neighbors not in the partial solution until it finds the target, searching every path.

#### Search pruning

It's the technique of skipping a partial solution when it cannot be extended into a complete solution. Using symmetries is another way of reducing exponential searches. Combinatorial search combined with pruning can find optimal solutions of small optimization problems between `15 to 50` items (i.e: sudoku).

#### Heuristic search methods

It's an alternative for combinatorial optimizations poblems. There are a few methods: random sampling, gradient descent search, and simulated anneling. They have 2 things in common that they need: 1. solution space representation, this is a description of the set of possible solutions, and 2. cost function: a function to evaluate the quality of the solution (i.e: best shortest distance found so far).

- Random sampling: also known as the monte carlo method. We create random solutions ultil we get one food enough, or after some timeout. True random sampling requires selecting samples from a solutions space unifomly at random, each possible solution must have the same probability of being selected. When it is useful:
- - When there is a high proportion of acceptable solutions. When there are many we may find one quickly.
- - When there is no coherence in the solution space. When we cannot know if we are getting closet to a solution, there is no way of finding a solution but randomly.
- Local search: employs local neighborhood around every element in the solution space. We slightly modify the current solution. This includes swapping a random pair of elements or changing (inserting or deleting) a single one. This is not greedy, i.e: what seems best, but random instead. It does well:
- - When there is great coherence in the solution space, there is a pth to reach the optimal solution.
- - Whenever the cost of incremental evaluation is much cheaper than global evaluation, when we can find a solution and then make changes to it in constant time without re evaluatinf the whole thins to know the new result.  
The drawback is finding a local optimum instead of the optimum solution.
- Simulated annealing: allows occasional transitions to inferior solutions, avoiding, getting stucj on local optima. But it spends more time working on food elements than inferior ones. The problem must have a representation of the solutions space and a cost function and a cooling schedule, with a parameter of how likely we are to accept a bad transition over time. At the beggining we pick a higher probability to explore the space widely, as we progress we decrease the probability to limit transition to mostly local improvements. This is usually the best out of the three heuristic search methods.
- Applications of simulated annealing:
- - Maximum cut: partition graph in 2 sets to maximize weigh (or number) of edges with one vertex in each set. It is NP-Complete. The solution space has `2^(n-1)` possible partitions. The cost of a solution is the sum of weights. A transition selects one vertex at random and moves it to the other partition. The change in cost will be the weight of old neighbors minus nwe neighbors. In time proportional to vertex degree.
- - Independent set: is a subset of vertices S such that there is no edge with both endpoint on S. The space is `2^n` subsets of vertices. A simple transition add or delete one vertex from S. One cost function might be 0 (zero) if S contains an edge, and `|S|` (value of S) if it's a independent set. We work to an independent set at each step. A better cost function would allow non-empty graph at begining of cooling `C(S)=|S|-x*m(s)/T` where x is a constant, T is the temperature, and m(s) is the number of edges in the subgraph induced by S.
- - Circuit board placement: this may include: 1. minimizing area of the board so it fits some space. 2. minimizing the total or longest wire length in connecting the components. Multi criterion optimization problems. We are given a collection of rectangular modules r1, ..., rn each with an associated dimension `hi*li`. For each pair of modules ri,rj we are given the num of wires W(i,j) that must connect the two components. We seek a placement that minimizes area and wire lenght, without overlapping rectangles. The solutions must describe the positions of the rectangles. They can be restricted to be on vertices of an integer grid. A transition may move one rectangle to another position, or swapping two rectangles. A cost function may be `C(S)=area(S height * S width)+sum(i,j) for (wire * Wij*dij+overlap(ri union rj))` where `area`, `wire` and `overlap` are constants governing the cost of these components on the cost function. Overlap should be an inverse function of temperature, so after placement it adjusts the rectangle positions to be disjoint. Simulated annealing finds good solutions to problems but not optimal ones.

#### Other heuristic search methods

Popular methods include: genetic algos, neural networks, and and colony optimization. They don't lead to better solutions with less implementation complexity.

#### Parallel algos

For some problems they are the most effective solution. However, there are several pitfalls: 1. there is often a small upper bound on the potential win (ie number of threads), 2. speed up means nothing when a sequential algo can prune and avoid repeated work against brute force parallel solutions, 3. they are hard to debug unless the problem can be deompose into tasks, communication being non-deterministic make things harder to debug.

### Dynamic programming

Used to solve problems involving optimizzations, where we want to find a solution that maximizes or minimizes some function. Greedy algos based on best local step fail to find the best global solution, and exhaustive search algos are too slow. Dynamic programming combines the best of both, search all possibilities while storing results to avoid recomputing. It's a technique for efficiently implementing a recursive algo by storing partial results. The trick is realizing whether the naive recursive solution computes the same problems over and over again, and cache partial results. Works for problems on combinatorial elemetns that have a left-to-right order: character strings, trees, polygons, and integer sequences.

#### Fibonacci

Recursive fibonacci rakes exponential time. Caching the results of the recursive calls make it run in linear time for a lineal amount of space, and provides most of the benefits of dynamic programming (DP) recurrence relation: `Fn=F(n-1)+F(n-2); F0=0,F1=1`. The DP with explicit order of evaluation of the recurrence relation, takes linear time and constant space. We only need to store the last two values we have seen.

Recursion can be eliminated by specifying the order of evaluation in many cases.

#### Binomial Coefficient

Recurrence relation:
```text
(n) = (n-1) + (n-1)
(k)   (k-1)   ( k )
```

Base case:
```text
(n-k)
( 0 )
```

There is only one way to select 0 things from a set, the empty set. With this recurrence we can build the Pascal triangle. The solution takes `O(n^2)` time and takes `O(n^2)` space. It builds the Pascal matrix/triangle.

#### Approximate string matching

Search a substring closest to a given pattern. We must first define a cost function telling how far apart two strings are. One distance measure gives the number of changes to convert one string into another. Substitution, Insertion, Deletion. Each with a cost of 1 defines the disance between strings.

- Edit distance by recursion: the last char of a string must be either matched, substituted, inserted, or deleted. After this operation, we have 3 shorter strings (match/substitution, insertion, or deletion). If we knew the cost of each of these operations, we could chose the best solution. This leads to a recursive algo that runs in exponential time if we don't cache the solution to every sub-problem. There can only be `P*T` possible unique recursive calls, where P is the pattern and T is the other string. There is only that many distinct pairs of chars. We can store these pairs in a table and chache them.
- Edit distance by dynamic programming: it gets the intermediate values using a matrix `|P|*|T|`. It updated the parent field to construct the edit sequence later.
- Varieties of edit distance:
- - Penalty cost: application specific cost function can be more forgiving of replacements located near each other on the keyboard or that sound or look similar.
- - Goal location: the endpoint in the solution may not have a fixed location, unlike the edit distance case.
- - Approximate substring matching: search where a pattern best occurs within a text. Including misspellings.
- - Longest common sequence: find longest scattered string of chars included within both strings. I.e: between democrat and republican is eca. A common subsequence is defined by identical chars in an edit trace. We must prevent substitutions. The min cost has the fewest insert-del.
- - Maximum monotone sub-sequence: a scattered sequence of increasing numbers. I.e: 243517698->23568. Same as LCS, except the second string is the first string sorted in increasing order. To get the longest decreasing sequence, just sort in decreasing order. There is a `O(nlogn)` solution using DP with binary search.

#### The partition problem

Integer partition without rearragement balance range on each partition. the evalutation order computes the smaller values before the bigger values, so each evaluation has the preious pre-computed value. Runtime `O(K*N^2)`. Recurrence: `M[n,k]=min max(M[i,k-1], sum(S(i+1)))` where `M[n,k]` is the min cost over all partitions of `{S1,...,Sn}` into K ranges, where the cost of a partition is the largest sum of its elements. Boundaries: `M[1,k]=S1 K>0`, `M[n,1]=sum(S(i))` where the first argument is n=1, as the first partition consists of a single element. We cannot create a smaller partition. The smallest value of the second argument is K=1, no partitions. We need `k*n` cells to store the partial results, fillinf each cell takes `n^2` time per box. Total time `O(kn^3)`. We can store the set of n prefix sum needed to update te cells to get `O(kn^2)` total time. We use a second matrix `K*N` to reconstruct the optimal partitions.

#### Parsing context free grammars

Constructing a parse tree by parsing a string based on a context free grammar. We assume the grammar has constant size. The right side of every rule has 2 non terminals (x->yz) or one terminal symbol (x->inf). The rule at the root splits S at some position i such that the left part `S[1,i]` generates Y and the right part `S[i+1,n]` generates Z. With DP we keep track of all non terminals generated by each substring. `M[i,j,x]=V(M[i,k,y]*M[k+1,j,z])` (note this is wrong cause I cannot write the notation in markdown, look up the book). This is true if there exist a prodution x->yz and breaking point k between i and j such that the left part generates y and the right part z. Where V is the logical OR over all productions and split positions, and `*` us the logical AND of two boolean values. The one char terminal symbols define the boundary condition of the recurrence. `M[i,i,X]` is true if there exists a prduction x->inf such that `S[i]=inf`. There are `O(n²)` pairs of substrings (i,j). Evaluating `M[i,j,x]` requires testing all intermediate values k, so it takes `O(n)` tune to evaluate each `O(n²)` cells. Total runtime is `O(n³)`.

#### Minimum weight triangulation

... [end of notes]


# License

MIT
