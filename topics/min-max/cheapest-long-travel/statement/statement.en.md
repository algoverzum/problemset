## Cheapest Long Travel
My friend Akiko has $N$ space trips to choose from. For each trip, we kow the distance to the destination in light years and the price of the trip in thalers. He wants to travel at least $K$ light years, and he will choose the cheapest of these trips. How much will it cost him?

### Input
The first line of the input contains two integers separated by spaces: $N,K$, the number of possible space trips, and the desired minimum distance. The second line contains $N$ integers separated by spaces, the distances to the destination in light years for each trip ($D_1, D_2, \ldots, D_N$). The third line contains $N$ integers separated by spaces, the prices for each trip in thalers ($P_1, P_2, \ldots, P_N$).

### Output
Print a single number, the cheapest price among the trips that are at least $K$ light years away, or $-1$ if there is no such trip.

### Constraints
* $1 \le N \le 1000$
* $1 \le D_i \le 1000$
* $1 \le P_i \le 1000$

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
