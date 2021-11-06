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
