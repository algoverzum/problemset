## Republic Starmap

The galaxy is divided into two factions: the Republic and the Separatists. The Republic controls the first $K$ planets, while the Separatists control the rest. The Republic wants to ensure efficient communication and transportation between all planets (including the separatist ones, because they have to travel there sometimes for diplomatic reasons), but they can only use routes that pass through Republic-controlled planets.

The galaxy's transportation network is represented as a **directed graph**. This means that the distance from planet $A$ to planet $B$ may not be the same as the distance from planet $B$ to planet $A$, or there may be a route in one direction but not the other.

Your task is to calculate the shortest paths between all planets using only routes that pass through Republic-controlled planets. (A route $P_1 \to P_2 \to \dots \to P_q$ is valid, if planets $P_2, P_3, \dots, P_{q-1}$ are controlled by the Republic.)

### Input
The first line of the input contains two integers $N$ and $K$ ($1 \le K \le N \le 100$) — the total number of planets and the number of Republic-controlled planets, respectively.

The next $N$ lines each contain $N$ integers. The $j$-th integer in the $i$-th line represents the distance from planet $i$ to planet $j$. If there is no direct route from planet $i$ to planet $j$, the distance is represented as $-1$.

### Output
Print an $N \times N$ matrix, where the value in the $i$-th row and $j$-th column represents the shortest distance from planet $i$ to planet $j$ using only Republic-controlled planets. If no such path exists between two planets, output $-1$ for that entry.

### Constraints
* $1 \le K \le N \le 100$
* Distances are non-negative integers or $-1$ (indicating no direct route). ($-1 \leq d \leq 10^6$)
* The distance from a planet to itself is always $0$.

### Example input
    5 3
    0 3 -1 1 -1
    -1 0 1 -1 -1
    -1 -1 0 1 -1
    4 1 -1 0 5
    -1 -1 -1 -1 0

### Example output
    0 3 4 1 -1
    -1 0 1 2 -1
    -1 -1 0 1 -1
    4 1 2 0 5
    -1 -1 -1 -1 0

### Explanation of the example
![](tex/abra.png)

The output is an $N \times N$ matrix. Each entry $(i, j)$ contains the shortest distance from planet $i$ to planet $j$ using only Republic-controlled planets ($1$ to $K$) as intermediate stops. If no such path exists, the entry is $-1$. For example:
- The shortest path from planet $1$ to planet $3$ is $1 \to 2 \to 3$, with a total distance of $4$.
- There is no path from planet $2$ to planet $1$, so the output is $-1$ in that position.
- The shortest path from planet $2$ to planet $3$ is a direct route with a distance of $1$.
- The shortest path from planet $4$ to planet $3$ goes through Republic planets: $4 \to 2 \to 3$ with total distance $1 + 1 = 2$.
- Planet $5$ can not be reached from Republic-controlled planets, because it is only reachable from planet $4$.