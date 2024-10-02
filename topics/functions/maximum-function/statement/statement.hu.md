## Sorozat maximuma
Írj függvényt, ami egy visszaadja egy egész számokból álló sorozat legnagyobb elemét!

### Korlátok
* $1 \le N \le 20$, ahol $N$ jelöli a sorozat hosszát

### Sablon
Indulj ki az alábbi sablonból (másold be ezt a szerkesztőbe)! Ne változtass a `main` függvényben semmit, mert különben nem lesz elfogadva. Egy `maximum` nevű függvényt kell definiálnod, aminek egyetlen paramétere `vector<int>` típusú, és egy `int` értéket ad vissza.

```cpp
#include <iostream>
#include <vector>
using namespace std;



int main() {
    cout << maximum({3, 1, 4, 5, 2}) << "\n";
    cout << maximum({6, 5, 4, 3, 2, 1}) << "\n";
    cout << maximum({-4, -3, -2, -1}) << "\n";
    cout << maximum({0}) << "\n";
    cout << maximum({42, 42, 42, 42, 42, 42, 42}) << "\n";
    cout << maximum({100, 101, 100, 101, 100, 101}) << "\n";
    cout << maximum({3456, 8989, 432, 982, 3497, 34, 5430, 2134, 1092, 9997}) << "\n";
}

```
