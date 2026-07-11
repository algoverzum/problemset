## Cheapest Long Travel
My friend Akiko has $N$ space trips to choose from. For each trip, we kow the distance to the destination in light years and the price of the trip in thalers. He wants to travel at least $K$ light years, and he will choose the cheapest of these trips. How much will it cost him?

### Input
The first line of the input contains a single integer, $N$, the number of available space trips.

The second line contains a single integer, $K$, the required minimum distance.

The next $2N$ lines contain the data for the trips. For each trip, there are two consecutive lines: first the distance to the destination, $D_i$, in light-years, then the price of the trip, $P_i$, in thalers.

### Output
Print a single number, the cheapest price among the trips that are at least $K$ light years away, or $-1$ if there is no such trip.

### Constraints
* $1 \le N \le 1000$
* $1 \le D_i \le 1000$
* $1 \le P_i \le 1000$

### Example 1 input
    5
    10
    100
    999
    5
    100
    9
    1
    20
    50
    15
    100

### Example 1 output
    50

### Explanation of example 1
Trip 4 is the cheapest among those that are at least 10 light years away.

### Example 2 input
    2
    10
    5
    12
    6
    345

### Example 2 output
    -1

### Explanation of example 2
There is no travel of at least 10 light years.
