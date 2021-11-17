Program graph-distance pozwala na obliczenie odległości dwóch grafów reprezentowanych jako macierze.
Odległość jest obliczana jako suma po całych macierzach absolutnej różnicy odpowiadających komórek.
Dla grafów o różnej wielkości, mniejszy z grafów uzupełniany jest dopełnieniem krawędzi grafu większego.

Problemem reprezentacji grafu jako macierz jest możliwość różnych numeracji wierzchołków.
Nawet grafy izomorficzne mogą dać wartość inną od zera, jeśli odpowiadające sobie wierzchołki mają przypisane różne liczby.

Udostępnione są dwa algorymtmy adresujące ten problem: dokładny (odblokowywany flagą -e/--exact) obliczający dokładną odległość między grafami,
iterujący po wszystkich możliwych numerowaniach i wybierający to najbardziej zbliżone do drugiego grafu.
Ten algorytm dla grafów izomorficznych zawsze zwróci zero, ale jego złożoność czasowa wynosi O(n!) (w praktyce dla n=10 obliczenia trwają ok 7s).
Drugi z algorytmów nie daje dokładnej wartości, a jedynie ją approksymuje (odblokowywany flagą -a/--approximate). Sortuje on oba grafy po stopniu wierzchołków, zwiększając szansę na
poprawną numerację odpowiadających sobie wierzchołków. MOŻE ON DAĆ WARTOŚĆ RÓŻNĄ OD ZERA DLA GRAFÓW IZOMORFICZNYCH, ale zyskuje lepszą złożoność
czasową wynoszącą O(n^2), w praktyce udało nam się policzyć wartości dla grafów o nawet 5000 wierzchołków.

Podstawowo algorytm pobiera ścieżkę do pliku z reprezentacją dwóch grafów (patrz katalog /examples dla przykładów formaty danych) jako pierwszy argument pozycyjny.
Dodatkowo algorytm może wygenerować nowy graf losowy o dowolnym rozmiarze z użyciem flagi "-r/--random N".
Taki graf może zostać zapisany do pliku z użyciem flagi "-o OUTPUT-FILE".
Przykładowe wywołania:

# grafy izomorficzne

graph-distance ./examples/graph-n2-0.txt

graph-distance ./examples/graph-n5-0.txt

graph-distance --random 5

graph-distance --random 7 --approximate

graph-distance ./examples/graph-n10-0.txt --approximate

graph-distance --file examples/graph-n100-0.txt --approximate

graph-distance--random 1000 --approximate -o graph-n1000.txt

# grafy o różnej liczbie wierzchołków

graph-distance ./examples/graph-semi-iso-n5-n3-0.txt

# grafy nieizomorficzne

graph-distance ./examples/graph-non-iso-n5-0.txt
