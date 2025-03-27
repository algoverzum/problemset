#!/usr/bin/env python3
# @check-accepted: *

n = int(input())
city_to_planet = {}
for _ in range(n):
    data = input().split()
    planet, cities = data[0], data[1:]
    for city in cities:
        city_to_planet[city] = planet
m = int(input())
for _ in range(m):
    city = input().strip()
    print(city_to_planet[city])
