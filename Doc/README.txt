Podstawowo algorytm pobiera ścieżkę do pliku z reprezentacją dwóch grafów (patrz katalog /examples dla przykładów formaty danych) jako pierwszy argument pozycyjny.
Dodatkowo algorytm może wygenerować nowy graf losowy o dowolnym rozmiarze z użyciem flagi "-r/--random N".
Taki graf może zostać zapisany do pliku z użyciem flagi "-o OUTPUT-FILE".

Przykładowe wywołania:

# grafy izomorficzne

graph-distance ../examples/graph-n2-0.txt

graph-distance ../examples/graph-n5-0.txt

graph-distance --random 5

graph-distance --random 7 --approximate

graph-distance ../examples/graph-n10-0.txt --approximate

graph-distance --file examples/graph-n100-0.txt --approximate

graph-distance--random 1000 --approximate -o graph-n1000.txt

# grafy o różnej liczbie wierzchołków

graph-distance ../examples/graph-semi-iso-n5-n3-0.txt

# grafy nieizomorficzne

graph-distance ../examples/graph-non-iso-n5-0.txt
