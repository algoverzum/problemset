#!/usr/bin/env python3
# @check-accepted: *

# Eldönti, hogy a könyvek kioszthatók-e legfeljebb k másolónak úgy,
# hogy senki ne kapjon limit oldalnál többet.
def ellenoriz(konyvek, k, limit):
    masolok = 1
    aktualis = 0
    for oldal in konyvek:
        # Egyetlen könyv sem fér bele
        if oldal > limit:
            return False
        if aktualis + oldal <= limit:
            aktualis += oldal
        else:
            masolok += 1
            aktualis = oldal
    return masolok <= k


def main():
    n, k = map(int, input().split())
    konyvek = list(map(int, input().split()))

    bal = max(konyvek)  # legalább a legnagyobb könyv
    jobb = sum(konyvek)  # legfeljebb az összes oldal

    megoldas = jobb

    while bal <= jobb:
        kozep = (bal + jobb) // 2
        if ellenoriz(konyvek, k, kozep):
            megoldas = kozep
            jobb = kozep - 1
        else:
            bal = kozep + 1

    print(megoldas)


if __name__ == "__main__":
    main()
