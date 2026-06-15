f = open("alllarge.txt")
t = int(f.readline())
for case in range(1, t + 1):
    n, k = map(int, f.readline().split())
    line = f.readline().strip()
    with open("input" + str(case) + ".txt", "w") as file:
        file.write(str(n) + " " + str(k) + "\n")
        file.write(line + "\n")
    file.close()

f.close()
