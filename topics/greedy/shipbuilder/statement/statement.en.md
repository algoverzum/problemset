## Shipbuilder
You are a successful spaceship-building entrepreneur who has become so popular that you're receiving more orders than you can handle. Fortunately, thanks to your advanced equipment, you can build any spaceship in exactly one day.
You are given a list of $N$ orders, where each order has a deadline. The deadlines are given in increasing order. An order is considered completed on time if it is finished on or before its deadline.
Determine the maximum number of spaceships you can build on time and output the indices of the orders you complete.

### Input
The first line of the input contains a single integer:
$N$ — the number of orders.<br>
The second line of the input contains $N$ integers: $H_1, H_2, \ldots, H_N$, where $H_i$ is the deadline of the $i$-th order.

### Output
The first line of the output should contain a single integer:
$S$ — the number of orders you completed on time.<br>
The second line should contain $S$ integers in increasing order: the 1-based indices of the orders you completed.

### Constraints
* $1 \le N, H_i \le 100\,000$
* $H_i \le H_j$ for all $1 \le i < j \le N$

### Example input
    7
    1 1 2 2 2 4 4

### Example output
    4
    1 3 6 7

### Explanation of the example
On day 1, you build order 1 (deadline: day 1).<br>
On day 2, you build order 3 (deadline: day 2).<br>
On day 3, you build order 6 (deadline: day 4).<br>
On day 4, you build order 7 (deadline: day 4).
