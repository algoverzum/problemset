def generate_assignments(N, forbidden):
    """Összes független halmaz előállítása lexikografikus sorrendben"""
    result = []

    # Minden részhalmaz vizsgálata
    for mask in range(1 << N):
        valid = True
        subset = []

        # Részhalmaz összeállítása
        for i in range(N):
            if mask & (1 << i):
                subset.append(i + 1)

        # Ellenőrizzük a tiltott éleket
        for a, b in forbidden:
            if (mask & (1 << (a - 1))) and (mask & (1 << (b - 1))):
                valid = False
                break

        if valid:
            result.append(subset)

    # Rendezés: először az üres halmaz, utána lexikografikus sorrend
    # A lexikografikus sorrend: összehasonlítjuk az elemeket sorban
    result.sort(key=lambda x: (len(x) == 0, x))
    # Az üres halmaz első, a többi lexikografikusan rendezve

    return result


def write_test_case(idx, N, M, forbidden):
    """Teszteset kiírása fájlba"""
    # Bemenet
    with open(f'input{idx}.txt', 'w') as f:
        f.write(f"{N} {M}\n")
        for a, b in forbidden:
            f.write(f"{a} {b}\n")

    # Kimenet
    results = generate_assignments(N, forbidden)
    with open(f'output{idx}.txt', 'w') as f:
        f.write(str(len(results)) + '\n')
        for subset in results:
            if subset:
                f.write(' '.join(map(str, subset)) + '\n')
            else:
                f.write('\n')  # Üres sor


# Tesztesetek definiálása
test_cases = [
    # 1. Minimális
    (1, 0, []),

    # 2. N=2, nincs tiltás
    (2, 0, []),

    # 3. N=2, egy tiltás
    (2, 1, [(1, 2)]),

    # 4. N=3, nincs tiltás
    (3, 0, []),

    # 5. N=3, egy tiltás
    (3, 1, [(1, 2)]),

    # 6. N=3, lánc
    (3, 2, [(1, 2), (2, 3)]),

    # 7. N=3, teljes gráf
    (3, 3, [(1, 2), (2, 3), (1, 3)]),

    # 8. N=4, példa
    (4, 2, [(1, 2), (2, 3)]),

    # 9. N=4, háromszög
    (4, 3, [(1, 2), (2, 3), (1, 3)]),

    # 10. N=5, nincs tiltás
    (5, 0, []),

    # 11. N=8, néhány tiltás (nagyobb)
    (8, 6, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]),

    # 12. N=15, néhány tiltás (nagyobb)
    (15, 8, [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9)]),
]

# Tesztek generálása
for idx, (N, M, forbidden) in enumerate(test_cases):
    write_test_case(idx, N, M, forbidden)
    print(f"Teszt {idx} elkészült: N={N}, M={M}")
