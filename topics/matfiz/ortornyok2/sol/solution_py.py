import sys


def main():
    data = sys.stdin.read().split()
    N, M = int(data[0]), int(data[1])

    forbidden = [[] for _ in range(N + 1)]
    for i in range(M):
        a = int(data[2 + 2 * i])
        b = int(data[3 + 2 * i])
        forbidden[a].append(b)
        forbidden[b].append(a)

    current = []
    best = []

    def ok(x):
        """Ellenőrzi, hogy az új torony felvehető-e a jelenlegi kiválasztottak mellé."""
        for y in current:
            if x in forbidden[y]:
                return False
        return True

    def can_improve(idx):
        """Pruning: megnézzük, hogy van-e esély jobb megoldásra."""
        remaining = N - idx + 1
        return len(current) + remaining >= len(best)

    def backtrack(idx):
        nonlocal best
        if idx > N:
            if len(current) > len(best):
                best = current[:]
            elif len(current) == len(best) and current < best:
                # Pythonban a listák < operátora lexikografikusan hasonlít
                best = current[:]
            return

        # PRUNING: ha innen már nem lehet jobb megoldás
        if not can_improve(idx):
            return

        # 1. ág: NEM választjuk
        backtrack(idx + 1)

        # 2. ág: választjuk (ha lehet)
        if ok(idx):
            current.append(idx)
            backtrack(idx + 1)
            current.pop()

    backtrack(1)

    print(len(best))
    print(" ".join(map(str, best)))


main()