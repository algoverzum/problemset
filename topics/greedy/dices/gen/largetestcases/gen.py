f = open("ts2_input.txt")
t = int(f.readline())
for case in range(1, t + 1):
    n = int(f.readline())
    S = list(map(int, f.readline().split()))
    with open("input" + str(case) + ".txt", "w") as file:
        file.write(str(n) + "\n")
        line = " ".join(map(str, S))
        file.write(line + "\n")
    file.close()

f.close()
