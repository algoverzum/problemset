## Cheapest Long Travel
My friend Akiko has $N$ space trips to choose from. For each trip, the distance to the destination in light years and the cost of the trip in thalers are known. He wants to travel at least $K$ light years, and he will choose the cheapest of these trips. How much will it cost him?

### Input
The first line of the input contains two integers separated by spaces: $N,K$, the number of possible space trips, and the desired minimum distance. The second line contains $N$ integers separated by spaces, the distances to the destination in light years for each trip ($A_1, A_2, \ldots, A_N$). The third line contains $N$ integers separated by spaces, the costs for each trip in thalers ($B_1, B_2, \ldots, B_N$).

### Output
Print a single number, the cheapest price among the trips that are at least $K$ light years away, or $-1$ if there is no such trip.

### Constraints
* $1 \le N \le 1000$
* $1 \le A_i \le 1000$
* $1 \le B_i \le 1000$

### Example 1 input
    5 10
    100 5 9 20 15
    999 100 1 50 100

### Example 1 output
    50

### Explanation of example 1
Trip 4 is the cheapest among those that are at least 10 light years away.

### Example 2 input
    2 10
    5 6
    12 345

### Example 2 output
    -1

### Explanation of example 2
There is no travel of at least 10 light years.
