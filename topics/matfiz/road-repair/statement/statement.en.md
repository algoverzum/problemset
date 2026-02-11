## Shortest Road Repair

An $N$ kilometer long road is being repaved in sections due to its poor condition. The repaving is done $M$ times. For each occasion, we know from which kilometer ($K_i$) to which kilometer ($V_i$) the section is repaved.

Write a program that determines the length of the shortest renovation! If there are multiple such renovations, you must output all of them!

### Input

The first line of the standard input contains the length of the road ($N$) and the number of renovations ($M$), and below it, each line contains the data of a renovation ($K_i$, $V_i$).

### Output

The first line of the standard output must contain a single integer, the length of the shortest renovation!

The following line(s) must contain the serial number of the renovation! If there are multiple identical shortest renovations, you must write their serial numbers in separate lines, in ascending order!

### Constraints

- $1 \le N \le 100000$
- $1 \le M \le 100$
- $0 \le K_i \le V_i \le N$

### Example Input

    100 5
    0 1
    0 5
    75 95
    12 17
    13 14

### Example Output

    2
    1
    5

### Explanation of the example

Since both 0–1 and 13–14 mean a 2-kilometer-long renovation, this is what is in the first line. In the next two lines are their indexes, 1 and 5.
