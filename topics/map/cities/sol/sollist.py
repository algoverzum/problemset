#!/usr/bin/env python3

n = int(input())
city_to_planet = []
for _ in range(n):
    planet, city_count = input().split()
    cities = input().split()
    for city in cities:
        city_to_planet.append((city, planet))
city_to_planet.sort()
m = int(input())
for _ in range(m):
    city = input()
    if city_to_planet[-1][0] == city:
        print(city_to_planet[-1][1])
    else:
        lo = 0
        hi = len(city_to_planet) - 1
        while hi - lo > 1:
            mid = (hi + lo) // 2
            if city_to_planet[mid][0] > city:
                hi = mid
            else:
                lo = mid
        print(city_to_planet[lo][1])
