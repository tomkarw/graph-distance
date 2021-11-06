Usage:
```
$ python3 graph-distance.py -h
usage: graph-distance.py [-h] [--exact] [--approximate] [--file FILE] [--random SIZE]

Calculate distance between two graphs.

optional arguments:
  -h, --help     show this help message and exit
  --exact        calculate exact distance (O(n!) time complexity)
  --approximate  calculate approximate distance (O(n^2) time complexity)
  --file FILE    read graphs from file (see examples/ for input format)
  --random SIZE  generate random isomorphic graphs
```

Examples:
```
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
```