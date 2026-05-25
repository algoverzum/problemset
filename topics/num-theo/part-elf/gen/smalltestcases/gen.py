f = open("allsmall.txt")
t = int(f.readline())
have = set()
for case in range(1, t + 1):
    r, c = map(int, f.readline().split("/"))
    if (r, c) not in have:
        with open("input" + str(case) + ".txt", "w") as file:
            file.write(str(r) + "\n")
            file.write(str(c) + "\n")
        file.close()
    have.add((r, c))

f.close()
