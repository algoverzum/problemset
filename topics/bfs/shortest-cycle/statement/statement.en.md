## Shortest Cycle
On the planet Kuklos, the cities are numbered from $1$ to $N$. Some of the cities are connected by roads, and each road can be used in both directions.

We are currently in city $P$, and we would like to take a short trip. It is important that:

* the trip returns to the starting city $P$,
* each road is used **at most** once,
* and we find the shortest possible such cycle.

Your task is to find the shortest route that starts and ends in city $P$, visits one or more other cities, and does not use any road more than once.

### Input
The first line contains three integers: $N$ – the number of cities, $M$ – the number of roads, and $P$ – the starting city.
Then $M$ lines follow, each containing two integers $A_i$ and $B_i$, meaning there is a road between city $A_i$ and city $B_i$.

### Output
The first line should contain a single integer: the length of the shortest cycle that can be found (i.e. the number of roads used). If no such cycle exists, print $-1$.

In the second line, print the cities in the order they are visited in the cycle.
(You may assume the cycle ends by returning from the last listed city back to the first - you don't need to print that final edge.)

If there are multiple valid solutions with the same length, any one of them is acceptable.

### Constraints
* $1 \le N \le 100000$
* $1 \le M \le 200000$
* $1 \le P \le N$
* $1 \le A_i, B_i \le N$ for each $i = 1, 2, \ldots, N$

### Example input
    8 10 2
    1 3
    3 6
    3 2
    2 4
    2 5
    6 7
    6 8
    1 8
    5 3
    4 7

### Example output
    3
    2 5 3

### Explanation of the example
The shortest cycle consists of the roads: 2-5, 5-3 and 3-2.  The cities may be given in any order, as long as it still forms a cycle. For example 5 2 3 is also a valid solution.

![](tex/abra.png)
