#!/usr/bin/env python3
# @check-accepted: *


def can(X: int, S: int, K: int, a: list) -> bool:
    trucks = 1
    current_sum = 0

    for i in range(X):
        if a[i] > S:
            return False

        if current_sum + a[i] <= S:
            current_sum += a[i]
        else:
            trucks += 1
            current_sum = a[i]

        if trucks > K:
            return False

    return True


def main():
    # Első sor beolvasása: N, K, S
    line1 = input().split()
    if not line1:
        return
    N = int(line1[0])
    K = int(line1[1])
    S = int(line1[2])

    # Második sor beolvasása: a tárgyak súlya
    line2 = input().split()
    a = [int(x) for x in line2]

    # Bináris (parametrikus) keresés a tárgyak darabszámára
    lo = 0
    hi = N

    while lo < hi:

        mid = (lo + hi + 1) // 2

        if can(mid, S, K, a):
            lo = mid
        else:
            hi = mid - 1

    print(lo)


if __name__ == "__main__":
    main()
