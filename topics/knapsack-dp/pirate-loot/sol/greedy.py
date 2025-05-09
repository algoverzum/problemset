#!/usr/bin/env python3
# @check-wrong-answer: examples small all

n, s = map(int, input().split())
cargo = [tuple(map(int, input().split())) for _ in range(n)]
cargo.sort(key=lambda x: x[0] / x[1])

val = 0
sum = 0

for value, weight in cargo:
    while sum + weight <= s:
        sum += weight
        val += value

print(val)
