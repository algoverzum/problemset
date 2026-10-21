#!/usr/bin/env python3
# @check-accepted: *


def lehet(X, sulyok, N, K, kezdo_indexek=None):
    """
    Ellenőrzi, hogy X maximális terhelés mellett
    el lehet-e osztani a konténereket legfeljebb K kamionba
    """
    kamionok = 1
    aktualis = 0

    if kezdo_indexek is not None:
        kezdo_indexek.clear()
        kezdo_indexek.append(1)

    for i in range(N):
        if aktualis + sulyok[i] > X or (N - i) <= (K - kamionok):
            kamionok += 1
            aktualis = sulyok[i]
            if kezdo_indexek is not None:
                kezdo_indexek.append(i + 1)  # 1-alapú indexelés
        else:
            aktualis += sulyok[i]

        if kamionok > K:
            return False

    return True


def main():
    # Beolvasás
    N, K = map(int, input().split())
    sulyok = list(map(int, input().split()))

    # Kezdeti értékek
    bal = max(sulyok)
    jobb = sum(sulyok)

    # Paraméteres keresés (bináris keresés) a minimális maximumra
    while bal < jobb:
        kozep = (bal + jobb) // 2
        if lehet(kozep, sulyok, N, K):
            jobb = kozep
        else:
            bal = kozep + 1

    optimum = bal
    print(optimum)

    # Kezdőindexek meghatározása
    kezdo_indexek = []
    lehet(optimum, sulyok, N, K, kezdo_indexek)

    # Ellenőrizzük, hogy a kezdőindexek száma megegyezik-e K-val
    if len(kezdo_indexek) != K:
        print(f"hiba: {len(kezdo_indexek)} != {K}")
        return

    # Kiírjuk a kezdőindexeket
    for idx in kezdo_indexek:
        print(idx, end=" ")
    print()


if __name__ == "__main__":
    main()
