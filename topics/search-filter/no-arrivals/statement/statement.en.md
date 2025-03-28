## No Arrivals
Every day at a spacecraft station we recorded how many incoming spacecraft we saw that day. Among the days recorded was a holiday when there was no traffic, so no spacecraft arrived that day. Your task is to find the index of the day on which this holiday fell.

### Input
The first line of the input contains a single integer, the number of days $N$
In the following $N$ lines each there a single integer, the number of spaceships that landed on that day: $A_1, A_2, \dots, A_N$

### Output
Print a single integer, the index of the day with 0 arrivals.

### Constraints
* $1 \le N \le 100$
* $0 \le A_i \le 100$

### Example 1 input
    6
    20
    1
    0
    3
    10
    6

### Example 1 output
    3

### Explanation of the example
On the third day there were no arrivals.

### Example 2 input
    6
    32
    13
    41
    52
    13
    0

### Example 2 output
    6
