## Közös betűk
Írj függvényt, ami két csupa angol kisbetűből álló stringnek megadja a közös betűit (common_letters). Az eredmény egy string legyen, amiben a közös betűk ábécé sorrendben szerepelnek, minden betű csak egyszer! Például `common_letters("apple", "leaves")` eredménye `"ael"`. Írhatsz hozzá segédfüggvényt is.

### Sablon
Indulj ki az alábbi sablonból (másold be ezt a szerkesztőbe)! Ne változtass a `main` függvényben semmit, mert különben nem lesz elfogadva. Ügyelj arra, hogy a megadott nevű függvényt definiáld, megfelelő paraméterekkel és visszatérési típussal.

```cpp
#include <iostream>
using namespace std;



int main() {
    cout << common_letters("apple", "leaves") << "\n";
    cout << common_letters("chocolate", "catching") << "\n";
    cout << common_letters("chocolate", "chocolate") << "\n";
    cout << common_letters("chocolate", "banana") << "\n";
    cout << common_letters("chocolate", "drums") << "\n";
    cout << common_letters("tree", "e") << "\n";
    cout << common_letters("", "x") << "\n";
    cout << common_letters("oooooooooo", "ooo") << "\n";
    cout << common_letters("shshshshshshshsh", "shake") << "\n";
    cout << common_letters("pneumonoultramicroscopicsilicovolcanoconiosis", "methylenedioxymethamphetamine") << "\n";
}

```

