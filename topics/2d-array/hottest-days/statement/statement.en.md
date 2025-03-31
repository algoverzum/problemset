## Hottest Days
Given the daily highest recorded temperature for each of the past $M$ days in $N$ cities. Let $H$ denote the maximum temperature that occurred. Determine, for each city, how many days had a temperature of $H$ degrees.

### Input
The first line of the input contains two integers: $N$ and $M$ - the number of cities and the number of days. The following $N$ lines each contain $M$ integers separated by spaces. The $j$-th number in the $i$-th row, $T_{i,j}$, represents the maximum daily temperature on the $j$-th day in the $i$-th city.

### Output
Print $N$ numbers, each on a separate line. The $i$-th line should contain the number of days in which the maximum temperature $H$ occurred in the $i$-th city.

### Constraints
* $1 \le N, M \le 100$
* $-50 \le T_{i,j} \le 50$

### Example input
    3 4
    2 -3 5 18
    18 18 18 18
    10 0 16 17

### Example output
    1
    4
    0

### Explanation of the example
The maximum temperature is $H = 18$ degrees. In the first city, 18 degrees occurred once; in the second city, it occurred four times; in the third city, it did not occur at all.
