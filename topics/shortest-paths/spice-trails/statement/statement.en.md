## Spice Trails
Vladimir Harkonnen is setting out from the planet Arrakis to explore the known universe. The planets are numbered from 0 to $N-1$, and Arrakis is planet 0.

You are given a directed graph representing the possible interplanetary travel routes. Direct travel between two planets is only possible if it is explicitly listed in the input. Each trip requires spice: traveling directly from planet $i$ to planet $j$ costs $S_{i,j}$ units of spice.

Write a program that starts from Arrakis (planet 0) and, for each $i = 1, 2, \ldots, N-1$, determines the minimum amount of spice required to reach each other planet in at most $i$ steps.

If a planet cannot be reached within $i$ steps, output $-1$ for that position.

### Input
The first line contains two integers, $N$ and $M$ — the number of planets and the number of travel routes.

The next $M$ lines contain three integers, the $k$th line contains: $U_k$, $V_k$, and $W_k$ — indicating that there is a directed edge from planet $U_k$ to planet $V_k$ with a spice cost of $W_k$ (a positive integer). 

### Output
Your program should output $N-1$ lines.
Each line should contain $N-1$ integers, separated by spaces.
The $i$-th line (for $i = 1, \ldots, N-1$) should contain, for each planet except planet 0, the minimum amount of spice needed to reach that planet in at most $i$ steps.
If a planet cannot be reached within $i$ steps, print $-1$ in that position.

### Constraints
* $2 \le N \le 1000$
* $0 \le M \le 2000$
* $0 \le U_k \not= V_k \le N-1$ for all $k = 1, 2, \ldots, M$
* $1 \le W_k \le 10^6$ for all $k = 1, 2, \ldots, M$

### Example 1 input
    4 5
    0 1 5
    0 2 2
    2 3 10
    2 1 1
    1 3 4

### Example 1 output
    5 2 -1
    3 2 9
    3 2 7

### Explanation of example 1
The diagram shows the graph on the left and step-by-step reachable planets on the right:

![](tex/abra.png)

1 step: Planets 1 and 2 are reachable from planet 0 for 5 and 2 spice respectively.
2 steps: Planet 1 becomes reachable for 3 spice (via planet 2), and planet 3 can be reached for 9.
3 steps: Planet 2 becomes reachable for 7 spice (via a longer path).

### Example 2 input
    4 5
    0 1 2
    2 0 1
    1 2 3
    2 1 1
    2 3 4

### Example 2 output
    2 -1 -1
    2 5 -1
    2 5 9
