import numpy as np


class Graph:
    matrix: np.array 

    def __init__(self, size: int):
        """Initialize empty graph"""
        self.matrix = np.empty([size, size], dtype=int)

    def __repr__(self):
        return f"Graph(size={self.size}, matrix={self.matrix}"

    @property
    def size(self):
        return self.matrix.shape[0]
