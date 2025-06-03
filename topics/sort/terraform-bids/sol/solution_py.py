#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
offers = []
for _ in range(n):
    company_name, cost = input().split()
    offers.append((int(cost), company_name))

offers.sort()

for _, company_name in offers:
    print(company_name)
