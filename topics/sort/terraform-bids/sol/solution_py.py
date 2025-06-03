#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
offers = []
for _ in range(n):
    company, bid = input().split()
    offers.append((int(bid), company))

offers.sort()

for _, company in offers:
    print(company)
