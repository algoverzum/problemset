## Max Temperature Variation
Our magical weather forecast animal, the yoshie has given the expected minimum and maximum temperatures for the next $N$ days. What will be the largest daily temperature variation? (That is, how large can the difference be between the maximum temperature and the minimum temperature for that day?)

### Input
The first line of the input contains a single integer, $N$, the number of days in the weather forecast.

The next $2N$ lines contain the temperatures. For each day, there are two consecutive lines: first the minimum temperature $A_i$, then the maximum temperature $B_i$.

### Output
Print a single number, the value of the largest daily temperature variation.

### Constraints
* $1 \le N \le 100$
* $-50 \le A_i \leq B_i\le 50$

### Example input
    5
    10
    15
    4
    8
    -5
    -1
    -2
    0
    -5
    1

### Example output
    6

### Explanation of the example
The first day $15-10=5$ is the temperature variation. Then $8-4=4$, $-1-(-5)=4$, $0-(-2)=2$, $1-(-5)=6$. The maximum of these is 6.
