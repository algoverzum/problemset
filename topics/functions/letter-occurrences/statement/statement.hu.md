## Betűszámlálás
Írjunk egy függvényt, ami megszámolja, hogy egy szóban hányszor fordul elő egy betű!

### Sablon
Indulj ki az alábbi sablonból (másold be ezt a szerkesztőbe)! Ne változtass a `main` függvényben semmit, mert különben nem lesz elfogadva. Egy `count` nevű függvényt kell definiálnod magadnak, ami két paramétert kap: egy szót, ami `string` típusú és egy betűt, ami `char` típusú. A visszatérési érték pedig a betű előfordulásainak a száma kell, hogy legyen, ami `int` típusú.

```cpp
#include <iostream>
using namespace std;



int main() {
    cout << count("chocolate", 'c') << "\n";
    cout << count("chocolate", 'b') << "\n";
    cout << count("tree", 't') << "\n";
    cout << count("tree", 'e') << "\n";
    cout << count("", 'x') << "\n";
    cout << count("oooooooooo", 'o') << "\n";
    cout << count("shshshshshshshsh", 's') << "\n";
    cout << count("pneumonoultramicroscopicsilicovolcanoconiosis", 'i') << "\n";
}
```

