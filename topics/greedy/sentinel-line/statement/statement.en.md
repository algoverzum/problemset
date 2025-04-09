## Sentinel Line
The Federation operates $N$ observation stations along a straight line on the Romulan border. To enhance their security, they have decided to install new high-performance cloaking generators to replace the old ones. A new cloaking generator provides coverage within a radius of $H$, concealing all stations within this range from prying eyes (e.g., Romulan Tal Shiar or Klingon Intelligence).

All old cloaking generators will be discarded, but it is not necessary to replace each one. However, new generators can only be installed at the location of an observation station.

Write a program that determines the minimum number of new cloaking generators required and specifies the stations where they should be installed so that every observation station falls within the range of at least one new cloaking field.

### Input
The first line of the input contains two integers: $N, H$ - the number of observation stations and the radius of a new cloaking generator.

The second line contains $N$ integers $A_1, A_2, \ldots, A_N$ - the distances of the observation stations from the first one ($A_i < A_{i+1}$).

### Output
The first line of the output should contain a single integer $M$ - the minimum number of new cloaking generators required.

The second line should contain exactly $M$ integers in order, the indices of the observation stations where new cloaking generators should be installed, so that all observation stations are within range of at least one!

If multiple solutions exist, any of them may be given.

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
One possible solution is to use stations 2, 5, and 7. Another valid option could be to use stations 1, 4, and 6 instead.
