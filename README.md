# graph-distance
This program allows calculating the distance between two graphs represented as matrices.
The distance is measured as a sum of absolute differences between corresponding cells.
For graphs (and thus matrices) of a different number of nodes, the smaller one is extended by the missing amount of nodes
and filled with vertices that are the negation of the larger graph (so if the vertex was in the larger one, it will be missing in the smaller).

One issue with representing a graph as a matrix is that nodes can be ordered in many ways.
Even isomorphic graphs could have a distance greater than zero if the corresponding nodes had different values assigned.

We provide two algorithms to address that issue: an exact algorithm (with a flag `-e/--exact`) that calculates the exact distance between two graphs.
It does so by iterating over all possible node numberings of one of the graphs and choosing the smallest value.
This algorithm will always return zero for isomorphic graphs, but at the cost of `O(n!)` time complexity (in practice this is achievable for graphs up to n=10).

The second algorithm does not provide an exact value, but only approximates it (when using the flag `-a/--approximate`).
It sorts both graphs by the degree of their nodes, raising the chance that corresponding vertices get assigned the same value.
THIS CAN RETURN DISTANCE OTHER THAT ZERO FOR ISOMORPHIC GRAPHS but gains much better time complexity at `O(n^2)`.
In practice, we were able to calculate the distance of graphs with up to 5000 nodes on a local machine in seconds.

In the simplest case, the program takes a path to a file with a representation of two graphs (see /examples for data format) as the first positional argument
and calculates the distance using both algorithms.
Additionally, the program can generate a new random graph (by using the `-r/--random`) flag. This generated graph can be saved to a file with the use of the -o flag.

# Usage:
```
$ python3 graph-distance.py --help
usage: graph-distance.py [-h] [-e] [-a] [-o OUTPUT-FILE]
                         (-f INPUT-FILE | -r SIZE)

Calculate the distance between the two graphs.

positional arguments:
  INPUT_FILE            read graphs from file (see examples/ for input format)

optional arguments:
  -h, --help            show this help message and exit
  -e, --exact           calculate exact distance (O(n!) time complexity)
  -a, --approximate     calculate approximate distance (O(n^2) time
                        complexity)
  -o OUTPUT-FILE, --output OUTPUT-FILE
                        save generated graphs to file
  -y                    skip confirmations
  -q, --quiet           don't print graphs
  -r SIZE, --random SIZE
                        generate random isomorphic graphs
```

# Examples:
```
$ python3 graph-distance.py examples/graph-n5-0.txt
exact distance:  0
approximate distance: 4

$ python3 graph-distance.py --random 5
exact distance:  0
approximate distance:  8

$ python3 graph-distance.py --random 5 --exact
exact distance:  0

$ python3 graph-distance.py --random 7 --approximate
approximate distance:  8

$ # this will require confirmation
$ python3 graph-distance.py --random 8
Are you sure you want to calculate exact distance of graph size 8? [y/n] y
exact distance:  0
approximate distance: 30 

$ # save generated graph to file after calculations
$ python3 graph-distane.py --random 1000 --approximate -o graph-n1000.txt
approximate distance: 495038
```

