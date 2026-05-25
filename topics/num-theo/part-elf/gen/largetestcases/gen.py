ff = open("../smalltestcases/allsmall.txt")
t = int(ff.readline())
have = set()
for case in range(1, t + 1):
    r, c = map(int, ff.readline().split("/"))
    have.add((r, c))
f = open("alllarge.txt")
t = int(f.readline())
for case in range(1, t + 1):
    r, c = map(int, f.readline().split("/"))
    if (r, c) not in have:
        with open("input" + str(case) + ".txt", "w") as file:
            file.write(str(r) + "\n")
            file.write(str(c) + "\n")
        file.close()
    have.add((r, c))

f.close()
