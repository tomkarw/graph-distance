import sys
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


def run(filename: str):
    [graph1, graph2] = read_graphs_from_file(filename)
    print(graph1, graph2)
    print(exact_distance(graph1, graph2))
    print(aprox_distance(graph1, graph2))


if __name__ == "__main__":
    filename = sys.argv[1]
    run(filename)
