#!/usr/bin/env python3
# @check-accepted: *
def main():
    # Első sor: K és M
    K, M = map(int, input().split())

    # Második sor: N
    N = int(input())

    # Igények tárolása (1..365 napok)
    igenyek = [0] * 366  # index 0-t nem használjuk
    for _ in range(N):
        nap = int(input())
        if 1 <= nap <= 365:  # biztonsági ellenőrzés
            igenyek[nap] += 1

    # Faházak foglaltsági állapota
    fszabad = [0] * (K + 1)  # 1..K faházak
    megold = 0

    # Napok végigjárása
    for nap in range(1, 366):
        # Amíg van igény ezen a napon
        while igenyek[nap] > 0:
            # Keresünk egy szabad faházat
            j = 1
            while j <= K and fszabad[j] > nap:
                j += 1

            if j <= K:
                megold += 1
                igenyek[nap] -= 1
                fszabad[j] = nap + M
            else:
                break  # Nincs szabad faház ezen a napon
    print(megold)


if __name__ == "__main__":
    main()

"""Alternatív megoldás
def main():
    # Első sor: K és M
    K, M = map(int, input().split())

    # Második sor: N
    N = int(input())

    # Igények beolvasása
    igenyek = []
    for _ in range(N):
        igenyek.append(int(input()))

    # Rendezés a kezdőnap szerint
    igenyek.sort()

    # A faházakban tároljuk, hogy mikor szabadulnak fel
    # Kezdetben minden faház szabad (0. naptól)
    fahazak = [0] * K

    elfogadott = 0

    for kezdet in igenyek:
        # Megkeressük a legkorábban felszabaduló faházat
        legkorabbi_index = 0
        for j in range(1, K):
            if fahazak[j] < fahazak[legkorabbi_index]:
                legkorabbi_index = j

        # Ha a legkorábban felszabaduló faház már szabad a kezdetkor
        if fahazak[legkorabbi_index] <= kezdet:
            elfogadott += 1
            # A faház a kezdet + M nap múlva szabadul fel
            fahazak[legkorabbi_index] = kezdet + M
        # Különben nem tudjuk elfogadni ezt az igényt

    print(elfogadott)


if __name__ == "__main__":
    main()
"""
