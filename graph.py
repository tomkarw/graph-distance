import numpy as np
import random


class Graph:
    matrix: np.array 

    def __init__(self, size: int):
        """Initialize empty graph"""
        self.matrix = np.empty([size, size], dtype=bool)

    def __repr__(self):
        return f"Graph(size={self.size}, matrix={self.matrix}"

    @property
    def size(self):
        return self.matrix.shape[0]

    def random_permutation(self):
        graph = Graph(size=self.size)
        graph.matrix = self.matrix.copy()

        order = [random.random() for _ in graph.matrix]

        # Traverse through all array elements
        for i in range(graph.size):
            # Find the minimum element in remaining
            # unsorted array
            min_idx = i
            for j in range(i + 1, len(order)):
                if order[min_idx] > order[j]:
                    min_idx = j

            # Swap the found minimum element with
            # the first element
            order[i], order[min_idx] = order[min_idx], order[i]
            # swap rows
            graph.matrix[[min_idx, i], :] = graph.matrix[[i, min_idx], :]
            # swap columns
            graph.matrix[:, [min_idx, i]] = graph.matrix[:, [i, min_idx]]

        assert np.sum(self.matrix) == np.sum(graph.matrix), "random permutation has an error"
        return graph


def read_graphs_from_file(filename: str) -> [Graph, Graph]:
    with open(filename, "r") as file_handle:
        lines = file_handle.readlines()
        # read first graph
        graph1 = Graph(size=int(lines[0]))
        for i in range(graph1.size):
            line = lines[i + 1].split(" ")
            graph1.matrix[i] = list(map(int, list(line)))

        # read second graph
        graph2 = Graph(size=int(lines[1 + graph1.size]))
        for i in range(graph2.size):
            line = lines[i + 2 + graph1.size].split(" ")
            graph2.matrix[i] = list(map(int, list(line)))

    return [graph1, graph2]


def write_graphs_to_file(graph1: Graph, graph2: Graph, filename: str):
    with open(filename, "w") as file_handle:
        file_handle.write(f"{graph1.size}\n")
        for row in graph1.matrix:
            file_handle.write(" ".join(map(lambda cell: str(int(cell)), row)))
            file_handle.write("\n")
        file_handle.write(f"{graph2.size}\n")
        for row in graph2.matrix:
            file_handle.write(" ".join(map(lambda cell: str(int(cell)), row)))
            file_handle.write("\n")

def print_graphs(graph1: Graph, graph2: Graph):
    pass
