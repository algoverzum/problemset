#!/usr/bin/env python3
# @check-accepted: examples
# @check-wrong-answer: all

N = int(input())
A = [int(x) for x in input().split()]

vals = sorted([(A[i], i + 1) for i in range(N)], reverse=True)
a, b = [], []
suma = sumb = 0
for v, i in vals:
    if suma < sumb:
        a.append(i)
        suma += v
    else:
        b.append(i)
        sumb += v

print(abs(suma - sumb))
print(len(a), *a)
print(len(b), *b)
