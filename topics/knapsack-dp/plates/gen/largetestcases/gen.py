f = open("alllarge.txt")
t = int(f.readline())
assert t == 100
for case in range(1, 11):
    with open("input" + str(case) + ".txt", "w") as file:
        file.write("10\n")
        for i in range(10):
            n, k, p = map(int, f.readline().split())
            table = [f.readline().strip() for i in range(n)]
            file.write(str(n) + " " + str(k) + " " + str(p) + "\n")
            for line in table:
                file.write(line + "\n")
    file.close()

f.close()
