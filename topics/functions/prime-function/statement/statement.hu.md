## Prímteszt
Írj függvényt, ami egy pozitív számról eldönti, hogy prímszám-e! (A prímek olyan 1-nél nagyobb egész számok, amelyeknek nincs osztójuk 1-en és önmagukon kívül.)

### Korlátok
* $1 \le N \le 1000$

### Sablon
Indulj ki az alábbi sablonból (másold be ezt a szerkesztőbe)! Ne változtass a `main` függvényben semmit, mert különben nem lesz elfogadva. A `prime` függvény belsejét kell megírnod, ami paraméterként kapja az $N$ értékét.

```cpp
#include <iostream>
using namespace std;

bool prime(int n) {

}

int main() {
    for (int i = 1; i <= 1000; i++) {
        if (prime(i)) cout << i << " ";
    }
    cout << "\n";
}
```

