## Median
We're testing a new spacecraft and we've measured a few times how long it took us to get it out of the atmosphere. We want to launch it to the market, but we need to know the median time it takes to get out of the atmosphere. Write a program that finds this number. The median of a set of numbers is the number exactly in the middle in ascending order. This is unambiguous for an odd number of elements, and for an even number of elements, you should take the lower of the two in the middle.

### Input
The first line of the input contains a single integer, the number of measurements: $N$.
The second line of the input contains $N$ integers, the results of the measurements: $A_1, A_2, \ldots, A_N$ .

### Output
Print a single integer number, the median value of the measurements.

### Constraints
* $1 \le N \le 100$
* $1 \le A_i \le 1000$

### Example input
    6
    5 4 1 1 4 3

### Example output
    3

### Explanation of the example
The numbers in order are: 1 1 3 4 4 5. The middle numbers are 3 and 4, and the lower out of those two is 3.
