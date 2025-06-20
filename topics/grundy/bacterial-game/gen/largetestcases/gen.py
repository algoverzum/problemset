f = open("large.in")
t = int(f.readline())
for case in range(1, t + 1):
    r, c = map(int, f.readline().split())
    table = [f.readline().strip() for i in range(r)]
    with open("input" + str(case) + ".txt", "w") as file:
        file.write(str(r) + " " + str(c) + "\n")
        for line in table:
            file.write(line + "\n")
    file.close()

f.close()
