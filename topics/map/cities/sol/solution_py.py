#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
city_to_planet = {}
for _ in range(n):
    planet, *cities = input().split()
    for city in cities:
        city_to_planet[city] = planet
m = int(input())
for _ in range(m):
    city = input()
    print(city_to_planet[city])
