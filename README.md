Usage:
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

$ # save generated graph to file after calculations
$ python3 graph-distane.py --random 1000 --approximate -o graph-n1000.txt
approximate distance: 495038
```
