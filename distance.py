from graph import Graph


def order_graphs(g1: Graph, g2: Graph) -> (Graph, Graph):
    """Order graphs, return larger as first element of the tuple"""
    return (g1, g2) if g1.size > g2.size else (g2, g1)


def calculate_distance(g1: Graph, g2: Graph) -> int:
    """Calculates distance between two Graphs"""
    assert g1.size == g2.size, "Graphs must have same size"
    # x xor y is the same as abs(x - y) for x,y in (0,1)
    return sum(
        [
            sum([xij ^ yij for xij, yij in zip(xi, yi)])
            for (xi, yi) in zip(g1.matrix, g2.matrix)
        ]
    )


def extend_graph(g1: Graph, g2: Graph) -> Graph:
    """
    Given two graphs with the first one having less vertecies
    returns the first graph extened by the missing number of vertecies
    and filled with compliment edges of the second graph
    """
    assert g1.size <= g2.size
    graph = Graph(size=g2.size)
    graph.matrix[[0, g1.size - 1], [0, g1.size - 1]] = g1.matrix[[0, g1.size - 1], [0, g1.size - 1]]
    graph.matrix[[0, g1.size - 1], [0, g1.size - 1]] = g1.matrix[[0, g1.size - 1], [0, g1.size - 1]]
    graph.matrix[[g1.size, g2.size - 1], :] = g2.matrix[[g1.size, g2.size - 1], :]
    graph.matrix[:, [g1.size, g2.size - 1]] = g2.matrix[:, [g1.size, g2.size - 1]]
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
    shortest_distance = g1.size ** 2
    # this has O(n!) complexity
    for graph in permutations(g2):
        graph = extend_graph(graph, g1)
        # this has O(n^2) complexity (which is negligible)
        permutation_distance = calculate_distance(graph, g1)
        if permutation_distance < shortest_distance:
            shortest_distance = permutation_distance

    return shortest_distance


def sort_vertecies_by_degree(graph: Graph) -> Graph:
    """
    Renumber the graph vertecies by their degree descending
    """
    degrees = [sum(row) for row in graph.matrix]
    ...

def aprox_distance(g1: Graph, g2: Graph):
    g1, g2 = order_graphs(g1, g2)
    g1 = sort_vertecies_by_degree(g1)
    g2 = sort_vertecies_by_degree(g2)
    g2 = extend_graph(g2, g1)
    return calculate_distance(g1, g2)

