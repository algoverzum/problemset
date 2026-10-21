#!/usr/bin/env python3
# @check-accepted: *


def jo(t, K, kapacitas):
    kamionok = 1
    aktualis = 0
    for x in t:
        if aktualis + x <= kapacitas:
            aktualis += x
        else:
            kamionok += 1
            aktualis = x
    return kamionok <= K


def main():
    N, K = map(int, input().split())
    t = list(map(int, input().split()))

    bal = max(t)  # legalább a legnagyobb rakomány
    jobb = sum(t)  # legfeljebb az összes rakomány

    while bal < jobb:
        kozep = (bal + jobb) // 2
        if jo(t, K, kozep):
            jobb = kozep
        else:
            bal = kozep + 1

    print(bal)


if __name__ == "__main__":
    main()
