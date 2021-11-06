#! /bin/python3
import argparse
import numpy as np
from graph import Graph
from distance import exact_distance, aprox_distance


def read_graphs_from_file(filename: str) -> [Graph, Graph]:
    with open(filename, "r") as file_handle:
        lines = file_handle.readlines()
        # read first graph
        graph1 = Graph(size=int(lines[0]))
        for i in range(graph1.size):
            line = lines[i + 1].rstrip()
            graph1.matrix[i] = list(map(int, list(line)))

        # read second graph
        graph2 = Graph(size=int(lines[1 + graph1.size]))
        for i in range(graph2.size):
            line = lines[i + 2 + graph1.size].rstrip()
            graph2.matrix[i] = list(map(int, list(line)))

    return [graph1, graph2]


def run(arguments):
    if file_name := arguments.file:
        [graph1, graph2] = read_graphs_from_file(file_name)
    elif n := arguments.random:
        graph1 = Graph(size=n)
        graph1.matrix = np.random.randint(2, size=(n, n))
        graph2 = graph1.random_permutation()
    else:
        print("either --file or --random flag must be passed")
        return

    if not (arguments.exact or arguments.approximate):
        arguments.exact = True
        arguments.approximate = True

    if arguments.exact:
        print("exact distance: ", exact_distance(graph1, graph2))
    if arguments.approximate:
        print("approximate distance: ", aprox_distance(graph1, graph2))


parser = argparse.ArgumentParser(description="Calculate distance between two graphs.")
parser.add_argument("--exact", action="store_true", help="calculate exact distance (O(n!) time complexity)")
parser.add_argument("--approximate", action="store_true", help="calculate approximate distance (O(n^2) time complexity)")
parser.add_argument("--file", type=str, help="read graphs from file (see examples/ for input format)")
parser.add_argument("--random", type=int, metavar='SIZE', help="generate random isomorphic graphs")


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)
