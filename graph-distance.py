#!/usr/bin/python3

import argparse
import copy
import numpy as np
from graph import Graph, read_graphs_from_file, write_graphs_to_file, print_graphs
from distance import exact_distance, approx_distance

GRAPH_SIZE_THRESHOLD = 7

def run(arguments):
    if file_name := arguments.file:
        try:
            [graph1, graph2] = read_graphs_from_file(file_name)
        except:
            print(f"Error: failed reading graphs from file, is the file name '{file_name}' correct?")
            exit(1)

    elif n := arguments.random:
        graph1 = Graph(size=n)
        graph1.matrix = np.random.randint(2, size=(n, n))
        graph2 = graph1.random_permutation()
    else:
        raise "unreachable"

    if not (arguments.exact or arguments.approximate):
        arguments.approximate = True

    if arguments.exact:
        calc_exact = True
        if not arguments.y:
            if (size := max(graph1.size, graph2.size)) > GRAPH_SIZE_THRESHOLD:
                answer = input(f"Are you sure you want to calculate exact distance of graph size {size}? [y/n] ")
                if answer not in ("y", "yes"):
                    calc_exact = False
        if calc_exact:
            if not arguments.quiet:
                print("EXACT DISTANCE")
                print("Input matrices")
                print_graphs(graph1, graph2)
            distance, graph1_changed, graph2_changed = exact_distance(graph1, graph2)
            if not arguments.quiet:
                print("After modification")
                print_graphs(graph1_changed, graph2_changed)
            print("exact distance: ", distance)

    if arguments.approximate:
        if not arguments.quiet:
            print("APPROXIMATE DISTANCE")
            print("Input matrices")
            print_graphs(graph1, graph2)
        distance, graph1_changed, graph2_changed = approx_distance(graph1, graph2)
        if not arguments.quiet:
            print("After modification")
            print_graphs(graph1_changed, graph2_changed)
        print("approximate distance: ", distance)

    if arguments.output:
        write_graphs_to_file(graph1, graph2, filename=arguments.output)

parser = argparse.ArgumentParser(description="Calculate distance between two graphs.")
parser.add_argument("-e", "--exact", action="store_true", help="calculate exact distance (O(n!) time complexity)")
parser.add_argument("-a", "--approximate", action="store_true", help="calculate approximate distance (O(n^2) time complexity)")
parser.add_argument("-o", "--output", type=str, metavar='OUTPUT-FILE', help="save generated graphs to file")
parser.add_argument("-y", action="store_true", help="skip confirmations")
parser.add_argument("-q", "--quiet", action="store_true", help="don't print graphs")
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("file", metavar="INPUT-FILE", help="read graphs from file (see examples/ for input format)", nargs="?")
group.add_argument("-r", "--random", type=int, metavar='SIZE', help="generate random isomorphic graphs")


if __name__ == "__main__":
    args = parser.parse_args()
    run(args)

