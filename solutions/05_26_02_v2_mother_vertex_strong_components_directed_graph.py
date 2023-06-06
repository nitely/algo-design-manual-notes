# -*- coding: utf-8 -*-

# Beware, while this may seem simpler,
# understanding the Skiena solution
# (the other file), helps solving other
# problems.

# This v2 does 2 passes to find the strongly
# connected components.
# * DFS keeping track of processed vertices
# * reverse every edge direction
# * DFS on the reversed graph using
#   the previous processed vertices order
#   to find each component
# * find a component without incoming edges,
#   and traverse the graph from any of those
#   vertices to check all vertices can be reached


def _dfs_ordered_vertices(graph, v, discovered, ordered_vertices):
    for y in graph.edges[v]:
        if y in discovered:
            continue
        discovered.add(y)
        _dfs_ordered_vertices(graph, v, discovered, ordered_vertices)
    ordered_vertices.append(v)


def dfs_ordered_vertices(graph, vertices):
    ordered_vertices = []
    discovered = set()
    for v in vertices:
        if v in discovered:
            continue
        discovered.add(v)
        _dfs_ordered_vertices(graph, v, discovered, ordered_vertices)
    return ordered_vertices


def strongly_connected_components(graph, ordered_vertices):
    components = []
    discovered = set()
    for v in reversed(ordered_vertices):
        if v in discovered:
            continue
        discovered.add(v)
        component = []
        _dfs_ordered_vertices(graph, v, discovered, component)
        components.append(component)
    return components


# O(V + E)
def mother_component(graph, components):
    component_by_v = [-1] * graph.nvertices
    for i, component in enumerate(components):
        for v in component:
            component_by_v[v] = i
    children = set()
    for component in components:
        component = set(component)  # XXX store sets in components in the first place
        for v in component:
            for y in graph.edges[v]:
                if y not in component:
                    assert component_by_v[y] != -1
                    children.add(component_by_v[y])
    mothers = set(range(len(components))) - children
    if mothers != 1:
        print('No mother vertex')
        return
    return components[mothers.pop()]


def has_mother_vertex(graph):
    ordered_vertices = dfs_ordered_vertices(graph, list(range(graph.nvertices)))
    assert graph.nvertices == len(ordered_vertices)
    graph2 = graph.traspose()
    components = strongly_connected_components(graph2, ordered_vertices)
    mother = mother_component(graph, components)
    if mother is None:
        return
    return graph.nvertices == len(dfs_ordered_vertices(graph, mother))

