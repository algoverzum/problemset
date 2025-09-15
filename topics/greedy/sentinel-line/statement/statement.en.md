## Sentinel Line
The Federation operates $N$ observation stations along a straight border line. We want to install cloaking generators that hide stations within a radius of $H$. Cloaking generators **can only be placed at the locations of observation stations**.

Task: select stations to install generators so that **all stations are covered with the minimal number of generators**.

For example, if the station coordinates are $0, 10, 30, 40, 60, 85, 100$, and generators have a radius of $20$, then three generators are enough: at positions 10, 60, and 100 (other solutions are also possible).

![](tex/abra.png)

### Input
The first line contains two numbers: $N$ and $H$ — the number of observation stations and the generator radius.

The second line contains $N$ numbers: $A\_1, A\_2, \ldots, A\_N$ — the distances of the observation stations from the first one ($A\_1 = 0$, $A\_i < A\_{i+1}$ for $1 \le i \le N-1$).

### Output
The first line should contain a single number: $M$ — the minimal number of generators required.

The second line should contain exactly $M$ integers, in order, representing the indices of the observation stations where generators should be installed.

If multiple solutions exist, any of them is acceptable.

### Constraints
* $1 \le N \le 10^5$
* $1 \le H \le 10^9$
* $0 \le A_1 < A_2 < \ldots < A_N \le 10^9$

### Example input
    7 20
    0 10 30 40 60 85 100

### Example output
    3
    2 5 7

### Explanation of the example
Installing cloaking generators at stations 2, 5, and 7 covers all stations. Other combinations are also possible, e.g., stations 1, 4, and 6.
