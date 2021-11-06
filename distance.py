import numpy as np
from graph import Graph


def order_graphs(g1: Graph, g2: Graph) -> (Graph, Graph):
    """Order graphs, return larger as first element of the tuple"""
    return (g1, g2) if g1.size < g2.size else (g2, g1)


def calculate_distance(g1: Graph, g2: Graph) -> int:
    """Calculates distance between two Graphs"""
    assert g1.size == g2.size, "Graphs must have same size"
    return np.sum(abs(g1.matrix - g2.matrix))


def extend_graph(g1: Graph, g2: Graph) -> Graph:
    """
    Given two graphs with the first one having less vertices
    returns the first graph extended by the missing number of vertices
    and filled with compliment edges of the second graph
    """
    assert g1.size <= g2.size
    graph = Graph(size=g2.size)
    graph.matrix = g2.matrix.copy()
    graph.matrix[0: g1.size, 0: g1.size] = g1.matrix
    graph.matrix[g1.size: g2.size, :] = 1 ^ g2.matrix[g1.size: g2.size, :]
    graph.matrix[:, g1.size: g2.size] = 1 ^ g2.matrix[:, g1.size: g2.size]
    return graph


def permutations(graph: Graph, step=0) -> [Graph]:
    """
    Return all possible vertex orderings of a graph
    """
    yield graph
    for i in range(step + 1, graph.size):
        # swap rows
        graph.matrix[[step, i], :] = graph.matrix[[i, step], :]
        # swap columns
        graph.matrix[:, [step, i]] = graph.matrix[:, [i, step]]
        yield from permutations(graph, step + 1)
        # swap back rows
        graph.matrix[[step, i], :] = graph.matrix[[i, step], :]
        # swap back columns
        graph.matrix[:, [step, i]] = graph.matrix[:, [i, step]]


def exact_distance(g1: Graph, g2: Graph):
    g1, g2 = order_graphs(g1, g2)
    shortest_distance = g2.size ** 2
    # this has O(n!) complexity
    for graph in permutations(g1):
        graph = extend_graph(graph, g2)
        # this has O(n^2) complexity (which is negligible)
        permutation_distance = calculate_distance(graph, g2)
        if permutation_distance < shortest_distance:
            shortest_distance = permutation_distance

    return shortest_distance


def sort_vertices_by_degree(graph: Graph) -> Graph:
    """
    Renumber the graph vertices by their degree descending
    """
    degrees = [sum(row) for row in graph.matrix]
    # Traverse through all array elements
    for i in range(graph.matrix.shape[0]):
        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(degrees)):
            if degrees[min_idx] > degrees[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        degrees[i], degrees[min_idx] = degrees[min_idx], degrees[i]
        # swap rows
        graph.matrix[[min_idx, i], :] = graph.matrix[[i, min_idx], :]
        # swap columns
        graph.matrix[:, [min_idx, i]] = graph.matrix[:, [i, min_idx]]

    return graph


def aprox_distance(g1: Graph, g2: Graph):
    g1, g2 = order_graphs(g1, g2)
    g1 = sort_vertices_by_degree(g1)
    g2 = sort_vertices_by_degree(g2)
    g1 = extend_graph(g1, g2)
    return calculate_distance(g1, g2)
