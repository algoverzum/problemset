## Összeg A-tól B-ig
Írj függvényt, ami kiszámolja $A$-tól $B$-ig a számok összegét! $A$ és $B$ egész számok, és $A \le B$.

### Korlátok
* $-10\,000 \le A \le B \le 10\,000$

### Sablon
Indulj ki az alábbi sablonból (másold be ezt a szerkesztőbe)! Ne változtass a `main` függvényben semmit, mert különben nem lesz elfogadva. A `sum_between` függvény belsejét kell megírnod, ami paraméterként kapja a két számot, $A$-t és $B$-t.

```cpp
#include <iostream>
using namespace std;

int sum_between(int a, int b) {

}

int main() {
    cout << sum_between(3, 5) << "\n";
    cout << sum_between(0, 10) << "\n";
    cout << sum_between(42, 42) << "\n";
    cout << sum_between(-1, 1) << "\n";
    cout << sum_between(-5, 3) << "\n";
    cout << sum_between(100, 1000) << "\n";
    cout << sum_between(3141, 5926) << "\n";
    cout << sum_between(1, 10000) << "\n";
}
```

