# graph-distance
This program allows to calculate the distance between two graphs which are represented as matricies.
Distance is measure as sum of absolute differences between corresponding cells.
For graphs (and thus matricies) of different number of nodes, the smaller one is extended by the missinig amout of nodes
and filled with vertecies that are negation of the bigger graph (so if the vertex was in the bigger one, it will be missing in the smaller).

One issue with representing a graph as a matrix is that nodes can be numbered in many ways.
Even isomorphic graphs could have distance greater than zero if the corresponding nodes had different values assigned.

We provide two algorithms to address that issue: exact algorithm (with a flag -e/--exact) that always calculates exact distance between two graphs.
It does so by iterating over all possible node numberings of one of the grahs and choosing the smallest value.
This algorithm will always return zero for isomorphic graphs, but at the cost of O(n!) time complexity (in practice this is achieavable for graphs up to n=10).

Second algorithm does not provide exact value, but only approximates it (when using the flag -a/--approximate).
It sorts both graphs by the degree of their nodes, rasing the chance that corresponding vertecies get assinged the same value.
THIS CAN RETURN DISTANCE OTHER THAT ZERO FOR ISOMORPHIC GRAPHS, but gains much better time complexity at O(n^2).
In practice we were able to easily calculate distance of graphs with up to 5000 nodes on a local machine in seconds.

In the simples case the program takes a path to a file with a representation of two graphs (see /examples for data format) as first positional argument
and calculates the distance using both algorithms.
Additionally the program can generate a new random graph (with the use of -r/--random) flag. Such graph can be saved to file with the use of -o flag.

# Usage:
```
$ python3 graph-distance.py --help
usage: graph-distance.py [-h] [-e] [-a] [-o OUTPUT-FILE]
                         (-f INPUT-FILE | -r SIZE)

Calculate distance between two graphs.

optional arguments:
  -h, --help            show this help message and exit
  -e, --exact           calculate exact distance (O(n!) time complexity)
  -a, --approximate     calculate approximate distance (O(n^2) time
                        complexity)
  -o OUTPUT-FILE, --output OUTPUT-FILE
                        save generated graphs to file
  -f INPUT-FILE, --file INPUT-FILE
                        read graphs from file (see examples/ for input format)
  -r SIZE, --random SIZE
                        generate random isomorphic graphs
```

# Examples:
```
$ python3 graph-distance.py ./examples/graph-n5-0.txt
exact distance:  0
approximate distance: 4

$ python3 graph-distance.py --random 5
exact distance:  0
approximate distance:  8

$ python3 graph-distance.py --random 5 --exact
exact distance:  0

$ python3 graph-distance.py --random 7 --approximate
approximate distance:  8

$ python3 graph-distance.py --file examples/graph0.txt
exact distance:  0
approximate distance:  6

$ # save generated graph to file after calculations
$ python3 graph-distane.py --random 1000 --approximate -o graph-n1000.txt
approximate distance: 495038
```
