#!/usr/bin/env python3
# @check-accepted: *

N = int(input())
books = []

for i in range(N):
    data = input().split()
    title = data[0]
    year = int(data[1])
    books.append((title, year))

books.sort(key=lambda x: (x[1], x[0]))
for title, year in books:
    print(f"{title} {year}")
