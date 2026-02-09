#!/usr/bin/env python3
# @check-accepted: *


def main():
    N = int(input())
    data = []
    eaters = set()

    for i in range(N):
        eater, eaten = input().split()
        data.append((eater, eaten))
        eaters.add(eater)

    # Kezdetben minden evő állat potenciálisan csak növényevő
    only_plants = eaters.copy()

    for eater, eaten in data:
        # Ha állatot eszik, akkor kiesik
        if eaten in eaters:
            only_plants.discard(eater)

    print(len(only_plants))
    for animal in sorted(only_plants):
        print(animal)


if __name__ == "__main__":
    main()
