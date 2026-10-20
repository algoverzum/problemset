#!/usr/bin/env python3
# @check-accepted: *


def check(R: int, N: int, K: int, a: list) -> bool:
    stations_used = 0
    i = 0

    while i < N:
        # Elhasználunk egy állomást a jelenlegi legelső lefedetlen faluhoz (a[i])
        stations_used += 1

        # Ha több állomás kellene, mint amennyi elérhető, ez az R sugár kevés
        if stations_used > K:
            return False

        # A maximális koordináta, ameddig ez az állomás elnyúlhat (2 * R átfogás)
        max_reach = a[i] + 2 * R

        # Mohón átugorjuk az összes olyan falut, ami beleesik ebbe a sávba
        while i < N and a[i] <= max_reach:
            i += 1

    return stations_used <= K


def main():
    # Első sor beolvasása (N és K)
    line1 = input().split()
    if not line1:
        return
    N = int(line1[0])
    K = int(line1[1])

    # Második sor beolvasása (falvak koordinátái)
    line2 = input().split()
    a = [int(x) for x in line2]

    # Parametrikus (bináris) keresés a minimális R hatósugárra
    low = 0
    high = a[N - 1] - a[0]
    ans = high

    while low <= high:
        mid = low + (high - low) // 2

        if check(mid, N, K, a):
            ans = mid  # A mid egy lehetséges sugár, elmentjük
            high = mid - 1  # Megpróbálunk kisebb sugarat keresni
        else:
            low = mid + 1  # Nagyobb sugárra van szükség

    print(ans)


if __name__ == "__main__":
    main()
