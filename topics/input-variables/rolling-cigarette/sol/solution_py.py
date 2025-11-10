#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
hossz = int(input())
csikk = int(input())

print(n + n * csikk // hossz, n * csikk % hossz)
