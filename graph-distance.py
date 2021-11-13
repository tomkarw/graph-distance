#!/usr/bin/python3
import argparse
import numpy as np
from graph import Graph, read_graphs_from_file, write_graphs_to_file
from distance import exact_distance, aprox_distance


def run(arguments):
    if file_name := arguments.file:
        [graph1, graph2] = read_graphs_from_file(file_name)
    elif n := arguments.random:
        graph1 = Graph(size=n)
        graph1.matrix = np.random.randint(2, size=(n, n))
        graph2 = graph1.random_permutation()
    else:
        raise "unreachable"

    if not (arguments.exact or arguments.approximate):
        arguments.exact = True
        arguments.approximate = True

    if arguments.exact:
        print("exact distance: ", exact_distance(graph1, graph2))
    if arguments.approximate:
        print("approximate distance: ", aprox_distance(graph1, graph2))

    if arguments.output:
        write_graphs_to_file(graph1, graph2, filename=arguments.output)


parser = argparse.ArgumentParser(description="Calculate distance between two graphs.")
parser.add_argument("--exact", action="store_true", help="calculate exact distance (O(n!) time complexity)")
parser.add_argument("--approximate", action="store_true", help="calculate approximate distance (O(n^2) time complexity)")
parser.add_argument("-o", "--output", type=str, metavar='OUTPUT-FILE', help="save generated graphs to file")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--file", type=str, metavar="INPUT-FILE", help="read graphs from file (see examples/ for input format)")
group.add_argument("--random", type=int, metavar='SIZE', help="generate random isomorphic graphs")


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)
