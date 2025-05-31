#!/usr/bin/env python3
# @check-accepted: *

from operator import itemgetter, attrgetter

n = int(input())
medals = []
for i in range(n):
    medal = [int(x) for x in input().split()]
    tup = (medal[0], medal[1], medal[2], (i + 1) * -1)
    medals.append(tup)

medals = sorted(medals, key=itemgetter(0, 1, 2, 3), reverse=True)

for i in medals:
    print(i[3] * (-1), end=" ")
print()
