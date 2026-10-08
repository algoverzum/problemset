#!/usr/bin/env python3
# @check-accepted: *
from collections import deque


def main():
    # Első sor beolvasása és szétvágása szóközök mentén
    elso_sor = input().split()
    N = int(elso_sor[0])  # Évek száma
    L = int(elso_sor[1])  # Maximális életkor
    K = int(elso_sor[2])  # Szaporodási kor alsó határa

    # A következő L sor beolvasása (kezdeti populáció)
    kezdeti_populacio = []
    for _ in range(L):
        kezdeti_populacio.append(int(input()))

    # A sort fordított sorrendben töltjük fel:
    # A sor elején (bal oldalon) a legidősebbek (L évesek),
    # a végén (jobb oldalon) a legfiatalabbak (1 évesek) lesznek.
    roka_sor = deque(reversed(kezdeti_populacio))

    MOD = 1000000

    # Évek szimulációja N éven keresztül
    for _ in range(N):
        ujszulottek = 0

        # Kiszámoljuk a születő rókákat.
        # Mivel fordított a sorrend, a sor első (L - K + 1) eleme szaporodik.
        szaporodo_korcsoportok = L - K + 1
        for i in range(szaporodo_korcsoportok):
            ujszulottek = (ujszulottek + roka_sor[i]) % MOD

        # 1. Az L évesek elpusztulnak (kivesszük őket a sor elejéről)
        roka_sor.popleft()

        # 2. Az újszülöttek bekerülnek a sor végére (mint 1 évesek)
        roka_sor.append(ujszulottek)

    # Végeredmény kiszámítása: összeadjuk a sorban maradt összes rókát
    osszes_roka = sum(roka_sor) % MOD

    # Kimenet
    print(osszes_roka)


if __name__ == "__main__":
    main()
